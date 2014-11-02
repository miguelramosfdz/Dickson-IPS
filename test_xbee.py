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

def sendData(xBee, i):
    nmeaList=[
            #"$GPRMC,162254.00,A,3723.02837,N,12159.39853,W,0.820,188.36,110706,,,A*74\r\n",
            "$GPVTG,188.36,T,,M,0.820,N,1.519,K,A*3F\r\n",
            #"$GPGGA,162254.00,3723.02837,N,12159.39853,W,1,03,2.36,525.6,M,-25.6,M,,*65\r\n",
            "$GPGSA,A,2,25,01,22,,,,,,,,,,2.56,2.36,1.00*02\r\n",
            "$GPGSV,4,1,14,25,15,175,30,14,80,041,,19,38,259,14,01,52,223,18*76\r\n",
            "$GPGSV,4,2,14,18,16,079,,11,19,312,,14,80,041,,21,04,135,25*7D\r\n",
            "$GPGSV,4,3,14,15,27,134,18,03,25,222,,22,51,057,16,09,07,036,*79\r\n",
            "$GPGSV,4,4,14,07,01,181,,15,25,135,*76\r\n",
            #"$GPGLL,3723.02837,N,12159.39853,W,162254.00,A,A*7C\r\n",
            "$GPZDA,162254.00,11,07,2006,00,00*63\r\n",
            ]

    if i==0:
        lat=-35.249391
        lon=149.153513
        gprmc=libnmea.gprmc(lat,lon)
        print gprmc,
        xBee.write( gprmc )
    else:
        print nmeaList[i],
        xBee.write( nmeaList[i] )

if __name__ == "__main__":

    # xBee information
    xBee = libxbee.connect(config.xBaud,port=config.xPort)
    if xBee:
        print("XBee %sdetected%s."%(colors[2],ENDC) )
    else:
        print("XBee %snot found%s."%(colors[4],ENDC) )

    print("Starting %sTEST%s protocol."%(colors[2], ENDC) )

    i=0
    while 1:
        if xBee:
            sendData(xBee,i)
        i=(i+1)%1
