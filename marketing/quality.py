"""Quality scoring for AI-generated blog posts. Score 0-100."""

import re
from bs4 import BeautifulSoup


def count_words(html: str) -> int:
    text = BeautifulSoup(html, 'html.parser').get_text()
    return len(text.split())


def count_headings(html: str) -> dict:
    soup = BeautifulSoup(html, 'html.parser')
    return {
        'h2': len(soup.find_all('h2')),
        'h3': len(soup.find_all('h3')),
        'total': len(soup.find_all(['h2', 'h3', 'h4'])),
    }


def keyword_density(html: str, keyword: str) -> float:
    if not keyword:
        return 0.0
    text = BeautifulSoup(html, 'html.parser').get_text().lower()
    words = text.split()
    if not words:
        return 0.0
    kw_lower = keyword.lower()
    count = sum(1 for w in words if kw_lower in w)
    return count / len(words) * 100


def avg_sentence_length(html: str) -> float:
    text = BeautifulSoup(html, 'html.parser').get_text()
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    if not sentences:
        return 0.0
    total_words = sum(len(s.split()) for s in sentences)
    return total_words / len(sentences)


def score_article(content_html: str, keyword: str = '', faq_json=None, intro: str = '', is_pillar: bool = False) -> tuple[float, int]:
    """
    Returns (quality_score: float, word_count: int).
    Auto-publish threshold: score >= 85.
    """
    score = 0.0
    word_count = count_words(content_html)
    headings = count_headings(content_html)

    # 1. Word count (30 points)
    if is_pillar:
        target_min, target_max = 2000, 3500
    else:
        target_min, target_max = 1200, 2000

    if word_count >= target_min:
        score += 20
        if word_count <= target_max * 1.2:
            score += 10
    elif word_count >= target_min * 0.8:
        score += 12
    elif word_count >= 800:
        score += 6

    # 2. Heading structure (20 points)
    if headings['h2'] >= 3:
        score += 12
    elif headings['h2'] >= 2:
        score += 8
    elif headings['h2'] >= 1:
        score += 4

    if headings['h3'] >= 2:
        score += 8
    elif headings['h3'] >= 1:
        score += 4

    # 3. Keyword usage (15 points)
    density = keyword_density(content_html, keyword)
    if 0.5 <= density <= 2.5:
        score += 15
    elif 0.3 <= density <= 3.5:
        score += 10
    elif density > 0:
        score += 5

    # 4. FAQ presence (15 points)
    if faq_json and len(faq_json) >= 4:
        score += 15
    elif faq_json and len(faq_json) >= 2:
        score += 10
    elif faq_json:
        score += 5

    # 5. Intro present (5 points)
    if intro and len(intro.split()) >= 40:
        score += 5

    # 6. Readability - avg sentence length (10 points)
    avg_len = avg_sentence_length(content_html)
    if 12 <= avg_len <= 22:
        score += 10
    elif 10 <= avg_len <= 28:
        score += 7
    elif avg_len > 0:
        score += 3

    # 7. Has bullet lists (5 points)
    soup = BeautifulSoup(content_html, 'html.parser')
    if soup.find_all('ul'):
        score += 5
    elif soup.find_all('ol'):
        score += 3

    return round(min(score, 100), 1), word_count
