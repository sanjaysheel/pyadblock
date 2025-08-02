import json
import os
from bs4 import BeautifulSoup
from .pyadblock.utils import url_matches_pattern

# Load rules from JSON
RULES_PATH = os.path.join(os.path.dirname(__file__), 'rules.json')
with open(RULES_PATH, 'r') as f:
    RULES = json.load(f)

def is_ad_url(url: str) -> bool:
    return any(url_matches_pattern(url, pattern) for pattern in RULES["blockUrls"])

def strip_ads_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    for selector in RULES["hideSelectors"]:
        for element in soup.select(selector):
            element.decompose()
    return str(soup)

def update_rules(new_rules: dict):
    global RULES
    RULES["blockUrls"] = new_rules.get("blockUrls", RULES["blockUrls"])
    RULES["hideSelectors"] = new_rules.get("hideSelectors", RULES["hideSelectors"])
