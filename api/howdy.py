from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        print("hello Razan :)")
        message="welcome howdy"
        self.wfile.write(message.encode())
        return