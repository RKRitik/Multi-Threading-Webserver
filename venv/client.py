# Python TCP Client 
import socket

host = socket.gethostname()
port = 2004
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientA: Enter message/ Enter exit:")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    MESSAGE = MESSAGE.encode()
    tcpClientA.send(MESSAGE)
    data = tcpClientA.recv(BUFFER_SIZE)
    print
    " Client2 received data:", data
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")

tcpClientA.close()