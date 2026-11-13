
from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    pass

server = HTTPServer(("127.0.0.1", 8000), MyHandler)

print("Web Server Started Successfully")
print("Open http://127.0.0.1:8000")

server.serve_forever()
