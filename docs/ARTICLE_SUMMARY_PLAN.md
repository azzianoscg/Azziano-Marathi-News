# Azziano Marathi News - Article Summary Plan

## Target Version
v1.1.0

## Objective

Display news summaries inside Azziano Marathi News instead of sending users directly to newspaper websites.

## Current Flow

RSS Feed
↓
news.json
↓
index.html
↓
External newspaper article


## New Flow

RSS Feed
↓
News Parser
↓
Article Processor
↓
article.json
↓
article.html
↓
Senior-friendly reading view


## Requirements

- Keep existing v1.0.0 functionality
- Do not break news.json
- Keep external article link as fallback
- Mobile-friendly design
- Simple reading experience


## Testing Sources

- Lokmat
- Loksatta
- Maharashtra Times
- eSakal