"""
==========================================================
Azziano Marathi News
writer.py

Purpose:
    Writes news data to news.json

Version : 1.0
==========================================================
"""

import json
from datetime import datetime, timezone, timedelta
from config import NEWS_JSON

# ----------------------------------------------------------
# Create Empty News Structure
# ----------------------------------------------------------

def create_news_structure():

    return {

        "lastUpdated": "",

        "maharashtra": [],

        "india": [],

        "world": [],

        "sports": [],

        "business": []

    }


# ----------------------------------------------------------
# Update Timestamp
# ----------------------------------------------------------

def update_timestamp(news_data):

    ist = timezone(timedelta(hours=5, minutes=30))

    news_data["lastUpdated"] = (
        datetime.now(ist).strftime("%d-%m-%Y | %I:%M %p") + " IST"
        )


# ----------------------------------------------------------
# Save JSON File
# ----------------------------------------------------------

def save_json(news_data, filename=NEWS_JSON):

    try:

        update_timestamp(news_data)

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(

                news_data,

                file,

                ensure_ascii=False,

                indent=4

            )

        print()

        print("✓ news.json generated successfully")

        print(filename)

        return True

    except Exception as ex:

        print()

        print("Error writing news.json")

        print(ex)

        return False