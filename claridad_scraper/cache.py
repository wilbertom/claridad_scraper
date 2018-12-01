from .response import Response


class Cache:

    def __init__(self, sink):
        self._sink = sink

    def cached(self, link):
        id = self._sink.id(link)

        if id is not None:
            record = self._sink.get(id)

            return Response(
                link,
                self._sink.content(record),
                self._sink.status_code(record),
                self._sink.headers(record),
            )

        return None
