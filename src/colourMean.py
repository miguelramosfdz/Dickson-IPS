#!/usr/bin/python
# -*- coding: utf-8 -*-

"""colourRec.py: Is able to detect differnt coloured boxes. Having numerous colours may slow it down.."""

import cv2
import numpy as np

import colourValues

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = 255*(df/mx)
    v = mx*255
    return map(int, (h, s, v))

def mouse_callback(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
       global new
       new = [x,y]

cv2.namedWindow('image',cv2.WINDOW_NORMAL) # Can be resized
cv2.setMouseCallback('image',mouse_callback) #Mouse callback

