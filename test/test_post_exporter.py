import unittest
import io

from test.support.files import support_file_contents
from claridad_wordpress import PostExporter
from claridad import Article


class TestPostExporter(unittest.TestCase):

    def setUp(self):
        self.fp = io.StringIO()
        self.exporter = PostExporter(self.fp)
        self.article_1 = Article(1, support_file_contents('article_1.html'))

    def test_it_returns_headers_with_all_post_columns(self):
        self.assertEquals(
            self.exporter.headers,
            [
                'post_id',
                'post_author',
                'post_date',
                'post_content',
                'post_title',
                'post_status',
                'post_type',
                # 'post_category',
                'comment_status',
            ]
        )

    def test_it_returns_a_csv_row_with_post_id_set(self):
        row = self.exporter.row(self.article_1)

        self.assertEquals(row[self.exporter.post_id], 1)

    def test_it_returns_a_csv_row_with_post_author_set(self):
        row = self.exporter.row(self.article_1)

        self.assertEquals(row[self.exporter.post_author], self.article_1.author_name)

    def test_it_returns_a_csv_row_with_post_date_set(self):
        row = self.exporter.row(self.article_1)

        self.assertEquals(row[self.exporter.post_date], '2018-10-30')

    def test_it_returns_a_csv_row_with_post_content_set(self):
        row = self.exporter.row(self.article_1)

        self.assertEquals(row[self.exporter.post_content], self.article_1.body)

    def test_it_returns_a_csv_row_with_post_title_set(self):
        row = self.exporter.row(self.article_1)

        self.assertEquals(row[self.exporter.post_title], self.article_1.title)

    def test_it_returns_a_csv_row_with_post_status_set(self):
        row = self.exporter.row(self.article_1)

        self.assertEquals(row[self.exporter.post_status], 'publish')

    def test_it_returns_a_csv_row_with_post_type_set(self):
        row = self.exporter.row(self.article_1)

        self.assertEquals(row[self.exporter.post_type], 'post')

    def test_it_returns_a_csv_row_with_post_category_set(self):
        self.fail('Still are not handling categories')
        # row = self.exporter.row(self.article_1)
        #
        # self.assertEquals(row[self.exporter.post_category], '')

    def test_it_returns_a_csv_row_with_comment_status_set(self):
        row = self.exporter.row(self.article_1)

        self.assertEquals(row[self.exporter.comment_status], 'open')

    def test_it_will_export_headers_on_initialization(self):
        fp = io.StringIO()
        exporter = PostExporter(fp)

        self.assertEquals(
            fp.getvalue(),
            'post_id,post_author,post_date,post_content,post_title,post_status,post_type,comment_status\r\n'
        )

    def test_it_exports_article_rows(self):
        self.exporter.export(self.article_1)

        self.maxDiff = 30000
        self.assertEquals(
            self.fp.getvalue(),
            'post_id,post_author,post_date,post_content,post_title,post_status,post_type,comment_status\r\n' +
            '1,Juan R. Recondo,2018-10-30,"{}",La cazadora y  su monstruo Halloween (2018),publish,post,open\r\n'.format(
                self.article_1.body
            )
        )
