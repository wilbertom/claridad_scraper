import os
import dataset
import requests
import shutil
import json

from .response import Response


class DBSink:
    def __init__(self, fs_dir):
        self._fs_dir = fs_dir
        self._pdfs_dir = os.path.join(self._fs_dir, 'pdfs')
        self._images_dir = os.path.join(self._fs_dir, 'images')
        self._pages_dir = os.path.join(self._fs_dir, 'pages')
        self._db = dataset.connect('sqlite:///{}'.format(os.path.join(self._fs_dir, 'db.sqlite3')))
        self._table = self._db['entries']

        if not os.path.isdir(self._fs_dir):
            os.mkdir(self._fs_dir)
            os.mkdir(self._pdfs_dir)
            os.mkdir(self._images_dir)
            os.mkdir(self._pages_dir)

    def save(self, response):
        if not isinstance(response, Response):
            raise ValueError('We only support saving our response wrapper')

        headers = self._headers(response)

        return self._table.insert({
            'link': response.url,
            'content': response.content,
            'status_code':  response.status_code,
            'headers': json.dumps(headers),
            'error': response.status_code != requests.codes.ok,
            'content_type': headers['content-type'].split(';')[0],
            'text': response.utf_8_text,
        })

    def get(self, id):
        return self._table.find_one(id=id)

    def id(self, link):
        record = self._table.find_one(link=link)

        if record is not None:
            return record['id']

        return None

    def content(self, record):
        return record['content']

    def text(self, record):
        return record['text']

    def link(self, record):
        return record['link']

    def has_errors(self, record):
        return record['error']

    def content_type(self, record):
        return record['content_type']

    def headers(self, record):
        return json.loads(record['headers'])

    def status_code(self, record):
        return record['status_code']

    def destroy(self):
        shutil.rmtree(self._fs_dir)

    def _headers(self, response):
        return {k.lower(): v for k, v in dict(response.headers).items()}
