#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Main Server file """

import socket
import select
import json
import libnmea
import libxbee
import config
import libcmn

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

# List to keep track of socket descriptors
CONNECTION_LIST = []
RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this has no effect, why ?
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)

# Add server socket to the list of readable connections
CONNECTION_LIST.append(server_socket)

xBee = libxbee.connect(config.xBaud,port=config.xPort)
if xBee:
    libcmn.debug("XBee *green*detected*end*.")
else:
    libcmn.debug("XBee *red*not found*end*.")
libcmn.debug("Starting IPS server on port *purple*%s*end*."%PORT)

while 1:

    # Get the list sockets which are ready to be read through select
    read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
    for sock in read_sockets:
        if sock == server_socket:
            # Handle the case in which there is a new connection recieved through server_socket
            sockfd, addr = server_socket.accept()
            CONNECTION_LIST.append(sockfd)
            libcmn.debug("Client *green*(%s, %s)*end* connected" %(addr[0], addr[1]))
        
        #Some incoming message from a client
        else:
            # Data recieved from client, process it
            try:
                #In Windows, sometimes when a TCP program closes abruptly,
                # a "Connection reset by peer" exception will be thrown
                data = sock.recv(RECV_BUFFER)
                if data:
                    try:
                        data=json.loads(data) ######### URGENT. Remove eval. Replace with JSON. #####
                        print("...")
                        print(node_positions[data['ID']])
                        for key in data['det']:
                            print(key)
                            print(data['det'][key])
                            print('')
                        if xBee:
                            1
                    except:
                        print(":O", data)
                        1
            except:
                #print "Client (%s, %s) is offline" % addr
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue

server_socket.close()

print(ENDC)
