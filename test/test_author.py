from unittest import TestCase

from test.support.files import support_file_contents
from claridad import Author


class TestAuthor(TestCase):
    def setUp(self):
        self.author_1 = Author(support_file_contents('author_1.html').decode('utf-8'))
        self.author_2 = Author(support_file_contents('author_2.html').decode('utf-8'))
        self.author_3 = Author(support_file_contents('author_3.html').decode('utf-8'))

    def test_it_has_a_name(self):
        self.assertEquals(self.author_1.name, 'Gervasio Morales Rodríguez')
        self.assertEquals(self.author_2.name, 'Democracy Now')
        self.assertEquals(self.author_3.name, 'María (Tati) Dolores Fernós')

    def test_profile_picture_url_returns_the_url_when_present(self):
        self.assertEquals(self.author_1.profile_picture_url, '/images/autores/Gervasio Morales Rodríguez.jpg')
        self.assertEquals(self.author_2.profile_picture_url, '/images/autores/democracy now.jpg')

    def test_profile_picture_url_returns_the_none_when_the_author_doesnt_have_a_profile_picture(self):
        self.assertEquals(self.author_3.profile_picture_url, None)

    def test_it_creates_a_username_from_the_author_name(self):
        self.assertEquals(self.author_1.username, 'gervasio-morales-rodriguez')
        self.assertEquals(self.author_2.username, 'democracy-now')
        self.assertEquals(self.author_3.username, 'maria-tati-dolores-fernos')

    def test_it_has_a_email_when_listed_on_the_webpage(self):
        self.assertEquals(self.author_1.email, 'gmoralesrodz@claridadpuertorico.com')

    def test_it_has_a_email_of_none_when_it_isnt_listed_on_the_webpage(self):
        self.assertIsNone(self.author_2.email)
        self.assertIsNone(self.author_3.email)
