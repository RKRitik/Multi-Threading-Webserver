import socket
from concurrent.futures import ThreadPoolExecutor
from time import ctime
from threading import Thread
PORT = 2008
BUFSIZE = 1024
class ClientHandler(Thread):
    """Handles a client request."""
    def __init__(self, client,address):
        Thread.__init__(self)
        self._client = client
        self.address = address


    def run(self):
        print('...connected from:', address)
        #self._client.send(bytes(ctime() + '\nHave a nice day!' , 'ascii'))
        #msg = '..'
        filename = input(str("Please enter the filename of the file : "))
        file = open(filename , 'rb')
        file_data = file.read(1024)
        client.send(file_data)
        print("Data has been transmitted successfully")
        #while len(msg)>0:
            #msg = self._client.recv(BUFSIZE)
            #print('message recieved ',msg.decode('utf-8'))
            #self._client.send(bytes('message recieved ..' , 'ascii'))
        self._client.close()


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()

ADDRESS = (host, PORT)
s.bind(ADDRESS)
s.listen(5)
executor = ThreadPoolExecutor(max_workers=5)
# The server now just waits for connections from clients
# and hands sockets off to client handlers
while True:
    print('Waiting for connection')
    client, address = s.accept()

    executor.submit(ClientHandler(client,address).start())
    # handler = ClientHandler(client)
    # handler.start()
