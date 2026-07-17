"""
==========================================================
Azziano Marathi News
parser.py

Purpose
-------
Universal parser for:

✓ RSS Feeds
✓ Google News Sitemaps
✓ Standard XML Sitemaps
✓ Sitemap Indexes

Version : 4.0
==========================================================
"""

import hashlib
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

from config import (
    REQUEST_TIMEOUT,
    USER_AGENT,
    RSS,
    SITEMAP,
    DEFAULT_IMAGE,
    DEFAULT_BREAKING
)

from logger import info, warning, error
from date_utils import normalize_date


# ---------------------------------------------------------
# Generate Unique News ID
# ---------------------------------------------------------

def generate_news_id(url):

    if not url:
        return ""

    return hashlib.sha1(
        url.encode("utf-8")
    ).hexdigest()[:12]


# ---------------------------------------------------------
# Download XML
# ---------------------------------------------------------

def download_xml(url):

    try:

        response = requests.get(

            url,

            timeout=REQUEST_TIMEOUT,

            headers={
                "User-Agent": USER_AGENT
            }

        )

        response.raise_for_status()

        response.encoding = "utf-8"

        return response.text

    except Exception as ex:

        error(f"Download failed : {url}")

        error(str(ex))

        return None


# ---------------------------------------------------------
# Download HTML Page
# (used for normal sitemaps)
# ---------------------------------------------------------

def download_html(url):

    try:

        response = requests.get(

            url,

            timeout=REQUEST_TIMEOUT,

            headers={
                "User-Agent": USER_AGENT
            }

        )

        response.raise_for_status()

        response.encoding = "utf-8"

        return response.text

    except Exception:

        return None


# ---------------------------------------------------------
# Extract HTML Title
# ---------------------------------------------------------

def extract_title(html):

    try:

        start = html.find("<title>")

        end = html.find("</title>")

        if start == -1 or end == -1:
            return ""

        title = html[start + 7:end]

        return " ".join(title.split())

    except Exception:

        return ""


# ---------------------------------------------------------
# Extract OpenGraph Image
# ---------------------------------------------------------

def extract_image(html):

    try:

        marker = 'property="og:image"'

        pos = html.find(marker)

        if pos == -1:
            return DEFAULT_IMAGE

        content = html.find('content="', pos)

        if content == -1:
            return DEFAULT_IMAGE

        content += 9

        end = html.find('"', content)

        return html[content:end]

    except Exception:

        return DEFAULT_IMAGE

def detect_category_from_url(url):
    """
    Detect category from article URL.
    """

    if not url:
        return None

    url = url.lower()

    rules = {

        "business": [
            "/business/",
            "/share-market/",
            "/stock-market/",
            "/economy/",
            "/finance/"
        ],

        "sports": [
            "/sports/",
            "/cricket/",
            "/football/",
            "/tennis/",
            "/ipl/"
        ],

        "world": [
            "/world/",
            "/international/"
        ],

        "india": [
            "/national/",
            "/india/"
        ],

        "maharashtra": [
            "/maharashtra/",
            "/mumbai/",
            "/pune/",
            "/nagpur/",
            "/thane/",
            "/nashik/",
            "/kolhapur/",
            "/satara/",
            "/ahilyanagar/",
            "/chhatrapati-sambhajinagar/"
        ]

    }

    for category, keywords in rules.items():

        for keyword in keywords:

            if keyword in url:
                return category

    return None
# ---------------------------------------------------------
# Parse RSS Feed
# ---------------------------------------------------------

def parse_rss(xml_text, source):

    articles = []

    try:

        root = ET.fromstring(xml_text)

        channel = root.find("channel")

        if channel is None:

            warning(f"{source['name']} : channel not found")

            return articles

        namespace = {
            "media": "http://search.yahoo.com/mrss/"
        }

        for item in channel.findall("item"):

            title = item.findtext(
                "title",
                ""
            ).strip()

            url = item.findtext(
                "link",
                ""
            ).strip()

            published = normalize_date(
                item.findtext(
                    "pubDate",
                    ""
                )
            )

            image = DEFAULT_IMAGE

            media = item.find(
                "media:content",
                namespace
            )

            if media is not None:

                image = media.attrib.get(
                    "url",
                    DEFAULT_IMAGE
                )

            enclosure = item.find("enclosure")

            if enclosure is not None:

                image = enclosure.attrib.get(
                    "url",
                    image
                )

            if not title:
                continue

            if not url:
                continue

            article = {

                "id": generate_news_id(url),

                "feed": source["id"],

                "title": title,

                "source": {

                    "id": source["id"],

                    "name": source["name"],

                    "website": source["website"],

                    "category": source.get("category")

                },

                "published": published,

                "url": url,

                "image": image,

                "isBreaking": DEFAULT_BREAKING

            }

            articles.append(article)

    except Exception as ex:

        error(f"{source['name']} RSS parsing failed")

        error(str(ex))

    info(f"{source['name']} RSS : {len(articles)} articles")

    return articles

