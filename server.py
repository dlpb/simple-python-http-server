#!/usr/bin/env python2
​
import BaseHTTPServer, SimpleHTTPServer
import SocketServer
import logging
​
PORT = 8080
​
class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
​
    def do_GET(self):
        logging.error("===== Begin Request =====")
        logging.error(self.headers)
        logging.error("====== End Request ======")
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Cache-Control', 'no-cache,no-store')
        self.end_headers()
​
        page ='''{"status":"ok"}'''
​
        self.wfile.write(page)
​
​
Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
​
httpd.serve_forever()