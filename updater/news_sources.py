"""
==========================================================
Azziano Marathi News
news_sources.py

Purpose:
    Defines all News Sitemap sources.

Version : 4.0
==========================================================
"""

# ----------------------------------------------------------
# Source Types
# ----------------------------------------------------------

SITEMAP = "sitemap"

# ----------------------------------------------------------
# News Sources
# esakal url https://www.esakal.com/news_sitemap.xml
# lokmat url https://www.lokmat.com/sitemap.xml
# loksatta url https://www.loksatta.com/news-sitemap.xml
# Maharashtra Times url https://maharashtratimes.com/staticsitemap/mt/news/sitemap-48hours.xml
# ----------------------------------------------------------

NEWS_SOURCES = [

    # ======================================================
    # eSakal
    # ======================================================

    {
        "id": "esakal",
        "name": "eSakal",
        "website": "https://www.esakal.com",
        "type": SITEMAP,
        "url": "https://www.esakal.com/news_sitemap.xml",
        "priority": 1,
        "max_articles": 200,
        "enabled": True
    },

    # ======================================================
    # Lokmat
    # ======================================================

    {
        "id": "lokmat",
        "name": "Lokmat",
        "website": "https://www.lokmat.com",
        "type": SITEMAP,
        "url": "https://www.lokmat.com/sitemap.xml",
        "priority": 2,
        "max_articles": 50,
        "enabled": True
    },

    # ======================================================
    # Loksatta
    # ======================================================

    {
        "id": "loksatta",
        "name": "Loksatta",
        "website": "https://www.loksatta.com",
        "type": SITEMAP,
        "url": "https://www.loksatta.com/news-sitemap.xml",
        "priority": 3,
        "max_articles": 100,
        "enabled": True
    },

    # ======================================================
    # Maharashtra Times
    # ======================================================

    {
        "id": "maharashtratimes",
        "name": "Maharashtra Times",
        "website": "https://maharashtratimes.com",
        "type": SITEMAP,
        "url": "https://maharashtratimes.com/staticsitemap/mt/news/sitemap-48hours.xml",
        "priority": 4,
        "max_articles": 100,
        "enabled": True
    }

]