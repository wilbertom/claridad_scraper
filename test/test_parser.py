from unittest import TestCase
from claridad_scraper import Parser
from bs4 import BeautifulSoup

from test.support.responses import HTML_RESPONSE, PDF_RESPONSE, ANOTHER_RESPONSE, JPG_RESPONSE, GIF_RESPONSE


class TestParser(TestCase):

    def setUp(self):
        self.parser = Parser('http://example.com')

    def test_links_from_a_pdf_response_raises_an_error_because_we_dont_want_to_scrape_them(self):
        self.assertRaises(ValueError, self.parser.links, PDF_RESPONSE)

    def test_links_removes_all_javascript_links(self):
        links = self.parser.links(HTML_RESPONSE)

        self.assertNotIn('javascript:SomeForm(1);', links)

    def test_links_removes_all_mailto_links(self):
        links = self.parser.links(HTML_RESPONSE)

        self.assertNotIn('mailto:person@example.com', links)

    def test_links_removes_all_none_links(self):
        links = self.parser.links(HTML_RESPONSE)
        self.assertNotIn(None, links)

    def test_links_removes_all_links_to_external_websites(self):
        links = self.parser.links(HTML_RESPONSE)

        self.assertNotIn('http://anotherwebsite.com/', links)

    def test_links_expands_all_links(self):
        links = self.parser.links(HTML_RESPONSE)

        for link in links:
            self.assertFalse(self.parser.link_helpers.is_relative(link), 'Link is relative: {}'.format(link))

    def test_links_removes_all_duplicates(self):
        links = self.parser.links(HTML_RESPONSE)

        self.assertEquals(links.count('http://example.com/'), 1)

    def test_links_accounts_for_duplicate_expanded_links(self):
        links = self.parser.links(HTML_RESPONSE)

        self.assertEquals(links.count('http://example.com/section.html'), 1)
