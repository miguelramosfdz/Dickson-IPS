#!/usr/bin/python
# -*- coding: utf-8 -*-

"""colourRec.py: Is able to detect different coloured boxes. Having numerous colours may slow it down."""
""" The main file of the Target Tracking program """

import cv2
import numpy as np

import colourValues

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

def main():
    webcam = cv2.VideoCapture(1)
    while True:
        rval, frame = webcam.read()

        # Image is flipped for previewing and more straight-forward coordinate system.
        frame=cv2.flip(frame,1,0)

        # Blurring removes possible false-positives
        img=cv2.GaussianBlur(frame, (5,5), 0)

        # Convert to HSV colour space - easier colour definitions
        img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # The colours of the markers, defined in colourValues.py
        for colour in ['blue', 'red']:

            # Only the target colour is used
            separated=cv2.inRange(img,colourValues.lowerRange[colour],colourValues.upperRange[colour])

            # Detect the contours - OpenCV has a built in function for this.
            contours,hierarchy=cv2.findContours(separated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

            # Only the largest contour with an area greater than 1000 is used.
            max_area = 0
            largest_contour = None
            for idx, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if area > max_area and area > 1000:
                    max_area = area
                    largest_contour=contour

            # If there is a detected object, calculate it's center, draw a square around it and save the position.
            if largest_contour != None:
                M = cv2.moments(largest_contour)
                cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
                cv2.circle(frame,(cx,cy),2,colourValues.rectangleC[colour],5)
                rect = cv2.minAreaRect(largest_contour)
                rect = ((rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
                cv2.putText(frame,"35'30'%s''S 149'12'%s''E"%(10, 10), (int(rect[0][0])-20, int(rect[0][1]-30)), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
                box = np.int0(cv2.cv.BoxPoints(rect))
                cv2.drawContours(frame,[box], 0, colourValues.rectangleC[colour], 2)
        
        # Show the image (optionally, resize before doing so)
        #frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
        cv2.imshow('image',frame)

        # Wait for the Esc key to break.
        key=cv2.waitKey(10)
        if key==27:
            break

if __name__=='__main__':
    main()
