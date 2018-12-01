from unittest import TestCase
from claridad_scraper import Parser
from bs4 import BeautifulSoup

from test.support.responses import HTML_RESPONSE, PDF_RESPONSE, ANOTHER_RESPONSE, JPG_RESPONSE, GIF_RESPONSE


class TestParser(TestCase):

    def setUp(self):
        self.parser = Parser('http://example.com')

    def test_parsing_a_html_response_returns_a_soup(self):
        self.assertIsInstance(self.parser.parse(HTML_RESPONSE), BeautifulSoup)

    def test_parsing_a_pdf_response_returns_the_pdf(self):
        self.assertEquals(self.parser.parse(PDF_RESPONSE), PDF_RESPONSE.content)

    def test_parsing_a_jpg_response_returns_the_jpg(self):
        self.assertEquals(self.parser.parse(JPG_RESPONSE), JPG_RESPONSE.content)

    def test_parsing_a_gif_response_returns_the_gif(self):
        self.assertEquals(self.parser.parse(GIF_RESPONSE), GIF_RESPONSE.content)

    def test_parsing_any_other_content_type_is_ignored_and_returns_none(self):
        self.assertEquals(self.parser.parse(ANOTHER_RESPONSE), None)

    def test_links_removes_all_javascript_links(self):
        links = self.parser.links(self.parser.parse(HTML_RESPONSE))

        self.assertNotIn('javascript:SomeForm(1);', links)

    def test_links_removes_all_mailto_links(self):
        links = self.parser.links(self.parser.parse(HTML_RESPONSE))

        self.assertNotIn('mailto:person@example.com', links)

    def test_links_removes_all_none_links(self):
        links = self.parser.links(self.parser.parse(HTML_RESPONSE))
        self.assertNotIn(None, links)

    def test_links_removes_all_links_to_external_websites(self):
        links = self.parser.links(self.parser.parse(HTML_RESPONSE))

        self.assertNotIn('http://anotherwebsite.com/', links)

    def test_links_expands_all_links(self):
        links = self.parser.links(self.parser.parse(HTML_RESPONSE))

        for link in links:
            self.assertFalse(self.parser.link_helpers.is_relative(link), 'Link is relative: {}'.format(link))

    def test_links_removes_all_duplicates(self):
        links = self.parser.links(self.parser.parse(HTML_RESPONSE))

        self.assertEquals(links.count('http://example.com/'), 1)

    def test_links_accounts_for_duplicate_expanded_links(self):
        links = self.parser.links(self.parser.parse(HTML_RESPONSE))

        self.assertEquals(links.count('http://example.com/section.html'), 1)

    def test_no_links_are_found_in_pdf_documents(self):
        links = self.parser.links(self.parser.parse(PDF_RESPONSE))

        self.assertEquals(links, [])
