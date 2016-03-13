import cv2 as cv
import numpy as np
import sys


if __name__ == '__main__':
    
    img = cv.imread(sys.argv[1])
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    filtered_gray = cv.medianBlur(gray,5)
    #filtered_gray = cv.GaussianBlur(gray,(5,5),0)
    #filtered_gray = gray
    '''
           circles - output vector of found circles (x,y,r)
           method - CV_HOUGH_GRADIENT
           dp - inverse ratio of the accumulator resolution
           minDist - min dist between the centers of the detected circles
           param1 - the higher threshold of the two passed to the Canny() edge detector (the lower is twice smaller)
           param2 - the smaller it is? the more false circles may be detected
           minRadius
           maxRadius
    '''
    circles = cv.HoughCircles(filtered_gray,cv.HOUGH_GRADIENT,1,25,
                                    param1=200,param2=22,minRadius=10,maxRadius=25)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(img,(i[0],i[1]),i[2],(0,255,0),1)
            # draw the center of the circle
            cv.circle(img,(i[0],i[1]),2,(0,0,255),2)
    cv.imshow('detected circles',img)
    cv.waitKey()
    name_ext = sysy.argv[1].split('.')
    cv.imwrite(name_ext[0] + '1.' + name_ext[1], img)
    cv.destroyAllWindows()