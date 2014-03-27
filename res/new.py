import cv2
import sys
import numpy as np

webcam = cv2.VideoCapture(1)

cv2.namedWindow('image')
cv2.setMouseCallback('image',on_mouse)



def on_mouse(self, event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        self.drag_start = (x, y)
    if event == cv2.EVENT_LBUTTONUP:
        self.drag_start = None
        self.track_window = self.selection
    if self.drag_start:
        xmin = min(x, self.drag_start[0])
        ymin = min(y, self.drag_start[1])
        xmax = max(x, self.drag_start[0])
        ymax = max(y, self.drag_start[1])
        self.selection = (xmin, ymin, xmax - xmin, ymax - ymin)


while True:
    rval, im = webcam.read()
    frame=cv2.flip(im,1,0)
    img=cv2.GaussianBlur(frame, (5,5), 0)
    img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower=np.array(lowers[ind],np.uint8)
    upper=np.array(uppers[ind],np.uint8)
    separated=cv2.inRange(img,lower,upper)
    contours,hierarchy=cv2.findContours(separated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    largest_contour = None
    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour=contour
    if largest_contour != None:
        moment = cv2.moments(largest_contour)
        if moment["m00"] > 1000:
            rect = cv2.minAreaRect(largest_contour)
            rect = ((rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
            (width,height)=(rect[1][0],rect[1][1])
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            #if(height>0.9*width and height<1.1*width):
            print(box)
            cv2.drawContours(frame,[box], 0, (255, 0, 0), 2)


    if self.drag_start and is_rect_nonzero(self.selection):
            sub = cv.GetSubRect(frame, self.selection)
            save = cv.CloneMat(sub)
            cv.ConvertScale(frame, frame, 0.5)
            cv.Copy(save, sub)
            x,y,w,h = self.selection
            cv.Rectangle(frame, (x,y), (x+w,y+h), (255,255,255))

            sel = cv.GetSubRect(self.hue, self.selection )
            cv.CalcArrHist( [sel], hist, 0)
            (_, max_val, _, _) = cv.GetMinMaxHistValue( hist)
            if max_val != 0:
                cv.ConvertScale(hist.bins, hist.bins, 255. / max_val)



    cv2.imshow('b',frame)
    cv2.imshow('a',separated)
    key=cv2.waitKey(10)
    if key==27:
        break

