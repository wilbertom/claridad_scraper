from bs4 import BeautifulSoup
from slugify import slugify


class Author:
    def __init__(self, content):
        self._soup = BeautifulSoup(content, 'html.parser')

    @property
    def name(self):
        return self._soup.find(id='content3').find('h2').get_text().strip()

    @property
    def username(self):
        return slugify(self.name)

    @property
    def email(self):
        tag = self._soup.find(id='edited')

        if tag is None:
            return None

        return tag.get_text().strip()

    @property
    def profile_picture_url(self):
        image_tag = self._soup.find(class_='mainPhotoInside2')

        if image_tag is None:
            return None

        return image_tag['src']
