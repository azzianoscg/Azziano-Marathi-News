"""
==========================================================
Azziano Marathi News
update_news.py

Main application

Workflow

1. Read configured sources
2. Download feeds
3. Parse feeds
4. Normalize data
5. Remove duplicates
6. Categorize
7. Sort by published date
8. Apply limits
9. Save news.json

Version : 2.0
==========================================================
"""
import time

from concurrent.futures import ThreadPoolExecutor, as_completed

from config import (
    CATEGORIES,
    NEWS_LIMITS
)

from news_sources import NEWS_SOURCES

from parser import (
    read_feed,
    normalize
)

from categorizer import categorize

from writer import (
    create_news_structure,
    save_json
)

from logger import (
    info,
    warning,
    error,
    start_session,
    end_session
)


# ----------------------------------------------------------
# Remove Duplicate URLs
# ----------------------------------------------------------

def remove_duplicates(news_list):

    unique = {}
    
    for item in news_list:

        url = item.get("url", "").strip()

        if not url:
            continue

        if url not in unique:
            unique[url] = item

    return list(unique.values())


# ----------------------------------------------------------
# Sort by Published Date
# ----------------------------------------------------------

def sort_news(news):

    return sorted(

        news,

        key=lambda x: x.get("published", ""),

        reverse=True

    )

# ----------------------------------------------------------
# Read one source
# ----------------------------------------------------------

    if not source.get("enabled", True):
        warning(f"Skipped : {source['name']}")
        return []

    info(f"Reading : {source['name']}")

    try:

        items = read_feed(source)

        items = normalize(items)

        info(f"{len(items)} articles")

        return items

    except Exception as ex:

        error(f"{source['name']} : {str(ex)}")

        return []

# ----------------------------------------------------------
# Main
# ----------------------------------------------------------

def main():

    start_session()

    start_time = time.perf_counter()

    try:

        info("Creating news structure")

        news_json = create_news_structure()

        all_news = []


        # -----------------------------------------
        # Read all configured sources
        # -----------------------------------------

        sources = sorted(
            NEWS_SOURCES,
            key=lambda x: x.get("priority", 999)
        )

        feed_start = time.perf_counter()

        with ThreadPoolExecutor(max_workers=4) as executor:

            futures = {
                executor.submit(read_feed, source): source
                for source in sources
                if source.get("enabled", True)
            }

            for future in as_completed(futures):

                source = futures[future]

                try:

                    info(f"Reading : {source['name']}")

                    items = future.result()

                    items = normalize(items)

                    info(f"{len(items)} articles")

                    all_news.extend(items)

                except Exception as ex:

                    error(f"{source['name']} : {str(ex)}")
        
        info(
                f"Feed download time : "
                f"{time.perf_counter() - feed_start:.2f} sec"
            )
        # -----------------------------------------
        # Remove Duplicates
        # -----------------------------------------

        info("Removing duplicates")

        all_news = remove_duplicates(all_news)

        info(
            f"Unique Articles : {len(all_news)}"
        )

        # -----------------------------------------
        # Categorize
        # -----------------------------------------

        info("Categorizing")

        cat_start = time.perf_counter()

        categorized = {
            category: []
            for category in CATEGORIES
        }

        for article in all_news:
            category = categorize(article)
            categorized[category].append(article)

        info(
            f"Categorization time : "
            f"{time.perf_counter() - cat_start:.2f} sec"
        )

        # -----------------------------------------
        # Sort + Limit
        # -----------------------------------------

        for category in CATEGORIES:

            articles = categorized.get(
                category,
                []
            )

            articles = sort_news(articles)

            limit = NEWS_LIMITS[category]

            news_json[category] = articles[:limit]

            info(

                f"{category} : "

                f"{len(news_json[category])}"

            )

        # -----------------------------------------
        # Save JSON
        # -----------------------------------------

        save_start = time.perf_counter()

        save_json(news_json)

        info(
            f"JSON write time : "
            f"{time.perf_counter() - save_start:.2f} sec"
        )

        info("news.json updated")

    except Exception as ex:

        error(str(ex))

    info(
        f"Total execution : "
        f"{time.perf_counter() - start_time:.2f} sec"
    )

    end_session()


# ----------------------------------------------------------
# Entry Point
# ----------------------------------------------------------

if __name__ == "__main__":

    main()