import time
import requests
import logging
import sys
from .parser import Parser
from .cache import Cache


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
        self._scrape(self._site)
        self._logger.info('Scraped {} links'.format(len(self._links)))

    def _scrape(self, link):
        try:
            if link in self._links:
                return

            self._logger.info('Fetching {}'.format(link))

            self._links.add(link)
            response = self._get_link(link)

            if response.status_code != requests.codes.ok:
                self._logger.error(response)

            else:
                # import pdb; pdb.set_trace()
                parsed = self._parser.parse(response)

                if parsed is None:
                    self._logger.warning("Ignored unknown content {}".format(response.url))
                    return

                links = self._parser.links(parsed)

                for link in links:
                    self._scrape(link)

        except KeyboardInterrupt:
            self._logger.info('Shutdown while scrapping {}'.format(link))
            sys.exit(0)

    def _get_link(self, link):
        response = self._cache.cached(link)

        if response is not None:
            self._logger.info('Using response cached for {}'.format(response.url))
            return response
        else:
            time.sleep(self._sleep)
            response = requests.get(link)
            self._logger.info("Fetched {}".format(link))
            self._sink.save(link, response)
            return response
