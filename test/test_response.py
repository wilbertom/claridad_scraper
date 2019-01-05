from unittest import TestCase
import requests

from claridad_scraper import Response, DBSink
from test.support.responses import HTML_UTF_8_RESPONSE, HTML_ASCII_RESPONSE, HTML_ISO_8859_1_RESPONSE


class TestResponse(TestCase):
    def setUp(self):
        self.sink = DBSink('/tmp/example_database_sink')

    def tearDown(self):
        self.sink.destroy()

    def test_from_requests_response(self):
        requests_response = requests.get('http://example.com')
        response = Response.from_requests_response(requests_response)

        self.assertEquals(response.url, requests_response.url)
        self.assertEquals(response.content, requests_response.content)
        self.assertEquals(response.status_code, requests_response.status_code)
        self.assertEquals(response.headers, requests_response.headers)

    def test_from_db_record_when_saved_with_our_response_wrapper(self):
        link = 'http://example.com'
        requests_response = requests.get(link)
        response = Response.from_requests_response(requests_response)
        self.sink.save(response)
        record_id = self.sink.id(response.url)
        record = self.sink.get(record_id)

        response = Response.from_sink_record(self.sink, record)

        self.assertEquals(response.url, requests_response.url)
        self.assertEquals(response.content, requests_response.content)
        self.assertEquals(response.status_code, requests_response.status_code)
        self.assertEquals(response.headers, requests_response.headers)

    def test_from_db_record_when_saved_directly_from_a_requests_response(self):
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
