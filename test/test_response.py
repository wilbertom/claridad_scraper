from unittest import TestCase
import requests

from claridad_scraper import Response, DBSink
from test.support.responses import HTML_UTF_8_CONTENT, HTML_ASCII_CONTENT, HTML_ISO_8859_1_CONTENT, HTML_CONTENT


class TestResponse(TestCase):
    def setUp(self):
        self.sink = DBSink('/tmp/example_database_sink')

    def tearDown(self):
        self.sink.destroy()

    def test_from_requests_response(self):
        requests_response = requests.get('http://example.com')
        response = Response.from_requests_response(requests_response)
        response.guess_content_encoding()

        self.assertEquals(response.url, requests_response.url)
        self.assertEquals(response.content, requests_response.content)
        self.assertEquals(response.status_code, requests_response.status_code)
        self.assertEquals(response.headers, requests_response.headers)
        self.assertEquals(response.encoding, requests_response.encoding)

    def test_from_db_record_when_saved_with_our_response_wrapper(self):
        link = 'http://example.com'
        requests_response = requests.get(link)
        response = Response.from_requests_response(requests_response)
        response.guess_content_encoding()
        self.sink.save(response)
        record_id = self.sink.id(response.url)
        record = self.sink.get(record_id)

        response = Response.from_sink_record(self.sink, record)

        self.assertEquals(response.url, requests_response.url)
        self.assertEquals(response.content, requests_response.content)
        self.assertEquals(response.status_code, requests_response.status_code)
        self.assertEquals(response.headers, requests_response.headers)
        self.assertEquals(response.encoding, requests_response.encoding)

    def test_from_db_record_when_saved_directly_from_a_requests_response(self):
        self.skipTest('We are deciding to only allow our response wrapper')
        link = 'http://example.com'
        requests_response = requests.get(link)
        self.sink.save(requests_response)
        record_id = self.sink.id(requests_response.url)
        record = self.sink.get(record_id)

        response = Response.from_sink_record(self.sink, record)

        self.assertEquals(response.url, requests_response.url)
        self.assertEquals(response.content, requests_response.content)
        self.assertEquals(response.status_code, requests_response.status_code)
        self.assertEquals(response.headers, requests_response.headers)
        self.assertEquals(response.encoding, requests_response.encoding)

    def test_guess_content_encoding_when_html_response_doesnt_specify_encoding(self):
        response = Response('http://example.com/', HTML_CONTENT)
        self.assertIsNone(response.encoding)

        response.guess_content_encoding()

        self.assertIsNone(response.encoding)

    def test_guess_content_encoding_html_response_when_ascii(self):
        response = Response('http://example.com/', HTML_ASCII_CONTENT)
        self.assertIsNone(response.encoding)

        response.guess_content_encoding()

        self.assertEquals(response.encoding, 'us-ascii')

    def test_guess_content_encoding_html_response_when_utf_8(self):
        response = Response('http://example.com/', HTML_UTF_8_CONTENT)
        self.assertIsNone(response.encoding)

        response.guess_content_encoding()

        self.assertEquals(response.encoding, 'utf-8')

    def test_guess_content_encoding_html_response_when_iso_8859_1(self):
        response = Response('http://example.com/', HTML_ISO_8859_1_CONTENT)
        self.assertIsNone(response.encoding)

        response.guess_content_encoding()

        self.assertEquals(response.encoding, 'iso-8859-1')

    def test_encoding_defaults_to_none(self):
        response = Response('http://example.com', HTML_CONTENT)
        self.assertIsNone(response.encoding)

    def test_text_cannot_be_accessed_without_setting_encoding(self):
        response = Response('http://example.com', HTML_CONTENT)

        with self.assertRaises(ValueError):
            response.text

    def test_text_returns_encoded_utf_8_content_correctly(self):
        response = Response('http://example.com', HTML_UTF_8_CONTENT)
        response.guess_content_encoding()

        self.assertIn('Suscríbete', response.text, 'UTF string incorrect')

    def test_text_returns_encoded_iso_8859_1_content_correctly(self):
        response = Response('http://example.com', HTML_ISO_8859_1_CONTENT)
        response.guess_content_encoding()

        self.assertIn('SuscrÃ\xadbete', response.text, 'ISO string incorrect')

    def test_utf_8_text_falls_back_to_none_when_we_dont_know_the_encoding(self):
        response = Response('http://example.com', HTML_CONTENT)

        self.assertIsNone(response.utf_8_text)

    def test_utf_8_text_returns_encoded_utf_8_content_correctly(self):
        response = Response('http://example.com', HTML_UTF_8_CONTENT)
        response.guess_content_encoding()

        self.assertIn('Suscríbete', response.utf_8_text, 'UTF string incorrect')

    def test_utf_8_text_returns_encoded_iso_8859_1_content_correctly(self):
        response = Response('http://example.com', HTML_ISO_8859_1_CONTENT)
        response.guess_content_encoding()

        self.assertIn('Suscríbete', response.utf_8_text, 'UTF string incorrect')
