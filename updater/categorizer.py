"""
==========================================================
Azziano Marathi News
categorizer.py

Purpose
-------
Categorize news articles.

Priority
--------
1. Feed Category (from rss_sources.py)
2. URL Mapping (url_category_map.py)
3. Keyword Matching

Version : 3.0
==========================================================
"""
DEBUG = False

import re

from config import CATEGORIES

from keywords import (
    MAHARASHTRA_KEYWORDS,
    INDIA_KEYWORDS,
    WORLD_KEYWORDS,
    SPORTS_KEYWORDS,
    BUSINESS_KEYWORDS
)

from url_category_map import URL_CATEGORY_MAP


# ----------------------------------------------------------
# Category Keywords
# ----------------------------------------------------------

KEYWORDS = {

    "maharashtra": MAHARASHTRA_KEYWORDS,

    "india": INDIA_KEYWORDS,

    "world": WORLD_KEYWORDS,

    "sports": SPORTS_KEYWORDS,

    "business": BUSINESS_KEYWORDS

}

# ----------------------------------------------------------
# Normalize Text
# ----------------------------------------------------------

def normalize(text):

    if not text:
        return ""

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    return text.strip()

# ----------------------------------------------------------
# Preprocess keywords (Done once when program starts)
# ----------------------------------------------------------

SINGLE_WORD_KEYWORDS = {}
PHRASE_KEYWORDS = {}

for category, keywords in KEYWORDS.items():

    single = set()
    phrases = set()

    for keyword in keywords:

        keyword = normalize(keyword)

        if " " in keyword:
            phrases.add(keyword)
        else:
            single.add(keyword)

    SINGLE_WORD_KEYWORDS[category] = frozenset(single)
    PHRASE_KEYWORDS[category] = frozenset(phrases)

def tokenize(text):
    """
    Convert text into a set of normalized words.
    """

    text = normalize(text)

    words = re.split(r"[^\w\u0900-\u097F]+", text)

 #   return set(filter(None, words))
    return {word for word in words if word}

# ----------------------------------------------------------
# Score Keywords
# ----------------------------------------------------------

# ----------------------------------------------------------
# Score All Categories
# ----------------------------------------------------------

def score_all_categories(text, words):

    scores = {}

    for category in CATEGORIES:

        score = 0

        # Count matching single-word keywords
        score += len(words & SINGLE_WORD_KEYWORDS[category])

        # Count matching phrases
        score += sum(
            phrase in text
            for phrase in PHRASE_KEYWORDS[category]
        )

        scores[category] = score

    return scores

# ----------------------------------------------------------
# Categorize One Article
# ----------------------------------------------------------

def categorize(news_item):

    # ======================================================
    # Priority 1
    # Feed Category
    # ======================================================
    if DEBUG:
        print("\nARTICLE")
        print(news_item.get("title"))

    source = news_item.get("source", {})

    feed_category = source.get("category")

    if feed_category in CATEGORIES:

        news_item["category_reason"] = "feed"

        if DEBUG:
            print("CATEGORY FROM FEED")

        return feed_category


    # ======================================================
    # Priority 2
    # URL Mapping
    # ======================================================

    url = news_item.get("url", "").lower()

    ## Normalize URL
    # Convert underscores to hyphens
    url = url.replace("_", "-")

    # Collapse multiple hyphens
    url = re.sub(r"-+", "-", url)

    # Remove duplicate slashes (except https://)
    url = re.sub(r"(?<!:)//+", "/", url)

    source_id = source.get("id", "").lower()

    if DEBUG:
        print("SOURCE ID =", source_id)

    publisher = None

    if source_id.startswith("esakal"):
        publisher = "esakal"

    elif source_id.startswith("loksatta"):
        publisher = "loksatta"

    elif source_id.startswith("lokmat"):
        publisher = "lokmat"

    elif source_id.startswith("maharashtratimes"):
        publisher = "maharashtratimes"

    if DEBUG:
        print("PUBLISHER =", publisher)

    if publisher:
        if DEBUG:
            print("Checking URL:", url)
        for pattern, category in URL_CATEGORY_MAP.get(publisher, {}).items():
            if DEBUG:
                print("Trying:", pattern)
            if pattern.lower() in url:
                if DEBUG:
                    print("Matched URL Pattern:", pattern)
                news_item["category_reason"] = "url"
                return category

    # ======================================================
    # Priority 3
    # Keyword Matching
    # ======================================================

    text = normalize(

        news_item.get("title", "") +

        " " +

        news_item.get("url", "")

    )

    words = tokenize(text)

    scores = score_all_categories(text, words)

    if DEBUG:
        for category in CATEGORIES:
            print(category, scores[category])

    # Find highest score

    best_category = None

    best_score = 0

    for category, score in scores.items():

        if score > best_score:

            best_score = score

            best_category = category

    # -------------------------------
    # DEBUG OUTPUT
    # -------------------------------

    if DEBUG:
        print("\n========================================")
        print(news_item.get("title"))
        print(news_item.get("url"))
        print("Scores :", scores)
        print("Best   :", best_category)
        print("Score  :", best_score)
        print("========================================")

    # Keyword matched

    if best_score > 0:

        news_item["category_reason"] = "keyword"
        if DEBUG:
            print("CATEGORY FROM KEYWORD")
        return best_category

    # Nothing matched

    news_item["category_reason"] = "default"

    return "india"

