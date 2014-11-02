#!/usr/bin/python
# -*- coding: utf-8 -*-

"""colourRec.py: Is able to detect different coloured boxes. Having numerous colours may slow it down."""
""" The main file of the Target Tracking program """

import socket
import json

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

def main():
    host="localhost"
    port=5001
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    con=0
    try:
        s.connect((host,port))
        con=1
    except:
        print("Unable to connect")
    while True:
        toSend={}
        toSend["red"]=[111,43]
        jsonData=json.dumps(toSend)
        print(jsonData)
        if(con==1):
            s.send(jsonData)
            
if __name__=='__main__':
    main()

