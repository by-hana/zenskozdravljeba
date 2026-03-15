"""
Two-step AI content generation using Claude API.

Step 1 — generate_outline(): search intent analysis + heading structure
Step 2 — generate_article(): full article with SEO/LLM writing guidelines baked in

Writing guidelines incorporated:
- SEO/AI Writing Guide (for articles) — ZenskoZdravlje.ba
- Brand voice: expert women's health portal (we/our in Bosnian: mi/nas/nase)
- 80% education / 20% brand experience
- Direct answer first, then elaborate
- Self-contained sentences (snippable for AI/LLM)
- No em dashes, no AI clichés, no contrastive reframing
- Short sections (1-2 paragraphs), Q&A FAQ format
- Ground all claims with specifics; cite sources inline
- Single CTA at the end

Language: Bosnian Latin script only (NO Cyrillic)
"""

import json
import re
import time

import anthropic
from django.conf import settings


def get_client():
    return anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)


# ─── System prompt ────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """Ti si ekspertni pisac zdravstvenih članaka za ŽenskoZdravlje.ba,
bosanski informativni portal o ženskom zdravlju.

IDENTITET I GLAS:
- Pišeš KAO član tima ŽenskoZdravlje.ba — koristi "mi", "nas", "naše" prirodno
- Ton: topao, stručni, direktan. Kao da razgovaraš s prijateljicom koja je doktor
- 80% edukacija (savjeti koje svaka žena može primijeniti), 20% iskustvo brenda
- Budi konkretna — brojevi, statistike, primjeri su vrijedniji od općih tvrdnji

JEZIK I FORMAT:
- OBAVEZNO koristi bosanska slova s dijakritičkim znakovima: č, ć, š, ž, đ
- Svaka riječ koja zahtijeva dijakritik MORA ga imati: što (ne sto), često (ne cesto), žena (ne zena), zdravlje (ne zdravlje), članak (ne clanak), stručni (ne strucni), također (ne takodjer)
- ISKLJUČIVO bosanski latinični pismo — nikad ćirilica, nikad engleski sadržaj
- Kratke rečenice. Kratki paragrafi (2-4 rečenice max)
- Svaka rečenica treba imati smisao i ako se izvuče iz konteksta
- Direktno odgovori na pitanje PRVO, zatim objasni

ZABRANJENA PONAŠANJA:
- Bez em-crtica (—). Umjesto toga koristi dvotačku ili zarez
- Bez AI klišeja: "nije X, već Y", "u današnje digitalno doba", "ključno je", "važno je napomenuti"
- Bez praznih tvrdnji: umjesto "zdravlje je bitno" piši "redovni pregledi smanjuju rizik od raka grlića za 70%"
- Bez uvodnih fraza tipa "U ovom članku ćemo..." — kreni odmah s odgovorom
- Bez dekorativnih simbola (strelice, zvjezdice, uskličnici)
- Bez kontrastivnog preoblikovanja ("nije samo alat, to je revolucija")
- Bez navoda koji su generički ili neprovjerivi. Ako nemaš podatak, ne izmišljaj ga

MEDICINSKA TAČNOST:
- Budi tačna. Ovo je zdravstveni portal — dezinformacije mogu štetiti čitateljicama
- Razlikuj "istraživanja pokazuju" od "stručnjaci preporučuju"
- Uvijek savjetuj da se konsultuju s doktorom za individualne slučajeve"""


# ─── Step 1: Outline ─────────────────────────────────────────────────────────

def generate_outline(keyword: str, cluster: str, is_pillar: bool = False) -> dict:
    """
    Step 1: Analyse search intent, determine article type and structure.
    Returns structured outline for use in generate_article().
    """
    word_target = "2500-3500 rijeci (pillar/stub clanak)" if is_pillar else "1200-2000 rijeci"

    client = get_client()

    prompt = f"""Analiziraj pretragu i kreiraj outline za SEO clanak.

KLJUCNA RIJEC: {keyword}
KLASTER: {cluster}
CILJNA DULJINA: {word_target}

