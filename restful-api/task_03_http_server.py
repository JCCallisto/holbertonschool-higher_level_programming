import http.server
import json
import socketserver


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for a simple API server.
    """

    def do_GET(self):
        """
        Handle GET requests for different endpoints.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = json.dumps(sample_data)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/info':
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = json.dumps(info_data)
            self.wfile.write(json_data.encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


def run_server(port=8000):
    """
    Start the HTTP server on the specified port.
    """
    with socketserver.TCPServer(("", port), SimpleAPIHandler) as httpd:
        print(f"Server running on http://localhost:{port}")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    run_server()
