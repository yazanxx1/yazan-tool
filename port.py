#!/usr/bin/python3

# ===== #

# ===== #
# Created Nov 2019 | Copyright (c)2019 Aliensec.
# ===== #

import threading
from queue import Queue
import time
import socket

# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.
print_lock = threading.Lock()



target = input('Enter ip Address: ')

maxport = int(input('Enter the max Number port to scan: '))




def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port)
        con.close()
    except:
        pass


# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()



#!/usr/bin/python3

# ===== #
# AlienSec
# facebook.com/aliensec.tech
# Youtube: https://youtube.com/c/aliensec
# https://www.aliensec.com/
# ===== #

# ===== #
# Created Nov 2019 | Copyright (c)2019 Aliensec.
# ===== #

import threading
from queue import Queue
import time
import socket
# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.
print_lock = threading.Lock()



target = input('Enter ip Address: ')

maxport = int(input('Enter the max Number port to scan: '))
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port)
        con.close()
    except:
        pass
# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()



        

# Create the queue and threader 
q = Queue()# how many threads are we going to allow for
for x in range(100):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()


start = time.time()

# 100 jobs assigned.
for worker in range(1,maxport):
    q.put(worker)

# wait until the thread terminates.
q.join()

