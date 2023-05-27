# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:38:26 2022

@author: techv
"""

import cv2 as cv
import numpy as np
import time 

#The sequence is BGR not RGB
#Black image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank Slate", blank)

#Green image
green = blank 
green[:] = 0,255,0
cv.imshow("Green Slate", green)

#Red image
red = blank
red[:] = 0,0,255
cv.imshow("Red Slate", red)

#Blue image
blue = blank
blue[:] = 255,0,0
cv.imshow("Blue Slate", blue)

# coloring part of the image
part = blank
part[150:300,325:350] = 0,255,0 ## ----> X axis and [Y, X]
cv.imshow("part color", part)


# Draw a rectangle 
rect = blank
cv.rectangle(rect, (0,0), (100,250), (0,255,0), thickness = 2)
cv.rectangle(rect, (100,250), (250,300), (0,255,0), thickness = cv.FILLED) # or -1 ## to fill the rectangle with bold
cv.imshow("rectangle",rect)


# cv.circle(blank, (x,y), (B,G,R), thickness)
# cv.line(blank, (x,y),(x1,y1), (B,G,R), thickness)
# cv.putText(blank, 'Hello', (225,255), cv.FONT_HERSHEY_DUPLEX, 1.0, (B,G,R), thickness)

cv.waitKey(0)
cv.destroyAllWindows() 
cv.waitKey(1)
