from pyadblock import is_ad_url, strip_ads_from_html, update_rules

# Sample URLs to test
test_urls = [
    "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js",
    "https://securepubads.g.doubleclick.net/tag/js/gpt.js",
    "https://ads.yahoo.com/",
    "https://www.wikipedia.org/",
    "https://track.adform.net/",
    "https://news.ycombinator.com/"
]

# Sample HTML to clean
html_input = """
<html>
  <head>
    <script src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  </head>
  <body>
    <div class="ad-banner">Ad Content Here</div>
    <div id="sponsored">Sponsored section</div>
    <iframe src="https://ads.amazon-adsystem.com/adframe"></iframe>
    <div>Actual content stays here</div>
  </body>
</html>
"""

def run_demo():
    print("=== URL Ad Check ===")
    for url in test_urls:
        print(f"{url} -> {'BLOCKED' if is_ad_url(url) else 'ALLOWED'}")

    print("\n=== HTML Cleaning ===")
    cleaned_html = strip_ads_from_html(html_input)
    print(cleaned_html)

if __name__ == "__main__":
    run_demo()
