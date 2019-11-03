import socket

#host = socket.gethostname()
host = "192.168.43.97"
print(host)
port = 2004
BUFFER_SIZE = 2000
#MESSAGE = input("tcpClientA: Enter message/ Enter exit:")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

"""while MESSAGE != 'exit':
    MESSAGE = MESSAGE.encode()
    tcpClientA.send(MESSAGE)
    data = tcpClientA.recv(BUFFER_SIZE)
    print
    " Client2 received data:", data
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")

"""
filename = input(str("Please enter a filename for the incoming file : "))
file = open(filename, 'wb')
file_data = tcpClientA.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully.")

tcpClientA.close()
