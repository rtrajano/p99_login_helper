#!/bin/env python3
__authors__ = [
    "Rigel Trajano",
]
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0.0"

import socketserver


class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        if self.client_address[0] == "127.0.0.1":
            socket.sendto(data, ("login.eqemulator.net", 5998))
            self.server.last_port = self.client_address[1]
        else:
            socket.sendto(data, ("localhost", self.server.last_port))


def main():
    with socketserver.UDPServer(("", 5998), RequestHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()
