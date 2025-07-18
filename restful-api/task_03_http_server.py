from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Ana endpoint: /
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))
        
        # /data endpoint: JSON döndürür
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))
        
        # /status endpoint: basit "OK"
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        # /info endpoint: JSON açıklama döndürür (ek özellik)
        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Tanımlanmamış endpointler için 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    port = 8000
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
