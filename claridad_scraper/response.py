
class Response:

    @classmethod
    def from_requests_response(cls, response):
        return cls(
            response.url,
            response.content,
            response.status_code,
            response.headers,
        )

    @classmethod
    def from_sink_record(cls, sink, record):
        return cls(
            sink.link(record),
            sink.content(record),
            sink.status_code(record),
            sink.headers(record),
        )

    def __init__(self, url, content, status_code=200, headers=None):
        self.url = url
        self.content = content
        self.status_code = status_code
        self.headers = headers
