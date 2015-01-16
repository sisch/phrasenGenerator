#! /usr/bin/python
import SocketServer
import phrasen

g=phrasen.generator("words.txt")

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.data = self.request.recv(1024).strip()
	phrase=("<meta http-equiv='content-type' content='text/html; charset=UTF-8'>Ich fordere: Wer %s, der %s!" % (g.generateWordPair())).encode('utf8', 'replace')
        self.request.sendall(phrase)
	print phrase
if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
