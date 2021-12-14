from http.server import HTTPServer, BaseHTTPRequestHandler


LOGFILE = "log/http_server.log"


class CustomHandler(BaseHTTPRequestHandler):
    def custom_log(self, path):
        with open(LOGFILE, "a+") as f:
            f.write(f"{path}\n")
            f.close()

    def set_headers(self):
        self.custom_log(self.path)
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def set_body(self, message="Not Found"):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")

    def do_GET(self):
        self.set_headers()
        self.wfile.write(self.set_body("Not Found"))

    def do_POST(self):
        self.set_headers()
        self.wfile.write(self.set_body("Not Found"))

    def log_message(self, format, *args):
        return


def run(server_class=HTTPServer, handler_class=CustomHandler, addr="127.0.0.1", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting HTTP server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    address = "127.0.0.1"
    port = 65480
    run(addr=address, port=port)
