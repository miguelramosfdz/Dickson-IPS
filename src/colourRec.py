import cv2
import numpy as np
import colourValues

lower=np.array(colourValues.down,np.uint8)
upper=np.array(colourValues.up,np.uint8)

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

webcam = cv2.VideoCapture(0)
while True:
    rval, im = webcam.read()
    frame=cv2.flip(im,1,0)
    img=cv2.GaussianBlur(frame, (5,5), 0)
    img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    separated=cv2.inRange(img,lower,upper)
    contours,hierarchy=cv2.findContours(separated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    max_area = 0
    largest_contour = None
    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > max_area and area > 1000:
            max_area = area
            largest_contour=contour


    if largest_contour != None:
        M = cv2.moments(largest_contour)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        cv2.circle(frame,(cx,cy),2,255,5)
        rect = cv2.minAreaRect(largest_contour)
        rect = ((rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
        box = np.int0(cv2.cv.BoxPoints(rect))
        cv2.drawContours(frame,[box], 0, (255, 0, 0), 2)

    cv2.imshow('image',frame)
    key=cv2.waitKey(10)
    if key==27:
        break
