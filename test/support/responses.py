from claridad_scraper import Response

with open('test/support/files/example.pdf', 'rb') as f:
    _PDF = f.read()


HTML_CONTENT = """
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
    'http://example.com', HTML_CONTENT.encode('utf=8'), headers={'content-type': 'text/html; charset=utf-8'}
)


with open('test/support/files/utf_8.html', 'rb') as f:
    HTML_UTF_8_CONTENT = f.read()

with open('test/support/files/iso_8859_1.html', 'rb') as f:
    HTML_ISO_8859_1_CONTENT = f.read()

with open('test/support/files/ascii.html', 'rb') as f:
    HTML_ASCII_CONTENT = f.read()


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
    'http://example.com/error.html', _ERROR.encode('utf=8'), status_code=500, headers={'content-type': 'text/html; charset=utf-8'}
)
