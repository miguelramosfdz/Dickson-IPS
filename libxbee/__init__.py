#!/usr/bin/python
# -*- coding: utf-8 -*-

""" libxbee """

import serial

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

# Connect to Xbee
self.ser = serial.Serial(20, 9600, timeout=100)

# Send data (a string)
self.ser.write(packet)

# Read data
self.data += self.ser.read()
