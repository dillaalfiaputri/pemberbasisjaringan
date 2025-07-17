from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):  
    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://testserver.com</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("<img src='https://stikombanyuwangi.ac.id/images/image.png'>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

        message = """
        <html
        <body>
            <p>Contoh input method get</p>
            <form action="/input" method="get">
                <label>Masukkan Nama Anda:</label>
                <input type="text" name="nama">
                <input type="submit" value="Kirim">
            </form>
        </body>
        </html>
        """
        self.wfile.write(message.encode('utf-8'))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))  
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
webServer.server_close()