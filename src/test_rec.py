#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Main Server file """

import socket
import select
import json
import libnmea
import libxbee
import config

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

node_positions={
        "00":[35.3075,149.1244],
        }

colors = ['\033[95m','\033[94m','\033[92m','\033[93m','\033[91m']
ENDC = '\033[0m'

def sendData(xBee, coord):
    #lat,lon=coord
    lat=139.1244
    lon=35.3075
    gprmc=libnmea.gprmc(lat,lon)
    print(gprmc)
    xBee.write( gprmc )

if __name__ == "__main__":

    # xBee information
    #xPort=config.xPort
    xPort="/dev/tty.usbserial-A100RYLY"
    xBaud=38400
    xBee=0
    try:
        xBee = libxbee.connect(xPort,xBaud)
        print("XBee %sfound%s at %s%s%s."%(colors[2],ENDC,colors[0],xPort,ENDC) )
    except:
        print("XBee %snot found%s at %s."%(colors[4],ENDC,xPort) )

    print("Starting %sTEST%s protocol."%(colors[2], ENDC) )

    data=""

    while 1:
        data = xBee.read()
        print(data.encode('hex'))
        #print(data)
