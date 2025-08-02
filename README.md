# pyadblock




📦 pyadblock/
├── main.py                  ▶ Entry point for CLI/test
├── core.py                  ▶ Main logic: match URLs, clean HTML
├── engine/
│   ├── rule_matcher.py      ▶ Efficient matcher for URLs/selectors
│   ├── html_cleaner.py      ▶ DOM cleaner using BeautifulSoup
│   └── telemetry.py         ▶ (Optional) logs unknown ads for future rule training
├── data/
│   ├── rules.json           ▶ URL rules (ads, trackers, scripts)
│   ├── selectors.json       ▶ CSS/DOM cosmetic filters
│   └── known_entities.json  ▶ (Optional) ownership/categorization
├── utils/
│   ├── fetcher.py           ▶ (Optional) fetch page source (requests or Selenium)
│   └── crawler.py           ▶ Smart crawler to discover ad patterns (optional)
├── generator/
│   └── auto_rule_builder.py ▶ Learns new rules from crawled data
├── tests/
│   └── test_core.py         ▶ Unit tests
└── README.md