KORAK 1 — ANALIZA PRETRAGE:
Promisli: Sta tacno zena trazi kada ukuca "{keyword}" u Google ili ChatGPT?
- Koja je primarna namjera (informaciona, dijagnosticka, prakticna)?
- Koji format clanaka najvise odgovara ovoj namjeri? (vodic, lista, Q&A, objasnjenje, usporedba)
- Sta bi citateljica htjela znati ODMAH, u prvoj recenici?

KORAK 2 — STRUKTURA:
Kreiraj naslove sekcija koji:
- Odgovaraju na pitanje koje bi stvarna osoba upisala u Google ili ChatGPT
- Slijede prirodnu hijerarhiju (H2 > H3)
- Nisu prepuni kljucnih rijeci — prirodan jezik na prvom mjestu
- Kljucna rijec se pojavljuje u H1/naslovu i mozda jos 1-2 puta u H2 naslovima, ali NE forsirati

KORAK 3 — FAQ:
Svako FAQ pitanje mora biti SPECIFICNIJE od naslova clanka (manje konkurentno, dugi rep).
Ne postavljaj ista pitanja kao naslovi sekcija.

Vrati ISKLJUCIVO JSON (bez markdown, bez komentara):

{{
  "title": "Naslov clanka — kljucna rijec sto blize pocetku, max 65 znakova, ukljuci godinu 2025 gdje ima smisla",
  "meta_title": "Meta title — max 65 znakova, kljucna rijec na pocetku",
  "meta_description": "Meta opis — 150-160 znakova, direktan, konkretan, povecaj CTR",
  "article_type": "guide|list|qa|explanation|comparison",
  "search_intent": "Jedna recenica: sta citateljica trazi i sta ocekuje naci",
  "opening_answer": "2-3 recenice koje direktno odgovaraju na primarno pitanje. Ovo ce biti uvod clanka. Pisi kao da ces biti izvucena u Google featured snippet. Samoodrzive recenice.",
  "brand_mention": "Kratka recenica koja prirodno spominje ZenskoZdravlje.ba tim u kontekstu teme, bez promocije. Npr: Na ZenskoZdravlje.ba cesto dobijamo pitanja o ovoj temi...",
  "sections": [
    {{
      "heading": "H2 naslov — sto bi neko upisao u Google",
      "type": "definition|explanation|list|example|comparison|qa",
      "notes": "Kratka napomena sta ova sekcija treba sadrzavati",
      "subsections": [
        {{"heading": "H3 podnaslov", "notes": "sta pokriva"}}
      ]
    }}
  ],
  "comparison_table_opportunity": "Kratki opis da li i gdje bi tabela usporedbe imala smisla, ili null",
  "faq_questions": [
    "Specificno pitanje 1 (dugi rep, manje konkurentno)?",
    "Specificno pitanje 2?",
    "Specificno pitanje 3?",
    "Specificno pitanje 4?",
    "Specificno pitanje 5?"
  ],
  "key_takeaways": [
    "Konkretan zakljucak 1 — sa brojem ili specificom gdje moguce",
    "Konkretan zakljucak 2",
    "Konkretan zakljucak 3",
    "Konkretan zakljucak 4"
  ],
  "cta_text": "Kratki poziv na akciju za kraj clanka — uputi citateljicu da posjeti ZenskoZdravlje.ba blog za vise informacija ili slicne clanke. Bez 'kontaktirajte nas' — informativno."
}}

