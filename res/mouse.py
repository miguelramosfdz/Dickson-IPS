import cv2
import numpy

def is_rect_nonzero(r):
    (minx,miny,maxx,maxy) = r
    return (maxx-minx > 0) and (maxy-miny > 0)

class CamShiftDemo:

    def __init__(self):
        self.capture = cv2.VideoCapture(1)
        cv2.namedWindow( "CamShiftDemo", 1 )
        cv2.namedWindow( "Histogram", 1 )
        cv2.setMouseCallback( "CamShiftDemo", self.on_mouse)

        self.drag_start = None      # Set to (x,y) when mouse starts drag
        self.track_window = None    # Set to rect when the mouse drag finishes

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
            self.selection = (xmin, ymin, xmax, ymax)

    def run(self):
        #hist = cv.CreateHist([180], cv.CV_HIST_ARRAY, [(0,180)], 1 )
        backproject_mode = False
        while True:
            rval, frame = self.capture.read()

            # Convert to HSV and keep the hue
            #hsv = cv.CreateImage(cv.GetSize(frame), 8, 3)
            hsv = numpy.zeros( [frame.shape[0],frame.shape[1], 0], numpy.int8)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Compute back projection
            #backproject = cv.CreateImage(cv.GetSize(frame), 8, 1)
            backproject = numpy.zeros( [frame.shape[0],frame.shape[1], 0], numpy.int8)

            # Run the cam-shift
            #cv.CalcArrBackProject( [self.hue], backproject, hist )
            if self.track_window and is_rect_nonzero(self.track_window):
                
                contours,hierarchy=cv2.findContours(hsv,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
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
                        box = numpy.int0(box)
                        #if(height>0.9*width and height<1.1*width):
                        print(box)
                        cv2.drawContours(frame,[box], 0, (255, 0, 0), 2)



            #    crit = ( cv.CV_TERMCRIT_EPS | cv.CV_TERMCRIT_ITER, 10, 1)
            #    (iters, (area, value, rect), track_box) = cv.CamShift(backproject, self.track_window, crit)
            #    self.track_window = rect
            

            # If mouse is pressed, highlight the current selected rectangle
            # and recompute the histogram

            if self.drag_start and is_rect_nonzero(self.selection):
                x1,y1,x2,y2 = self.selection
                sub = frame[x1:x2, y1:y2]
                save=sub.copy()
                #frame = cv2.resize(frame, (frame.shape[0]/2, frame.shape[1]/2))
                x1,y1,x2,y2 = self.selection
                cv2.rectangle(frame, (x1,y1), (x2,y2), (255,255,255))

            #elif self.track_window and is_rect_nonzero(self.track_window):
                #cv.EllipseBox( frame, track_box, cv.CV_RGB(255,0,0), 3, cv.CV_AA, 0 )

            if not backproject_mode:
                cv2.imshow( "CamShiftDemo", frame )
            else:
                cv2.imshow( "CamShiftDemo", backproject)

            c = cv2.waitKey(7)
            if c == 27:
                break
            elif c == ord("b"):
                backproject_mode = not backproject_mode

if __name__=="__main__":
    demo = CamShiftDemo()
    demo.run()
