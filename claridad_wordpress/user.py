import datetime
from slugify import slugify


class User:

    def __init__(
            self,
            id, user_login, display_name, user_email,
    ):
        self.id = id
        self.user_login = user_login
        self.user_pass = None
        self.user_email = user_email
        self.user_url = None
        self.user_registered = datetime.datetime.utcnow()
        self.user_activation_key = None
        self.user_status = 0
        self.display_name = display_name

    @property
    def user_nicename(self):
        return slugify(self.user_login)
