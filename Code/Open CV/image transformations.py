# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:19:33 2022

@author: techv
"""

import cv2 as cv
import numpy as np

img  = cv.imread("images/Cat.jpg")
cv.imshow("img",img)

def translate(img,x,y):
    transMat = np.array([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0]) #[1] --> width, [2] ---> height
    return cv.wrapAffine(img, transMat, dimensions)

translate = 

cv.waitKey(0)
cv.destroyAllWindows()