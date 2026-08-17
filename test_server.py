#!/usr/bin/env python3
"""Tiny local server to test intruder.py against — simulates a login form
where the correct password is 'letmein123'."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

CORRECT_PASSWORD = "letmein123"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silence

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode()
        params = parse_qs(body)
        password = params.get("password", [""])[0]

        if password == CORRECT_PASSWORD:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Welcome back, admin! Login successful.")
        else:
            self.send_response(401)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Invalid credentials.")


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8899), Handler)
    print("Test server running on http://127.0.0.1:8899")
    server.serve_forever()
