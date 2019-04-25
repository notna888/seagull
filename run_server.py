import http.server
import socketserver
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def launch_web_server():
  WEBDIR = os.path.join(os.path.dirname(__file__), 'output')
  os.chdir(WEBDIR)

  with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

if __name__=='__main__':
  launch_web_server()
