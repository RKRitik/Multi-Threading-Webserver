# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 08:50:20 2019

@author: HP
"""
import random
import os
import socket
import time

host = socket.gethostname()
#host='172.17.63.77'
port = 2004
BUFFER_SIZE = 2000
#MESSAGE = input("tcpClientA: Enter message/ Enter exit:")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

time_start = time.time()

dst='D:\os project'


#filename = input(str("Please enter a filename for the incoming file : "))
    
filename='rand' +str(random.randint(1,100)) +'.mp4'
fp = open(filename, 'wb')
# image
while True:
    strng = tcpClientA.recv(1024)
    if not strng:
        break
    fp.write(strng)
    
    
fp.close()
print ("Data Received successfully")
time_end = time.time()

duration_time = time_end - time_start
print ('time:  start = ',time_start, ' end = ',time_end)
print ('time:  duration_time = ', duration_time)
#exit()

tcpClientA.close()
