from unittest import TestCase
from claridad_scraper import LinkHelpers


class TestLinkHelpers(TestCase):

    def setUp(self):
        self.local_link = 'http://example.com'
        self.link_helpers = LinkHelpers(self.local_link)

    def test_is_javascript(self):
        self.assertTrue(self.link_helpers.is_javascript('javascript:FormStep(1);'))
        self.assertTrue(self.link_helpers.is_javascript('javascript:'))

        self.assertFalse(self.link_helpers.is_javascript('/'))
        self.assertFalse(self.link_helpers.is_javascript('http://example.com'))
        self.assertFalse(self.link_helpers.is_javascript('mailto:person@example.com'))

    def test_is_mailto(self):
        self.assertTrue(self.link_helpers.is_mailto('mailto:person@example.com'))

        self.assertFalse(self.link_helpers.is_mailto('/'))
        self.assertFalse(self.link_helpers.is_mailto('http://example.com'))
        self.assertFalse(self.link_helpers.is_mailto('javascript:'))

    def test_link_is_not_url(self):
        self.assertTrue(self.link_helpers.is_not_url('javascript:'))
        self.assertTrue(self.link_helpers.is_not_url('mailto:person@example.com'))
        self.assertIsNone(self.link_helpers.is_not_url('http://example.com'))
        self.assertIsNone(self.link_helpers.is_not_url('/'))

    def test_is_relative(self):
        self.assertTrue(self.link_helpers.is_relative('/'))
        self.assertTrue(self.link_helpers.is_relative('/section.html'))
        self.assertTrue(self.link_helpers.is_relative('/section.html?section=1'))
        self.assertTrue(self.link_helpers.is_relative('section.html'))

        self.assertFalse(self.link_helpers.is_relative('http://example.com'))
        self.assertFalse(self.link_helpers.is_relative('http://anotherexample.com'))

    def test_is_to(self):
        self.assertTrue(self.link_helpers.is_to('http://example.com', 'http://example.com'))
        self.assertTrue(self.link_helpers.is_to('http://example.com', 'http://example.com/page.html'))

        self.assertFalse(self.link_helpers.is_to('http://example.com', 'http://anotherexample.com'))
        self.assertFalse(self.link_helpers.is_to('http://example.com', 'http://anotherexample.com/page.html'))

    def test_is_local_returns_true_for_relative_urls(self):
        self.assertTrue(self.link_helpers.is_local('/'))
        self.assertTrue(self.link_helpers.is_local('/section.html'))

    def test_is_local_returns_true_for_local_fully_qualified_links(self):
        self.assertTrue(self.link_helpers.is_local('http://example.com'))
        self.assertTrue(self.link_helpers.is_local('http://example.com/section.html'))

    def test_is_local_returns_false_for_links_to_other_sites(self):
        self.assertFalse(self.link_helpers.is_local('http://anotherexample.com'))
        self.assertFalse(self.link_helpers.is_local('http://anotherexample.com/section.html'))

    def test_expand_noop_on_already_expanded_links(self):
        link = 'http://example.com/page.html'

        self.assertEquals(self.link_helpers.expand(link), link)

    def test_expand_fully_qualifies_relative_links(self):
        link = '/section.html'

        self.assertEquals(
            self.link_helpers.expand(link),
            'http://example.com/section.html'
        )

    def test_expands_fully_qualifies_relative_links_without_a_slash_prefix(self):
        link = 'section.html'

        self.assertEquals(
            self.link_helpers.expand(link),
            'http://example.com/section.html'
        )

    def test_expands_fully_qualifies_relative_links_and_keeps_query_parameters(self):
        link = '/section.html?section=1'

        self.assertEquals(
            self.link_helpers.expand(link),
            'http://example.com/section.html?section=1'
        )

    def test_expands_fully_qualifies_a_single_slash(self):
        link = '/'

        self.assertEquals(
            self.link_helpers.expand(link),
            'http://example.com/'
        )
