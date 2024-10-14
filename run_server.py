import http.server
import socketserver
import os

PORT = 3000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

os.chdir(os.path.join(os.getcwd(), 'docs', 'html'))
handler_object = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print("serving at port", PORT)
    print("Server is running on http://localhost:" + str(PORT) + ". Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print("Server stopped")
    httpd.server_close()
    print("Server closed")
