#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Main Server file """

import socket
import select
import json
import libnmea
import libxbee

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

colors = ['\033[95m','\033[94m','\033[92m','\033[93m','\033[91m']
ENDC = '\033[0m'

def sendData(xBee, coord):
    #lat,lon=coord
    lat=139.1244
    lon=35.3075
    gprmc=libnmea.gprmc(lat,lon)
    xBee.write( gprmc )

if __name__ == "__main__":
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

    # xBee information
    xPort="/dev/tty.usbserial-A600dJm8"
    xBaud=9600
    xFound=0
    try:
        xBee = libxbee.connect(xPort,xBaud)
        print("XBee %sfound%s at %s%s%s."%(colors[2],ENDC,colors[0],xPort,ENDC) )
        xFound=1
    except:
        print("XBee %snot found%s."%(colors[4],ENDC) )

    print("Starting IPS server on port %s%s%s."%(colors[0], PORT, ENDC) )

    while 1:

        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
        for sock in read_sockets:
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print("Client %s(%s, %s)%s connected" %(colors[2],addr,ENDC))
            
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        try:
                            data=eval(data) ######### URGENT. Remove eval. Replace with JSON. #####
                            print(data)
                            if xFound:
                                sendData(xBee, [0,0] )
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
