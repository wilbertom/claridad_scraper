from unittest import TestCase
from claridad_scraper import Parser, Response

from test.support.responses import HTML_RESPONSE, PDF_RESPONSE, HTML_ISO_8859_1_CONTENT


class TestParser(TestCase):

    def setUp(self):
        self.parser = Parser('http://example.com')
        self.html_response = Response(
            'http://example.com', HTML_ISO_8859_1_CONTENT, headers={'content-type': 'text/html; charset=utf-8'}
        )
        self.html_response.guess_content_encoding()

    def test_links_from_a_pdf_response_raises_an_error_because_we_dont_want_to_scrape_them(self):
        self.assertRaises(ValueError, self.parser.links, PDF_RESPONSE)

    def test_links_removes_all_javascript_links(self):
        links = self.parser.links(self.html_response)

        self.assertNotIn('javascript:SomeForm(1);', links)

    def test_links_removes_all_mailto_links(self):
        links = self.parser.links(self.html_response)

        self.assertNotIn('mailto:person@example.com', links)

    def test_links_removes_all_none_links(self):
        links = self.parser.links(self.html_response)
        self.assertNotIn(None, links)

    def test_links_removes_all_links_to_external_websites(self):
        links = self.parser.links(self.html_response)

        self.assertNotIn('http://anotherwebsite.com/', links)

    def test_links_expands_all_links(self):
        links = self.parser.links(self.html_response)

        for link in links:
            self.assertFalse(self.parser.link_helpers.is_relative(link), 'Link is relative: {}'.format(link))

    def test_links_removes_all_duplicates(self):
        links = self.parser.links(self.html_response)

        self.assertEquals(links.count('http://example.com/'), 1)

    def test_links_accounts_for_duplicate_expanded_links(self):
        links = self.parser.links(self.html_response)

        self.assertEquals(links.count('http://example.com/section.html'), 1)

    def test_links_are_correctly_encoded(self):
        links = self.parser.links(self.html_response)

        self.assertIn(
            'http://example.com/images/articles/Imagen_Títeres,-sin-querer-queriendo-w_xlg.jpg',
            links
        )
