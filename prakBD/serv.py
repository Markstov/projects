from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

server_adress = ("localhost", 8000)
http_server = HTTPServer(server_adress, CGIHTTPRequestHandler)
http_server.serve_forever()