"""
==========================================================
Azziano Marathi News
url_category_map.py

Purpose
-------
URL patterns used for categorizing articles from
mixed RSS feeds and sitemaps.

Version : 4.0
==========================================================
"""

# ======================================================
# Common Maharashtra URL Patterns
# ======================================================

MAHARASHTRA_PATTERNS = [
    "ahilyanagar",
    "ahmednagar",
    "akola",
    "amravati",
    "beed",
    "bhandara",
    "buldhana",
    "chandrapur",
    "chhatrapati-sambhajinagar",
    "dharashiv",
    "dhule",
    "gadchiroli",
    "gondia",
    "hingoli",
    "jalgaon",
    "jalna",
    "kokan",
    "kolhapur",
    "konkan",
    "latur",
    "maharashtra",
    "maharashtra-news",
    "marathwada",
    "mumbai",
    "nagpur",
    "nanded",
    "nandurbar",
    "nashik",
    "navi-mumbai",
    "navimumbai",
    "osmanabad",
    "palghar",
    "parabhani",
    "parbhani",
    "pune",
    "raigad",
    "ratnagiri",
    "sambhajinagar",
    "sangli",
    "satara",
    "sindhudurg",
    "sindhudurga",
    "solapur",
    "thane",
    "vidarbha",
    "wardha",
    "washim",
    "yavatmal",
    "state",
    "bombay",
    "poona",
    "bombay-news",
    "mmr",
    "mumbai-metropolitan",
    "vidarbha-news",
    "marathwada-news",
    "konkan-news",
]

MAHARASHTRA_URLS = {

    f"/{p}/": "maharashtra"
        for p in MAHARASHTRA_PATTERNS

}

# ======================================================
# Common India URL Patterns
# ======================================================

INDIA_URLS = {

    "/india/": "india",
    "/india-news/": "india",
    "/national/": "india",
    "/nation/": "india",
    "/desh/": "india",
    "/bharat/": "india",
    "/breaking-news/": "india",
    "/entertainment/": "india",
    
    # States
    "/andhra-pradesh/": "india",
    "/arunachal-pradesh/": "india",
    "/assam/": "india",
    "/bihar/": "india",
    "/chhattisgarh/": "india",
    "/goa/": "india",
    "/gujarat/": "india",
    "/haryana/": "india",
    "/himachal-pradesh/": "india",
    "/jharkhand/": "india",
    "/karnataka/": "india",
    "/kerala/": "india",
    "/madhya-pradesh/": "india",
    "/manipur/": "india",
    "/meghalaya/": "india",
    "/mizoram/": "india",
    "/nagaland/": "india",
    "/odisha/": "india",
    "/orissa/": "india",          # Older spelling
    "/punjab/": "india",
    "/rajasthan/": "india",
    "/sikkim/": "india",
    "/tamil-nadu/": "india",
    "/telangana/": "india",
    "/tripura/": "india",
    "/uttar-pradesh/": "india",
    "/uttarakhand/": "india",
    "/uttaranchal/": "india",     # Older spelling
    "/west-bengal/": "india",

    "/ap/": "india",          # Andhra Pradesh
    "/up/": "india",          # Uttar Pradesh
    "/mp/": "india",          # Madhya Pradesh
    "/jk/": "india",          # Jammu & Kashmir

    # Union Territories
    "/andaman-nicobar/": "india",
    "/chandigarh/": "india",
    "/dadra-nagar-haveli/": "india",
    "/daman-diu/": "india",
    "/delhi/": "india",
    "/new-delhi/": "india",
    "/jammu-kashmir/": "india",
    "/ladakh/": "india",
    "/lakshadweep/": "india",
    "/puducherry/": "india",
    "/pondicherry/": "india",     # Older name

}

# ======================================================
# Common World URL Patterns
# ======================================================

WORLD_URLS = {

    "/world/": "world",
    "/world-news/": "world",
    "/international/": "world",
    "/global/": "world",
    "/abroad/": "world",

    # Countries
    "/usa/": "world",
    "/united-states/": "world",
    "/china/": "world",
    "/pakistan/": "world",
    "/bangladesh/": "world",
    "/nepal/": "world",
    "/ukraine/": "world",
    "/russia/": "world",
    "/israel/": "world",
    "/iran/": "world",
    "/france/": "world",
    "/germany/": "world",
    "/japan/": "world",
    "/uk/": "world",
    "/britain/": "world",
    "/england/": "world",

    "/canada/": "world",
    "/australia/": "world",
    "/new-zealand/": "world",
    "/uae/": "world",
    "/dubai/": "world",
    "/saudi-arabia/": "world",
    "/sri-lanka/": "world",
    "/afghanistan/": "world",
    "/myanmar/": "world",
    "/taiwan/": "world",
    "/north-korea/": "world",
    "/south-korea/": "world",

#UN
#NATO
#WHO
}

# ======================================================
# Common Sports URL Patterns
# ======================================================

SPORTS_URLS = {

    "/sports/": "sports",
    "/krida/": "sports",
    "/cricket/": "sports",
    "/football/": "sports",
    "/kabaddi/": "sports",
    "/tennis/": "sports",
    "/badminton/": "sports",
    "/hockey/": "sports",
    "/olympics/": "sports",
    "/ipl/": "sports",
    "/fifa/": "sports",
    "/world-cup/": "sports",
    "/sports-news/": "sports",

    "/chess/": "sports",
    "/athletics/": "sports",
    "/wimbledon/": "sports",
    "/formula-1/": "sports",
    "/f1/": "sports",
    "/nba/": "sports",
    "/icc/": "sports",

}

# ======================================================
# Common Business URL Patterns
# ======================================================

BUSINESS_URLS = {

    "/business/": "business",
    "/finance/": "business",
    "/money/": "business",
    "/economy/": "business",
    "/stock-market/": "business",
    "/share-market/": "business",
    "/arthvrutant/": "business",
    "/agriculture/": "business",
    "/farming/": "business",
    "/agro/": "business",
    "/auto/": "business",
    "/technology/": "business",
    "/tech/": "business",
    "/business-news/": "business",
#    "/market/": "business",

    "/startup/": "business",
    "/startups/": "business",
    "/startup-news/": "business",
    "/crypto/": "business",
    "/bitcoin/": "business",
    "/tax/": "business",
    "/income-tax/": "business",
    "/income-tax-return/": "business",
    "/itr/": "business",

}

COMMON_URLS = {
    **MAHARASHTRA_URLS,
    **INDIA_URLS,
    **WORLD_URLS,
    **SPORTS_URLS,
    **BUSINESS_URLS,
}

URL_CATEGORY_MAP = {

    # ======================================================
    # eSakal
    # ======================================================

    "esakal": {

        **COMMON_URLS,
        "/premier/": "india"

    },

    # ======================================================
    # Loksatta
    # ======================================================

    "loksatta": {

        **COMMON_URLS,

    },

    # ======================================================
    # Lokmat
    # ======================================================

    "lokmat": {

        **COMMON_URLS,
        "/bhakti/": "india",
        "/photos/bhakti/": "india",

    },

    # ======================================================
    # Maharashtra Times
    # ======================================================

    "maharashtratimes": {

        **COMMON_URLS,

        "/editorial/": "india",
        "/entertainment/": "india",
        "/education/": "india",
        "/health/": "india",
        "/lifestyle/": "india",
        "/technology/": "business",
        "/tech/": "business",
        "/auto/": "business",
        "/photos/": "india",
    }

}