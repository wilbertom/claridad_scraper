from .csv_exporter import CsvExporter


class UserExporter(CsvExporter):

    @property
    def headers(self):
        return [
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

    def row(self, user):
        return [
            user.id,
            user.user_login,
            user.user_pass,
            user.user_nicename,
            user.user_email,
            user.user_url,
            user.user_registered.strftime('%Y-%m-%d %H:%M:%S'),
            user.user_activation_key,
            user.user_status,
            user.display_name,
        ]
