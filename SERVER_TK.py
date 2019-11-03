# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 08:42:50 2019

@author: HP
"""
import os
import time
import socket
from concurrent.futures import ThreadPoolExecutor
from time import ctime
from threading import Thread


sb='D:\os project'
PORT = 2004
BUFSIZE = 1024
class ClientHandler(Thread):
    def __init__(self, client,address):
        Thread.__init__(self)
        self._client = client
        self.address = address



    def run(self):
        #files = os.listdir(sb)
        file='omg.mp4'
        pages = 0;
        """while (files):
            print ('\nMaybe, pending work')
            if (au.find('d')>-1):
                    os.chdir(sb+au)
                    imgFiles = os.listdir(sb+'\''+au)
                    images = [img for img in imgFiles if img.endswith('.jpg')]
                    print ('\n%s user done' ,au)"""
        #self._client.send(file)

        #copies all .img files in the folder from server to client
        #for imgs in images:
        #self._client.send(file)
        file_name = open(file,'rb')
        while True:
            strng = file_name.readline()
            if not strng:
                break
            self._client.send(strng)
        file_name.close()
        #os.remove(sb+'/'+au+'/'+imgs)       
        print ("Data sent successfully")                          
        time.sleep(1)

                    
        self._client.close()


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
ADDRESS = (host, PORT)
s.bind(ADDRESS)
s.listen(5)
executor = ThreadPoolExecutor(max_workers=5)
while True:
    print('Waiting for connection')
    #lab=Label(root, text="Waiting for connection").pack()
    client, address = s.accept()

    executor.submit(ClientHandler(client,address).start())
    # handler = ClientHandler(client)
    # handler.start()

root.mainloop()
