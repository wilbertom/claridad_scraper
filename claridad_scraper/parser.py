from bs4 import BeautifulSoup
from .link_helpers import LinkHelpers


class Parser:
    def __init__(self, site):
        self.site = site
        self.link_helpers = LinkHelpers(site)

    def links(self, response):
        parsed = self._parse(response)

        if not isinstance(parsed, BeautifulSoup):
            # do not look for links in things that aren't HTML pages
            return []

        links = set([])

        for anchor in parsed.find_all('a'):
            link = self.link_helpers.expand(anchor.get('href'))

            if self._should_scrape(link):
                links.add(link)

        return list(links)

    def _parse(self, response):
        if self._is_html(response):
            if response.utf_8_text is None:
                raise ValueError("Can't parse a html webpage without know its encoding")

            return BeautifulSoup(response.utf_8_text, 'html.parser')
        elif self._is_pdf(response):
            raise ValueError("Downloaded a PDF but these shouldn't be downloaded")
        elif self._is_gif(response) or self._is_jpeg(response):
            return response.content
        else:
            return None

    def _is_pdf(self, response):
        return response.headers['content-type'].split(';')[0] == 'application/pdf'

    def _is_html(self, response):
        return response.headers['content-type'].split(';')[0] == 'text/html'

    def _is_jpeg(self, response):
        return response.headers['content-type'].split(';')[0] == 'image/jpeg'

    def _is_gif(self, response):
        return response.headers['content-type'].split(';')[0] == 'image/gif'

    def _should_scrape(self, link):
        return link is not None and \
               not self.link_helpers.is_not_url(link) and \
               self.link_helpers.is_local(link)
