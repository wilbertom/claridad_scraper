from bs4 import BeautifulSoup
from .link_helpers import LinkHelpers


class Parser:
    def __init__(self, site):
        self.site = site
        self.link_helpers = LinkHelpers(site)

    def parse(self, response):
        if self._is_html(response):
            return BeautifulSoup(response.content, 'html.parser')
        elif self._is_pdf(response) \
                or self._is_gif(response) \
                or self._is_jpeg(response):
            return response.content
        else:
            return None

    def links(self, parsed):
        if not isinstance(parsed, BeautifulSoup):
            # do not look for links in things that aren't HTML pages
            return []

        links = []

        for anchor in parsed.find_all('a'):
            link = self.link_helpers.expand(anchor.get('href'))

            if self._should_scrape(link):
                links.append(link)

        return list(set(links))

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
