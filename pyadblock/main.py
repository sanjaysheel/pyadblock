import os
from core.engine import AdBlockEngine

if __name__ == "__main__":
    test_urls = [
        "https://ads.google.com/banner?id=123",
        "https://partner.googleadservices.com/ad",
        "https://example.com/content",
        "http://doubleclick.net/tracker",
        "https://www.wikipedia.org/"
    ]

    current_dir = os.path.dirname(os.path.abspath(__file__))
    rule_file_path = os.path.join(current_dir, "../rules/baseline.udr")

    if not os.path.exists(rule_file_path):
        raise FileNotFoundError(f"Rule file not found at: {rule_file_path}")

    engine = AdBlockEngine(rule_file_path)

    print("\n=== Veilblock Ad Test ===")
    for url in test_urls:
        result = engine.check_url(url)
        print(f"{url} -> {'BLOCKED' if result else 'ALLOWED'}")
