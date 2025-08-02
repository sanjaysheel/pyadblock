import os
from core.engine import AdBlockEngine

if __name__ == "__main__":
    # Dynamically resolve path
    rule_file_path = os.path.join(os.path.dirname(__file__), "./rules/baseline.udr")
    
    if not os.path.exists(rule_file_path):
        raise FileNotFoundError(f"Rule file not found at: {rule_file_path}")

    engine = AdBlockEngine(rule_file_path)

    test_urls = [
        "https://ads.google.com/banner?id=123",
        "https://partner.googleadservices.com/ad",
        "https://example.com/content",
        "http://doubleclick.net/tracker",
        "https://www.wikipedia.org/"
    ]

    print("\n=== Veilblock Ad Test ===")

    for url in test_urls:
        result = engine.check_url(url)
        print(f"{url} -> {'BLOCKED' if result else 'ALLOWED'}")

