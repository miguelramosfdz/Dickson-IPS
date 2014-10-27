#!/usr/bin/python
# -*- coding: utf-8 -*-

""" libxbee """

import serial

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

# Connect to Xbee
def connect(port, baud):
    return serial.Serial(port, baud)

if __name__=="__main__":
    self.ser = serial.Serial(20, 9600)

    # Send data (a string)
    self.ser.write("$*0")

    # Read data
    self.data += self.ser.read()
