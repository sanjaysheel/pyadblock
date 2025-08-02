import unittest
from pyadblock import is_ad_url, strip_ads_from_html, update_rules

class TestAdBlock(unittest.TestCase):
    def test_is_ad_url(self):
        self.assertTrue(is_ad_url("https://ads.yahoo.com/"))
        self.assertTrue(is_ad_url("https://track.adform.net/event"))
        self.assertFalse(is_ad_url("https://www.wikipedia.org/"))

    def test_strip_ads_from_html(self):
        html = '''
        <html><body>
        <div class="ad-banner">Ad Content</div>
        <div id="sponsored">Sponsored</div>
        <iframe src="https://ads.example.com/"></iframe>
        <div>Good Content</div>
        </body></html>'''
        cleaned = strip_ads_from_html(html)
        self.assertIn("Good Content", cleaned)
        self.assertNotIn("ad-banner", cleaned)
        self.assertNotIn("sponsored", cleaned)

    def test_update_rules(self):
        update_rules({"blockUrls": ["testad.com"]})
        self.assertTrue(is_ad_url("http://testad.com/banner"))

if __name__ == '__main__':
    unittest.main()