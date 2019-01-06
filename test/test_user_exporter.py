import unittest
import io

from test.support.files import support_file_contents
from claridad_wordpress import UserExporter, User


class TestUserExporter(unittest.TestCase):

    def setUp(self):
        self.fp = io.StringIO()
        self.exporter = UserExporter(self.fp)
        self.user = User(
            1, 'user', 'User', 'user@example.com',
        )

    def test_it_returns_headers_with_all_post_columns(self):
        self.assertEquals(
            self.exporter.headers,
            [
                'id',
                'user_login',
                'user_pass',
                'user_nicename',
                'user_email',
                'user_url',
                'user_registered',
                'user_activation_key',
                'user_status',
                'display_name',
            ]
        )

    def test_it_exports_user_rows(self):
        self.exporter.export(self.user)

        self.assertEquals(
            self.fp.getvalue(),
            'id,user_login,user_pass,user_nicename,user_email,user_url,user_registered,user_activation_key,user_status,display_name\r\n' +
            '1,user,,User,user@example.com,,{},,0,User\r\n'.format(
                self.user.user_registered.strftime('%Y-%m-%d')
            )
        )
