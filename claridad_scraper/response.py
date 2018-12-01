
class Response:
    def __init__(self, url, content, status_code=200, headers=None):
        self.url = url
        self.content = content
        self.status_code = status_code
        self.headers = headers
