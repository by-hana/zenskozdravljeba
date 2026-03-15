"""
Two-step AI content generation using Claude API.
Step 1: Generate article outline
Step 2: Generate full article from outline

Content language: Bosnian (Latin script only)
Topic domain: women's health
"""

import json
import re
import time

import anthropic
from django.conf import settings


def get_client():
    return anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)


SYSTEM_PROMPT = """Ti si strucni pisac zdravstvenih clanaka za ZenskoZdravlje.ba,
bosanski portal o zenskom zdravlju. Pises na bosanskom jeziku koristeci ISKLJUCIVO
latinicno pismo. Nikad ne koristis cirilicu ni engleski jezik u samom sadrzaju.
Tvoji clanci su medicinski tacni, razumljivi, korisni i optimizirani za SEO i
LLM pretragu. Ton je topao, profesionalan i empaticni. Bavi se temama reproduktivnog
zdravlja, hormona, ginekoloskog zdravlja, ishrane i mentalnog zdravlja zena."""


def generate_outline(keyword: str, cluster: str, is_pillar: bool = False) -> dict:
    """
    Step 1: Generate article outline.
    Returns dict with: title, meta_title, meta_description, search_intent,
    sections, faq_questions, suggested_internal_topics, key_takeaways
    """
    word_target = "2500-3500 rijeci (pillar clanak)" if is_pillar else "1200-2000 rijeci"

    client = get_client()

    prompt = f"""Kreiraj detaljan outline za SEO clanak na bosanskom jeziku.

Kljucna rijec / tema: {keyword}
Tematski klaster: {cluster}
Duljina: {word_target}

Vrati ISKLJUCIVO JSON objekat (bez komentara, bez markdown, bez objasnjavanja) sa sljedecim poljima:

{{
  "title": "SEO-optimiziran naslov clanka (max 65 znakova)",
  "meta_title": "Meta title (max 65 znakova, ukljuci kljucnu rijec)",
  "meta_description": "Meta opis (max 155 znakova, uvjerljiv i informativan)",
  "search_intent": "Kratko objasnjenje sto korisnik trazi ovim upitom",
  "sections": [
    {{
      "heading": "H2 naslov sekcije",
      "type": "definition|explanation|list|example|comparison",
      "subsections": ["H3 podnaslov 1", "H3 podnaslov 2"]
    }}
  ],
  "faq_questions": [
    "Pitanje 1?",
    "Pitanje 2?",
    "Pitanje 3?",
    "Pitanje 4?",
    "Pitanje 5?"
  ],
  "key_takeaways": [
    "Kljucni zakljucak 1",
    "Kljucni zakljucak 2",
    "Kljucni zakljucak 3",
    "Kljucni zakljucak 4"
  ],
  "suggested_internal_topics": [
    "tema za interni link 1",
    "tema za interni link 2",
    "tema za interni link 3"
  ]
}}

Sekcije moraju ukljucivati:
1. Kratki odgovor / brzi rezime (prva sekcija)
2. Definicija pojma
3. 3-5 glavnih sekcija s objasnjenjima
4. Prakticni savjeti ili primjeri
5. FAQ sekcija (5 pitanja)
6. Kljucni zakljucci

Sve na bosanskom latinicnom pismu."""

    for attempt in range(3):
        try:
            response = client.messages.create(
                model="claude-opus-4-6",
                max_tokens=2000,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
            raw = response.content[0].text.strip()
            # Extract JSON if wrapped in markdown
            json_match = re.search(r'\{.*\}', raw, re.DOTALL)
            if json_match:
                raw = json_match.group()
            return json.loads(raw)
        except json.JSONDecodeError:
            if attempt == 2:
                raise
            time.sleep(2)
        except anthropic.RateLimitError:
            time.sleep(60)
        except anthropic.APIError as e:
            if attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))

    return {}


