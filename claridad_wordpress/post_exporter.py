from .csv_exporter import CsvExporter
from slugify import slugify

class PostExporter(CsvExporter):

    @property
    def headers(self):
        return [
            'post_id',
            'post_author',
            'post_date',
            'post_title',
            # 'post_excerpt',
            'post_status',
            # 'post_password',
            # 'post_name',
            # 'post_parent',
            # 'menu_order',
            'post_type',
            # 'post_thumbnail',
            # 'post_category',
            # 'post_tags',
            # 'tax_{taxonomy}',
            # '{custom_field_key}',
            # 'cfs_{field_name}',
            # 'scf_{field_name}',
            'comment_status',
            'post_content',
        ]

    def row(self, article):
        return [
            article.id,
            slugify(article.author_name),
            article.date_published.strftime('%Y-%m-%d'),
            article.title,
            'publish',
            'post',
            'open',
            article.body,
        ]
