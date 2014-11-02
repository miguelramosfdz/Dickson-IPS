#!/usr/bin/python
# -*- coding: utf-8 -*-

""" libxbee """

import serial
import serial.tools.list_ports

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

# Connect to Xbee
def connect(baud,port="",verbose=1):

    # Automatic Port Detection
    if port=="":
        # The XBee vid:pid == 403:6001
        # list_ports.grep returns a generator
        xBees = serial.tools.list_ports.grep("403:6001")
        for port in xBees:
            try:
                xBee=serial.Serial(port[0],baud)
                if verbose:
                    print( "XBee found at %s ."%port[0] )
            except:
                0
            return xBee

    # Manual Port Detection + No XBees detected
    try:
        xBee=serial.Serial(port,baud)
    except:
        # No XBees where found
        xBee=""

    return xBee

"""
# Send data (a string)
self.ser.write("$*0")

# Read data
self.data += self.ser.read()
"""
