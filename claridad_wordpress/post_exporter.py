import csv


class PostExporter:
    def __init__(self, fp):
        self._csv = csv.writer(fp)
        self.headers = [
            'post_id',
            'post_author',
            'post_date',
            'post_content',
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
        ]

        self._csv.writerow(self.headers)

        self.post_id = self.headers.index('post_id')
        self.post_author = self.headers.index('post_author')
        self.post_date = self.headers.index('post_date')
        self.post_content = self.headers.index('post_content')
        self.post_title = self.headers.index('post_title')
        self.post_status = self.headers.index('post_status')
        self.post_type = self.headers.index('post_type')
        # self.post_category = self.headers.index('post_category')
        self.comment_status = self.headers.index('comment_status')

    def row(self, article):
        return [
            article.id,
            article.author_name,
            article.date_published.strftime('%Y-%m-%d'),
            article.body,
            article.title,
            'publish',
            'post',
            'open'
        ]

    def export(self, article):
        self._csv.writerow(self.row(article))