# ---------------------------------------------------------
# Universal Sitemap Parser
# ---------------------------------------------------------

# ---------------------------------------------------------
# Universal Sitemap Parser (Version 5)
# ---------------------------------------------------------

def parse_sitemap(xml_text, source):

    articles = []

    ns = {
        "sm": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "news": "http://www.google.com/schemas/sitemap-news/0.9",
        "image": "http://www.google.com/schemas/sitemap-image/1.1"
    }

    try:

        root = ET.fromstring(xml_text)

        urls = root.findall("sm:url", ns)

        # Limit number of sitemap URLs to process
        max_articles = source.get("max_articles", 50)

        urls = urls[:max_articles]

        info(f"{source['name']} : Processing {len(urls)} latest urls")

        for node in urls:

            # -----------------------------------
            # URL
            # -----------------------------------

            url = node.findtext(
                "sm:loc",
                "",
                ns
            ).strip()

            if not url:
                continue

            # -----------------------------------
            # Published Date
            # -----------------------------------

            published = node.findtext(
                "news:news/news:publication_date",
                "",
                ns
            ).strip()

            if not published:

                published = node.findtext(
                    "sm:lastmod",
                    "",
                    ns
                ).strip()

            published = normalize_date(published)

            # -----------------------------------
            # Image from Sitemap
            # -----------------------------------

            image = DEFAULT_IMAGE

            image_node = node.find(
                "image:image/image:loc",
                ns
            )

            if image_node is not None and image_node.text:

                image = image_node.text.strip()

            # -----------------------------------
            # Google News Title
            # -----------------------------------

            title = node.findtext(
                "news:news/news:title",
                "",
                ns
            ).strip()

            # -----------------------------------
            # Standard Sitemap
            # Fetch page only when title missing
            # -----------------------------------

            if not title:

                html = download_html(url)

                if html:

                    soup = BeautifulSoup(
                        html,
                        "html.parser"
                    )

                    # OpenGraph title

                    og = soup.find(
                        "meta",
                        property="og:title"
                    )

                    if og and og.get("content"):

                        title = og["content"].strip()

                    elif soup.title:

                        title = soup.title.text.strip()

                    # Remove site suffix

                    if "|" in title:
                        title = title.split("|")[0].strip()

                    if "Latest" in title:
                        title = title.split("|")[0].strip()

                    # OpenGraph image

                    if image == DEFAULT_IMAGE:

                        og_img = soup.find(
                            "meta",
                            property="og:image"
                        )

                        if og_img and og_img.get("content"):

                            image = og_img["content"].strip()

            if not title:
                continue

            article = {

                "id": generate_news_id(url),

                "feed": source["id"],

                "title": title,

                "source": {

                    "id": source["id"],
                    "name": source["name"],
                    "website": source["website"],
                    "category": detect_category_from_url(url)
                                or source.get("category")

                },

                "published": published,

                "url": url,

                "image": image,

                "isBreaking": DEFAULT_BREAKING

            }

            articles.append(article)

    except Exception as ex:

        error(f"{source['name']} Sitemap parsing failed.")

        error(str(ex))

    info(f"{source['name']} Sitemap : {len(articles)} articles")

    return articles

# ---------------------------------------------------------
# Read Feed
# ---------------------------------------------------------

def read_feed(source):

    info(f"Reading {source['name']}")

    xml = download_xml(source["url"])

    if xml is None:

        return []

    if source["type"] == RSS:

        return parse_rss(
            xml,
            source
        )

    if source["type"] == SITEMAP:

        return parse_sitemap(
            xml,
            source
        )

    warning(
        f"Unknown feed type : {source['type']}"
    )

    return []


# ---------------------------------------------------------
# Remove Duplicate Articles
# ---------------------------------------------------------

def normalize(news_list):

    normalized = []

    ids = set()

    urls = set()

    for article in news_list:

        if not article.get("title"):
            continue

        if not article.get("url"):
            continue

        if not article.get("id"):
            continue

        if article["id"] in ids:
            continue

        if article["url"] in urls:
            continue

        ids.add(article["id"])

        urls.add(article["url"])

        normalized.append(article)

    info(f"Unique Articles : {len(normalized)}")

    return normalized
	