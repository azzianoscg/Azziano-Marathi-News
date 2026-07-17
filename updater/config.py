"""
==========================================================
Azziano Marathi News
config.py

Purpose:
    Central configuration for the project.

Version : 2.0
==========================================================
"""
from pathlib import Path

PROJECT_NAME="Azziano Marathi News"
PROJECT_VERSION="2.0"
GENERATED_BY="Azziano Marathi News Engine"
LANGUAGE="mr"
COUNTRY="India"

BASE_DIR = Path(__file__).resolve().parent.parent
UPDATER_DIR = BASE_DIR / "updater"
LOG_DIR = BASE_DIR / "logs"
NEWS_JSON = BASE_DIR / "news.json"

REQUEST_TIMEOUT=20
USER_AGENT="Azziano-Marathi-News/2.0 (Python Requests)"

NEWS_LIMITS={
    "maharashtra":5,
    "india":5,
    "world":5,
    "sports":3,
    "business":3
}

REFRESH_INTERVAL_MINUTES=60
LOG_FILE=LOG_DIR/"update.log"

RSS="rss"
SITEMAP="sitemap"

CATEGORIES=[
    "maharashtra",
    "india",
    "world",
    "sports",
    "business"
]

CATEGORY_TITLES={
    "maharashtra":"महाराष्ट्र",
    "india":"भारत",
    "world":"जग",
    "sports":"क्रीडा",
    "business":"व्यवसाय"
}

DEFAULT_IMAGE=""
DEFAULT_BREAKING=False

FEED_CATEGORY_MAP={
    "lokmat_maharashtra":"maharashtra",
    "lokmat_india":"india",
    "lokmat_world":"world",
    "lokmat_sports":"sports",
    "lokmat_business":"business",
}

URL_CATEGORY_MAP={
    "/maharashtra/":"maharashtra",
    "/mumbai/":"maharashtra",
    "/pune/":"maharashtra",
    "/thane/":"maharashtra",
    "/nashik/":"maharashtra",
    "/nagpur/":"maharashtra",
    "/vidarbha/":"maharashtra",
    "/marathwada/":"maharashtra",
    "/kokan/":"maharashtra",
    "/konkan/":"maharashtra",
    "/national/":"india",
    "/india/":"india",
    "/premier/":"india",
    "/world/":"world",
    "/international/":"world",
    "/global/":"world",
    "/sports/":"sports",
    "/cricket/":"sports",
    "/football/":"sports",
    "/business/":"business",
    "/finance/":"business",
    "/economy/":"business",
    "/money/":"business",
}
