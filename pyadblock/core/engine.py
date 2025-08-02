# veilblock/core/engine.py
from core.loader import RuleLoader
from core.dispatcher import PluginDispatcher
from core.context import RequestContext

class AdBlockEngine:
    def __init__(self, rule_file_path):
        self.rules = RuleLoader.load_rules(rule_file_path)
        self.dispatcher = PluginDispatcher(self.rules)

    def check_url(self, url):
        context = RequestContext(url=url, headers={}, content_type="text/html")
        return self.dispatcher.run_url_plugins(context)

    def clean_html(self, html):
        return self.dispatcher.run_html_plugins(html)

    def filter_js(self, script):
        return self.dispatcher.run_js_plugins(script)
