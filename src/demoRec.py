#!/usr/bin/python
# -*- coding: utf-8 -*-

"""remoRec.py: A short demonstration of the marker detection."""

import cv2
import numpy as np
from random import randrange

import colourValues

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

if __name__=='__main__':
    webcam = cv2.VideoCapture('demo.mp4')
    rval, im = webcam.read()
    sample = cv2.resize(im, (int(im.shape[1]*0.6), int(im.shape[0]*0.6)))
    #save = cv2.VideoWriter('demoOut.avi', cv2.cv.CV_FOURCC('I', '4', '2', '0'), 15, (sample.shape[1], sample.shape[0]), True)
    save = cv2.VideoWriter('video.mp4', cv2.cv.CV_FOURCC('x', '2', '6','4'), 15, (sample.shape[1],sample.shape[0]), True)
    while True:
        # Restart the video if we've reached the end
        if webcam.get(1)==webcam.get(7): webcam.set(0, 0)
        rval, im = webcam.read()
        if not rval: break

        # Resize, flip, blur (for better detection) and convert colour space
        frame = cv2.resize(im, (int(im.shape[1]*0.6), int(im.shape[0]*0.6)))
        frame=cv2.flip(frame,1,0)
        img=cv2.GaussianBlur(frame, (5,5), 0)
        img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Split the colours (we are only interested in white) and detect the contours
        separated=cv2.inRange(img,colourValues.lowerRange['white'],colourValues.upperRange['white'])
        contours,hierarchy=cv2.findContours(separated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        # Find the biggest contour
        max_area = 0
        largest_contour = None
        for idx, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > max_area and area > 1000:
                max_area = area
                largest_contour=contour

        # If we've found a marker, we want to highlight it
        if largest_contour != None:
            M = cv2.moments(largest_contour)
            cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
            cv2.circle(frame,(cx,cy),2,255,5)
            rect = cv2.minAreaRect(largest_contour)
            #tmp=frame[rect[0][1]-rect[1][1]:rect[0][1]+rect[1][1], rect[0][0]-rect[1][0]:rect[0][0]+rect[1][0]]
            #if tmp.shape[0]>0 and tmp.shape[1]>1:
            #    cv2.imshow('a', tmp)

            cv2.putText(frame,"35'30'%s''S 149'12'%s''E"%(tuple(map(randrange, [60,60]))), (int(rect[0][0])-20, int(rect[0][1]-30)), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
            rect = ((rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
            box = np.int0(cv2.cv.BoxPoints(rect))
            cv2.drawContours(frame,[box], 0, (255, 0, 0), 2)
            detected=True
        else: detected=False

        # Bit of fun: an overlayed display
        overlay = frame.copy()
        cv2.rectangle(overlay, (10,10), (250,120), (21,20,29), -1)
        if detected: cv2.rectangle(overlay, (10,130), (250,160), (21,20,29), -1)
        cv2.addWeighted(overlay, 0.5, frame, 1 - 0.5, 0, frame)
        if detected: cv2.putText(frame,"MARKER DETECTED", (20,150), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
        cv2.putText(frame,"35'30'%s''S 149'12'%s''E"%(tuple(map(randrange, [60,60]))), (20,30), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
        cv2.putText(frame,"35'30'%s''S 149'12'%s''E"%(tuple(map(randrange, [60,60]))), (20,50), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
        cv2.putText(frame,"ALTITUDE: %s m"%(randrange(120,130)/10.0), (20,70), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
        cv2.putText(frame,"SPEED: %s ms2"%(randrange(430,440)/10.0), (20,90), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
        cv2.putText(frame,"AUTOPILOT: DISENGAGED", (20,110), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))

        # Show the image and wait 0.04 seconds to continue the loop. If the Esc key is pressed, quit.
        cv2.imshow('image',frame)
        save.write(frame)
        key=cv2.waitKey(40)
        if key==27:
            break
