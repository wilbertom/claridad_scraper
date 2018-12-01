from urllib.parse import urlparse, urljoin


class LinkHelpers:
    @classmethod
    def is_javascript(cls, link):
        return link.startswith('javascript:')

    @classmethod
    def is_mailto(cls, link):
        return link.startswith('mailto:')

    @classmethod
    def is_not_url(cls, link):
        if cls.is_javascript(link) or cls.is_mailto(link):
            return True

        # we know when it is not a URL in some cases but we can't test for all without doing some other validation
        return None

    @classmethod
    def is_relative(cls, link):
        url = urlparse(link)
        return url.hostname is None

    @classmethod
    def is_to(cls, site_link, target_link):
        return urlparse(site_link).hostname == urlparse(target_link).hostname

    def __init__(self, local_link):
        self._local_link = local_link
        self._local_url = urlparse(self._local_link)

    def is_local(self, link):
        return self.is_relative(link) or self.is_to(self._local_link, link)

    def expand(self, link):
        if self.is_relative(link):
            return self._fully_qualify_relative_url(link)
        else:
            return link

    def _fully_qualify_relative_url(self, link):
        return urljoin(self._local_link, link)