def generate_article(
    outline: dict,
    keyword: str,
    is_pillar: bool = False,
    pillar_title: str = '',
    pillar_slug: str = '',
    related_posts: list = None,
) -> dict:
    """
    Step 2: Generate full article HTML from outline.
    Returns dict with: intro, content_html, faq_json, word_count_estimate
    """
    word_target = "2500-3500 rijeci" if is_pillar else "1200-2000 rijeci"
    related_posts = related_posts or []

    # Build internal links instruction
    internal_links_text = ''
    if pillar_title and pillar_slug:
        internal_links_text += f'\n- Linkuj na pillar clanak: "{pillar_title}" (URL: /blog/{pillar_slug}/)'
    for rp in related_posts[:3]:
        internal_links_text += f'\n- Linkuj na srodan clanak: "{rp["title"]}" (URL: /blog/{rp["slug"]}/)'

    sections_text = '\n'.join(
        f'- {s["heading"]}' + (
            '\n  ' + '\n  '.join(f'- {sub}' for sub in s.get('subsections', []))
            if s.get('subsections') else ''
        )
        for s in outline.get('sections', [])
    )

    faq_text = '\n'.join(f'{i+1}. {q}' for i, q in enumerate(outline.get('faq_questions', [])))
    takeaways_text = '\n'.join(f'- {t}' for t in outline.get('key_takeaways', []))

    client = get_client()

    prompt = f"""Napisi kompletan SEO clanak na bosanskom jeziku prema outline-u ispod.

NASLOV: {outline.get('title', keyword)}
KLJUCNA RIJEC: {keyword}
CILJNA DULJINA: {word_target}

STRUKTURA:
{sections_text}

FAQ PITANJA:
{faq_text}

KLJUCNI ZAKLJUCCI:
{takeaways_text}

INTERNI LINKOVI (obavezno ukljuci u tekst):
{internal_links_text if internal_links_text else 'Nema specificiranih internih linkova.'}

UPUTE ZA PISANJE:
1. Pisi ISKLJUCIVO na bosanskom latinicnom pismu
2. Pocni s kratkim reziméom (2-3 recenice koje direktno odgovaraju na glavno pitanje)
3. Koristi semanticki HTML: <h2>, <h3>, <p>, <ul>, <ol>, <li>, <strong>, <blockquote>
4. Kljucnu rijec koristi prirodno, ne pretjeruj
5. Kratke paragrafe (2-4 recenice)
6. Ukljuci barem 2 bulleted liste
7. FAQ sekcija mora imati <h2>Cesto postavljana pitanja</h2> i svako pitanje kao <h3>
8. Zavrsi sa <h2>Kljucni zakljucci</h2> i bulleted listom
9. Za interne linkove koristi: <a href="/blog/SLUG/">NASLOV</a>
10. Nemoj ukljucivati naslov clanka na vrhu (samo sadrzaj)
11. Nemoj koristiti em-dash, umjesto toga koristi dvotacku ili zarez

VRATI ISKLJUCIVO JSON objekat:
{{
  "intro": "Uvodni paragraf (2-3 recenice, direktan odgovor na upit)",
  "content_html": "<p>Cio HTML sadrzaj clanka ovdje...</p>",
  "faq_json": [
    {{"question": "Pitanje?", "answer": "Odgovor u 2-4 recenice."}},
    {{"question": "Pitanje 2?", "answer": "Odgovor."}}
  ]
}}"""

    for attempt in range(3):
        try:
            response = client.messages.create(
                model="claude-opus-4-6",
                max_tokens=8000,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
            raw = response.content[0].text.strip()
            json_match = re.search(r'\{.*\}', raw, re.DOTALL)
            if json_match:
                raw = json_match.group()
            return json.loads(raw)
        except json.JSONDecodeError:
            if attempt == 2:
                raise
            time.sleep(2)
        except anthropic.RateLimitError:
            time.sleep(60)
        except anthropic.APIError:
            if attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))

    return {}
