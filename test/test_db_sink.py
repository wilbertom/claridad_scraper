import os
from unittest import TestCase
import requests

from claridad_scraper import DBSink, Response
from test.support.responses import HTML_RESPONSE, PDF_RESPONSE, ERROR_RESPONSE, HTML_UTF_8_CONTENT, HTML_CONTENT


class TestDBSink(TestCase):

    def setUp(self):
        self.fs_dir = '/tmp/claridad_scraper_out'
        self.db_sink = DBSink(self.fs_dir)

    def tearDown(self):
        self.db_sink.destroy()

    def test_creating_a_db_sink_creates_the_base_db_directory(self):
        self.assertTrue(os.path.isdir(self.fs_dir))

    def test_it_can_retrieve_a_id_by_link(self):
        id = self.db_sink.save(PDF_RESPONSE)

        self.assertEquals(self.db_sink.id(PDF_RESPONSE.url), id)

    def test_it_returns_false_when_trying_to_get_a_id_for_a_unknown_link(self):
        link = 'http://example.com/example.pdf'
        self.assertIsNone(self.db_sink.id(link))

    def test_it_can_retrieve_a_saved_record_by_id(self):
        id = self.db_sink.save(PDF_RESPONSE)
        record = self.db_sink.get(id)

        self.assertIsNotNone(record)

    def test_a_saved_pdf_link_can_be_retrieved(self):
        id = self.db_sink.save(PDF_RESPONSE)
        record = self.db_sink.get(id)

        self.assertEquals(self.db_sink.link(record), PDF_RESPONSE.url)

    def test_a_saved_page_link_can_be_retrieved(self):
        id = self.db_sink.save(HTML_RESPONSE)
        record = self.db_sink.get(id)

        self.assertEquals(self.db_sink.link(record), HTML_RESPONSE.url)

    def test_a_saved_pdf_can_be_retrieved(self):
        id = self.db_sink.save(PDF_RESPONSE)
        record = self.db_sink.get(id)
        pdf = self.db_sink.content(record)

        self.assertEquals(pdf, PDF_RESPONSE.content)

    def test_a_saved_html_page_can_be_retrieved(self):
        id = self.db_sink.save(HTML_RESPONSE)
        record = self.db_sink.get(id)
        page = self.db_sink.content(record)

        self.assertEquals(page, HTML_RESPONSE.content)

    def test_a_saved_error_page_can_be_retrieved(self):
        id = self.db_sink.save(ERROR_RESPONSE)
        record = self.db_sink.get(id)
        page = self.db_sink.content(record)

        self.assertEquals(page, ERROR_RESPONSE.content)

    def test_we_know_when_a_page_has_errors(self):
        id = self.db_sink.save(ERROR_RESPONSE)
        record = self.db_sink.get(id)

        self.assertTrue(self.db_sink.has_errors(record))

    def test_we_know_when_a_page_doesnt_have_errors(self):
        id = self.db_sink.save(HTML_RESPONSE)
        record = self.db_sink.get(id)

        self.assertFalse(self.db_sink.has_errors(record))

    def test_it_knows_when_it_saved_a_pdf(self):
        id = self.db_sink.save(PDF_RESPONSE)
        record = self.db_sink.get(id)

        self.assertEquals(self.db_sink.content_type(record), 'application/pdf')

    def test_it_knows_when_it_saved_a_html_page(self):
        id = self.db_sink.save(HTML_RESPONSE)
        record = self.db_sink.get(id)

        self.assertEquals(self.db_sink.content_type(record), 'text/html')

    def test_it_cant_save_requests_responses(self):
        response = requests.get('http://example.com')

        with self.assertRaises(ValueError):
            self.db_sink.save(response)

    def test_it_saves_the_http_headers(self):
        id = self.db_sink.save(HTML_RESPONSE)
        record = self.db_sink.get(id)

        self.assertEquals(self.db_sink.headers(record), HTML_RESPONSE.headers)

    def test_it_lower_cases_all_http_header_names(self):
        response = Response(
            'http://example.com',
            HTML_RESPONSE.content,
            headers={
                'Content-Type': 'text/html; charset=utf-8',
            }
        )

        id = self.db_sink.save(response)
        record = self.db_sink.get(id)

        self.assertEquals(self.db_sink.headers(record), {'content-type': 'text/html; charset=utf-8'})

    def test_it_saves_the_http_status_code(self):
        id = self.db_sink.save(HTML_RESPONSE)
        record = self.db_sink.get(id)

        self.assertEquals(self.db_sink.status_code(record), HTML_RESPONSE.status_code)

    def test_it_saves_the_encoding(self):
        response = Response(
            'http://example.com', HTML_UTF_8_CONTENT, headers={'content-type': 'text/html; charset=utf-8'}
        )
        response.guess_content_encoding()

        id = self.db_sink.save(response)
        record = self.db_sink.get(id)

        self.assertEquals(self.db_sink.encoding(record), 'utf-8')
        self.assertEquals(self.db_sink.encoding(record), response.encoding)

    def test_it_saves_the_text_for_html_responses(self):
        response = Response(
            'http://example.com', HTML_UTF_8_CONTENT, headers={'content-type': 'text/html; charset=utf-8'}
        )
        response.guess_content_encoding()
        id = self.db_sink.save(response)
        record = self.db_sink.get(id)

        self.assertIsNotNone(self.db_sink.text(record))
        self.assertEquals(self.db_sink.text(record), response.utf_8_text)

    def test_it_saves_none_text_for_html_responses_without_encoding(self):
        response = Response(
            'http://example.com', HTML_CONTENT, headers={'content-type': 'text/html; charset=utf-8'}
        )
        response.guess_content_encoding()
        id = self.db_sink.save(response)
        record = self.db_sink.get(id)

        self.assertIsNone(self.db_sink.text(record))
