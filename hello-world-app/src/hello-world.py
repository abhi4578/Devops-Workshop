import requests
import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        ip=requests.get("https://ifconfig.me").text
        str_return="Hello World I am " + ip
        self.wfile.write(bytes(str_return, 'utf-8'))


httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()

