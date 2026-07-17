"""
==========================================================
Azziano Marathi News
date_utils.py

Purpose:
    Convert various RSS and Sitemap date formats
    into a standard ISO-8601 format.

Output Format

YYYY-MM-DDTHH:MM:SS

Example

2026-07-13T09:15:00

Version : 1.0
==========================================================
"""

from datetime import datetime
from email.utils import parsedate_to_datetime


# ----------------------------------------------------------
# Convert Date
# ----------------------------------------------------------

def normalize_date(date_string):
    """
    Converts various date formats into
    YYYY-MM-DDTHH:MM:SS

    Returns empty string if conversion fails.
    """

    if not date_string:
        return ""

    date_string = date_string.strip()

    # ------------------------------------------------------
    # RSS Date
    # Example:
    # Mon, 13 Jul 2026 09:15:00 +0530
    # ------------------------------------------------------

    try:

        dt = parsedate_to_datetime(date_string)

        return dt.strftime("%Y-%m-%dT%H:%M:%S")

    except Exception:
        pass

    # ------------------------------------------------------
    # ISO Format
    # Example:
    # 2026-07-13T09:15:00+05:30
    # ------------------------------------------------------

    try:

        dt = datetime.fromisoformat(
            date_string.replace("Z", "+00:00")
        )

        return dt.strftime("%Y-%m-%dT%H:%M:%S")

    except Exception:
        pass

    # ------------------------------------------------------
    # YYYY-MM-DD HH:MM:SS
    # ------------------------------------------------------

    try:

        dt = datetime.strptime(
            date_string,
            "%Y-%m-%d %H:%M:%S"
        )

        return dt.strftime("%Y-%m-%dT%H:%M:%S")

    except Exception:
        pass

    # ------------------------------------------------------
    # YYYY-MM-DD
    # ------------------------------------------------------

    try:

        dt = datetime.strptime(
            date_string,
            "%Y-%m-%d"
        )

        return dt.strftime("%Y-%m-%dT00:00:00")

    except Exception:
        pass

    # Unknown format

    return ""


# ----------------------------------------------------------
# Compare Dates
# ----------------------------------------------------------

def sort_key(article):
    """
    Returns sortable date string.
    """

    return article.get("published", "")


# ----------------------------------------------------------
# Test
# ----------------------------------------------------------

if __name__ == "__main__":

    tests = [

        "Mon, 13 Jul 2026 09:15:00 +0530",

        "2026-07-13T09:15:00+05:30",

        "2026-07-13T09:15:00Z",

        "2026-07-13 09:15:00",

        "2026-07-13"

    ]

    for value in tests:

        print(value)

        print(normalize_date(value))

        print("-" * 40)