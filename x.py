import sys
import http.server
import socketserver

addr = "127.0.0.1"
port = 8333


# class myHandler(http.server.SimpleHTTPRequestHandler):
# 	def do_GET(self):
# 		self.
# 		print(self.headers)
# 		print ("GET")  
# 		print(self.headers['content-length'])

handler = http.server.SimpleHTTPRequestHandler

# handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((addr, port), handler)
print ("HTTP server is at: http://%s:%d/" % (addr, port))
httpd.serve_forever()


