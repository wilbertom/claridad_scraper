from datetime import datetime

from bs4 import BeautifulSoup
from .helpers import translate_spanish_month_to_number


class ArticleMetaDataNotFound(ValueError):
    pass


class Article:
    def __init__(self, uid, content):
        self.id = uid
        self._content = content
        self._soup = BeautifulSoup(self._content, 'html.parser')

    @property
    def content_id(self):
        url = self._soup.find('meta', property='og:url')['content']
        return url.split('content.html?news=')[1]

    @property
    def is_summary(self):
        return self._soup.find(id='resumen') is not None

    @property
    def title(self):
        return self._soup.find(id='content3').find('h2').get_text()

    @property
    def pdf_link(self):
        return 'http://www.claridadpuertorico.com/contentpdf.html?news={}'.format(
            self.content_id
        )

    @property
    def body(self):
        paragraphs = []

        for p_tag in self._body_paragraph_tags():
            paragraphs.append(p_tag.get_text().strip())

        return '\n\n'.join(paragraphs)

    @property
    def date_published(self):
        date_published_meta_p = self._content_3_meta_data('Publicado')
        date_published_meta_p = date_published_meta_p.replace('Publicado: ', '')

        # example publish date: "Publicado: martes, 30 de octubre de 2018"
        _day_name, day, _de, month_name, _de, year = date_published_meta_p.split(' ')

        return datetime(
            int(year),
            translate_spanish_month_to_number(month_name),
            int(day)
        )

    @property
    def author_name(self):
        try:
            author_meta_p = self._content_3_meta_data('Por')
        except ArticleMetaDataNotFound as e:
            for p_tag in self._body_paragraph_tags():
                p_text = p_tag.get_text().strip()

                if p_text.startswith('Por') and len(p_text.split(' ')) < 4:
                    author_meta_p = p_text
                    break
            else:
                raise e

        return author_meta_p.replace('Por ', '')

    def _content_3_meta_data(self, meta):
        tables = self._soup \
            .find(id='content3') \
            .find_all('table')

        for table in tables:
            p = table.find('p')

            if p is None:
                continue

            p_text = p.get_text().strip()

            if meta in p_text:
                return p_text

        raise ArticleMetaDataNotFound

    def _body_paragraph_tags(self):
        # the last paragraph tag is some BS with comments
        return self._soup.find(id='my_content').find_all('p')[:-1]
