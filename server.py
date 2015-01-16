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
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        #print "{} wrote:".format(self.client_address[0])
        #print self.data
        # just send back the same data, but upper-cased
	phrase=("<meta http-equiv='content-type' content='text/html; charset=UTF-8'>Ich fordere: Wer %s, der %s!" % (g.generateWordPair())).encode('utf8', 'replace')
        self.request.sendall(phrase)
	print phrase
if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
