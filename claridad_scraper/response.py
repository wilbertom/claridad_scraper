from bs4 import BeautifulSoup


class Response:

    @classmethod
    def from_requests_response(cls, response):
        return cls(
            response.url,
            response.content,
            response.status_code,
            response.headers,
            response.encoding,
        )

    @classmethod
    def from_sink_record(cls, sink, record):
        return cls(
            sink.link(record),
            sink.content(record),
            sink.status_code(record),
            sink.headers(record),
            sink.encoding(record),
        )

    def guess_content_encoding(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        self.encoding = self._parse_encoding(soup)
        return self

    @property
    def text(self):
        if self.encoding is None:
            raise ValueError

        return str(self.content, self.encoding)

    @property
    def utf_8_text(self):
        try:
            return self.content.decode('utf-8')
        except ValueError:
            return None

    def _parse_encoding(self, soup):
        meta = soup.find('meta', {'http-equiv': 'Content-Type'})

        if meta is None:
            return self.encoding

        return meta['content'].split('=')[1].lower()

    def __init__(self, url, content, status_code=200, headers=None,  encoding=None):
        self.url = url
        self.content = content
        self.encoding = encoding
        self.status_code = status_code
        self.headers = headers