Sve na bosanskom latinicnom pismu."""

    max_tokens = 5000 if is_pillar else 3500
    outline = _call_api(client, prompt, max_tokens=max_tokens)
    # Restore diacritics on string fields
    for field in ('title', 'meta_title', 'meta_description', 'search_intent',
                  'opening_answer', 'brand_mention', 'cta_text'):
        if outline.get(field):
            outline[field] = restore_diacritics(outline[field], client)
    return outline


# ─── Step 2: Full article ─────────────────────────────────────────────────────

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
    Returns dict with: intro, content_html, faq_json
    """
    word_target = "2500-3500 rijeci" if is_pillar else "1200-2000 rijeci"
    related_posts = related_posts or []

    # Internal links block
    internal_links_lines = []
    if pillar_title and pillar_slug:
        internal_links_lines.append(
            f'- Pillar clanak: "{pillar_title}" → <a href="/blog/{pillar_slug}/">{pillar_title}</a>'
        )
    for rp in related_posts[:3]:
        internal_links_lines.append(
            f'- Srodni clanak: "{rp["title"]}" → <a href="/blog/{rp["slug"]}/">{rp["title"]}</a>'
        )
    internal_links_text = '\n'.join(internal_links_lines) if internal_links_lines else 'Nema specificiranih internih linkova.'

    # Build sections text with notes
    sections_lines = []
    for s in outline.get('sections', []):
        sections_lines.append(f'H2: {s["heading"]}')
        if s.get('notes'):
            sections_lines.append(f'    Napomena: {s["notes"]}')
        for sub in s.get('subsections', []):
            if isinstance(sub, dict):
                sections_lines.append(f'  H3: {sub["heading"]}')
                if sub.get('notes'):
                    sections_lines.append(f'      Napomena: {sub["notes"]}')
            else:
                sections_lines.append(f'  H3: {sub}')
    sections_text = '\n'.join(sections_lines)

    faq_text = '\n'.join(
        f'{i+1}. {q}' for i, q in enumerate(outline.get('faq_questions', []))
    )
    takeaways_text = '\n'.join(f'- {t}' for t in outline.get('key_takeaways', []))
    opening_answer = outline.get('opening_answer', '')
    brand_mention = outline.get('brand_mention', '')
    cta_text = outline.get('cta_text', 'Za vise informacija o zenskom zdravlju, procitajte nase ostale clanke na ZenskoZdravlje.ba.')
    table_opportunity = outline.get('comparison_table_opportunity', '')

    client = get_client()

    prompt = f"""Napisi kompletan, SEO-optimiziran clanak na bosanskom jeziku.

=== META INFORMACIJE (ne ukljucuj u content_html) ===
Naslov: {outline.get('title', keyword)}
Kljucna rijec: {keyword}
Ciljna duljina: {word_target}
Tip clanka: {outline.get('article_type', 'guide')}
Namjera pretrage: {outline.get('search_intent', '')}

=== UVOD (koristi ovo kao osnovu za intro polje) ===
Direktan odgovor: {opening_answer}
Spomen brenda: {brand_mention}

=== STRUKTURA SEKCIJA ===
{sections_text}

=== FAQ PITANJA ===
{faq_text}

=== KLJUCNI ZAKLJUCCI ===
{takeaways_text}

=== INTERNI LINKOVI (obavezno ukljuci u tekst gdje se prirodno uklapa) ===
{internal_links_text}

{f"=== MOGUCNOST ZA TABELU ==={chr(10)}{table_opportunity}" if table_opportunity else ""}

=== PRAVILA PISANJA (OBAVEZNO SLIJEDITI) ===

FORMAT:
- Semanticki HTML: <h2>, <h3>, <p>, <ul>, <ol>, <li>, <strong>, <blockquote>, <table>
- Ne ukljucuj H1 naslov — samo tijelo clanka
- Kratke sekcije: 1-2 paragrafa ispod svakog H2
- Kratki paragrafi: 2-4 recenice maksimum
- Koristiti <ul> liste kada nabrajamo stavke (barem 2 liste u clanku)
- Koristiti <table> za usporedbe: <table class="zz-table"><thead>...<tbody>...

GLAS I STIL:
- Pisi kao clan tima ZenskoZdravlje.ba — "mi pratimo", "u nasim clancima", "preporucujemo"
- Direktan odgovor PRVO, zatim pojasnjenje
- Svaka recenica mora imati smisao sama po sebi (snippable za AI)
- Konkretni podaci > opste tvrdnje: "magnezij smanjuje boli za 40%" > "magnezij pomaze"
- Primjeri i scenariji gdje god je moguce
- Kad citiras statistiku bez URL-a, navedi izvor u zagradi: (izvor: WHO, 2023)

ZABRANA:
- Bez em-crtica (—) nigdje u tekstu
- Bez kliseja: "vazno je", "kljucno je", "u danasnje doba", "nije X vec Y"
- Bez uvodnih fraza: "U ovom clanku...", "Ovaj tekst ce..."
- Bez izmisljenih statistika — ako nemas podatak, opisi kvalitativno
- Bez visekratnog ponavljanja kljucne rijeci — koristi sinonime i semanticki slicne termine

FAQ SEKCIJA:
- <h2>Cesto postavljana pitanja</h2>
- Svako pitanje kao <h3>Tekst pitanja?</h3>
- Odmah ispod: <p>Direktan odgovor u 1-3 recenice.</p>
- Ne koristiti <ul> unutar FAQ odgovora — cisti tekst

KLJUCNI ZAKLJUCCI:
- <h2>Kljucni zakljucci</h2>
- <ul> lista s konkretnim, specificnim zakljuccima

CTA (kraj clanka):
- <div class="zz-cta-inline"><p>{cta_text}</p></div>

=== SAMOPROVJERA PRIJE OUTPUTA ===
Prije nego vratis JSON, provjeri:
[ ] Uvod direktno odgovara na "{keyword}" — bez uvijanja
[ ] Kljucna rijec je prirodno u tekstu, nije forcirana
[ ] Svaka sekcija je kratka (1-2 paragrafa)
[ ] Postoje barem 2 liste (<ul>)
[ ] FAQ pitanja su specificnija od naslova (dugi rep)
[ ] Nema em-crtica nigdje
[ ] Nema AI kliseja
[ ] Interni linkovi su ukljuceni gdje se prirodno uklapaju
[ ] CTA blok je na kraju

=== OUTPUT FORMAT ===
Vrati ISKLJUCIVO JSON objekat (bez markdown kod blokova, bez objasnjavanja):

{{
  "intro": "2-3 samoodrzive recenice koje direktno odgovaraju na '{keyword}'. Ovo se prikazuje prominentno iznad clanka. Ukljuci spomen ZenskoZdravlje.ba tima gdje prirodno.",
  "content_html": "<p>Kompletan HTML sadrzaj clanka...</p>",
  "faq_json": [
    {{"question": "Specificno pitanje?", "answer": "Direktan odgovor u 1-3 recenice."}},
    {{"question": "Pitanje 2?", "answer": "Odgovor."}}
  ]
}}"""

    max_tokens = 16000 if is_pillar else 12000
    article = _call_api(client, prompt, max_tokens=max_tokens)
    # Restore diacritics on article text fields
    if article.get('intro'):
        article['intro'] = restore_diacritics(article['intro'], client)
    if article.get('content_html'):
        article['content_html'] = restore_diacritics(article['content_html'], client)
    return article


