from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

# Set the port for the server
PORT = 8000

# Create and start the server
server = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print(f"Server started at http://localhost:{PORT}")

# Open the browser automatically
webbrowser.open(f'http://localhost:{PORT}/midi_display.html')

# Keep the server running
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server...")
    server.shutdown()