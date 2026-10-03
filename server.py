#!/usr/bin/env python3
import http.server
import json

class GenericApiHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_json({"status": "healthy", "service": "mailguard-api", "version": "1.0.0"})
            return
        self.send_json({"success": True, "message": "API mailguard-api active and ready for RapidAPI requests"})

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", 8080), GenericApiHandler)
    server.serve_forever()