# ─── Shared API caller with retry logic ──────────────────────────────────────

def _call_api(client, prompt: str, max_tokens: int = 8000) -> dict:
    for attempt in range(3):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=max_tokens,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
            raw = response.content[0].text.strip()
            # Strip markdown code fences if present
            raw = re.sub(r'^```(?:json)?\s*', '', raw)
            raw = re.sub(r'\s*```$', '', raw)
            # Extract outermost JSON object
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


# ─── Diacritics restoration ───────────────────────────────────────────────────

def restore_diacritics(text: str, client=None) -> str:
    """
    Post-process text to restore proper Bosnian diacritics (č, ć, š, ž, đ).
    Uses claude-haiku-4-5 for speed and low cost.
    For HTML content, preserves all tags exactly — only text nodes are corrected.
    """
    if not text:
        return text
    client = client or get_client()
    # Output will be roughly same length as input; add generous buffer
    # Haiku max is 8192, so for long HTML we chunk if needed
    char_len = len(text)
    out_tokens = min(int(char_len / 3) + 500, 8000)

    system = (
        "Ti si korektor bosanskog teksta. Tvoj jedini zadatak je da dodaš ispravne "
        "dijakritičke znakove (č, ć, š, ž, đ) gdje nedostaju. "
        "Ako je ulaz HTML, sve HTML tagove (<p>, <h2>, <ul>, <li>, <strong> itd.) "
        "ostavi IDENTIČNE — mijenjaj samo tekst unutar tagova. "
        "Vrati isključivo ispravljeni tekst ili HTML, bez ikakvih objašnjenja."
    )
    for attempt in range(3):
        try:
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=out_tokens,
                system=system,
                messages=[{"role": "user", "content": text}],
            )
            result = response.content[0].text.strip()
            # Sanity check: result should be similar length; if drastically shorter, fall back
            if len(result) < char_len * 0.5:
                return text
            return result
        except Exception:
            if attempt == 2:
                return text
            time.sleep(2)
    return text
