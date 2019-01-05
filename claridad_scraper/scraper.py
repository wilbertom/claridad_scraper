import time
import requests
import logging
import sys
from .parser import Parser
from .cache import Cache
from .response import Response


class Scraper:
    def __init__(self, site, db_sink):
        self._site = site
        self._parser = Parser(site)
        self._sink = db_sink
        self._cache = Cache(self._sink)

        self._links = set([])
        self._sleep = 0.05

        self._logger = logging.getLogger('claridad_scraper.scraper')
        fh = logging.FileHandler('claridad_scraper.scraper.log')
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self._logger.addHandler(fh)

    def run(self):
        try:
            self._scrape(self._site)
        except KeyboardInterrupt:
            self._logger.info('Shutdown while scrapping {}'.format(link))
            sys.exit(0)

        self._logger.info('Scraped {} links'.format(len(self._links)))

    def skip(self, link):
        if link in self._links:
            return True

        if 'contentpdf.html?news' in link:
            return True

        return False

    def _scrape(self, link):
        if self.skip(link):
            return

        response = self._get_link(link)

        if response.status_code != requests.codes.ok:
            self._logger.error("Error {}".format(response.url))
            return

        links = self._parser.links(response)

        for link in links:
            self._scrape(link)

    def _get_link(self, link):
        self._links.add(link)
        response = self._cache.cached(link)

        if response is not None:
            self._logger.info('Using response cached for {}'.format(response.url))
            return response
        else:
            time.sleep(self._sleep)
            response = Response.from_requests_response(requests.get(link))
            self._logger.info("Fetched {}".format(response.url))
            self._sink.save(response)
            return response
