from unittest import TestCase
import requests
from claridad_scraper import DBSink, Cache


class TestCache(TestCase):

    def setUp(self):
        self.sink = DBSink('/tmp/example_database_sink')
        self.cache = Cache(self.sink)

    def tearDown(self):
        self.sink.destroy()

    def test_it_knows_when_a_link_has_been_cached(self):
        link = 'http://example.com/'
        response = requests.get(link)
        self.sink.save(link, response)
        self.assertIsNotNone(self.cache.cached(link))

    def test_it_knows_when_a_link_has_not_been_cached(self):
        link = 'http://example.com/'
        self.assertIsNone(self.cache.cached(link))

    def test_it_can_return_the_cached_response(self):
        link = 'http://example.com/'
        response = requests.get(link)

        self.sink.save(link, response)
        cached_response = self.cache.cached(link)

        self.assertEquals(response.status_code, cached_response.status_code)
        self.assertEquals(response.headers, cached_response.headers)
        self.assertEquals(response.content, cached_response.content)
