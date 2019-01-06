from unittest import TestCase
import datetime

from claridad_wordpress import User


class TestUser(TestCase):

    def setUp(self):
        self.user = User(
            1, 'user', 'User', 'user@example.com',
        )

    def test_it_sets_the_id(self):
        self.assertEquals(self.user.id, 1)

    def test_it_sets_the_user_login(self):
        self.assertEquals(self.user.user_login, 'user')

    def test_it_sets_the_user_nicename(self):
        self.assertEquals(self.user.user_nicename, 'user')

    def test_it_sets_the_user_email(self):
        self.assertEquals(self.user.user_email, 'user@example.com')

    def test_it_defaults_the_display_name_to_the_nicename(self):
        self.assertEquals(self.user.display_name, 'User')

    def test_it_defaults_the_user_url_to_none(self):
        self.assertIsNone(self.user.user_url)

    def test_it_defaults_the_user_pass_to_none(self):
        self.assertIsNone(self.user.user_pass)

    def test_it_defaults_the_user_registered_to_now(self):
        now = datetime.datetime.utcnow()
        self.assertEquals(self.user.user_registered.year, now.year)
        self.assertEquals(self.user.user_registered.month, now.month)
        self.assertEquals(self.user.user_registered.day, now.day)

    def test_it_defaults_the_user_activation_key_to_none(self):
        self.assertIsNone(self.user.user_activation_key)

    def test_it_defaults_the_user_status_to_zero(self):
        self.assertEquals(self.user.user_status, 0)
