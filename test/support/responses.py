from claridad_scraper import Response

with open('test/support/files/example.pdf', 'rb') as f:
    _PDF = f.read()


_PAGE = """
<html>
  <head></head>
  <body>
    <a href="http://example.com/" />
    <a href="javascript:SomeForm(1);" />
    <a href="/section.html" />
    <a href="http://example.com/section.html" />
    <a href="about.html" />
    <a />
    <a href="mailto:person@example.com" />
    <a href=&quot;mailto:person@example.com&quot;>
    <a href="http://example.com/contact.html" />
    <a href="http://anotherwebsite.com/" />
    <a href="http://example.com/" />
  </body>
</html>
"""

_ERROR = """
<html>
  <head></head>
  <body>
    <h1>Internal Server Error</h1>
  </body>
</html>
"""

HTML_RESPONSE = Response(
    'http://example.com', _PAGE, headers={'content-type': 'text/html; charset=utf-8'}
)

PDF_RESPONSE = Response(
    'http://example.com/example.pdf', _PDF, headers={'content-type': 'application/pdf; charset=utf-8'}
)

JPG_RESPONSE = Response(
    'http://example.com/example.jpg', _PDF, headers={'content-type': 'image/jpeg; charset=utf-8'}
)

GIF_RESPONSE = Response(
    'http://example.com/example.gif', _PDF, headers={'content-type': 'image/gif; charset=utf-8'}
)

ANOTHER_RESPONSE = Response(
    'http://example.com/example.somethingelse', _PDF, headers={'content-type': 'application/something-else; charset=utf-8'}
)

ERROR_RESPONSE = Response(
    'http://example.com/error.html', _ERROR, status_code=500, headers={'content-type': 'text/html; charset=utf-8'}
)
