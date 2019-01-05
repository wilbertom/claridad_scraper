from .response import Response


class Cache:

    def __init__(self, sink):
        self._sink = sink

    def cached(self, link):
        record_id = self._sink.id(link)

        if record_id is not None:
            record = self._sink.get(record_id)
            return Response.from_sink_record(self._sink, record)

        return None
