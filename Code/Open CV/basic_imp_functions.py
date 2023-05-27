# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:18:15 2022

@author: techv
"""

import cv2 as cv

#Reading an Image 
img = cv.imread("images/cat.jpg")
cv.imshow('Cat',img)

#Converting to Gray Scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blurring an Image (to remove noise form an image)
#Guassian Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # the kernel must be ODD not EVEN
cv.imshow('blurred',blur)

#Edge Cascade
canny = cv.Canny(img, 100,175)
cv.imshow('Canny 100',canny)

# canny = cv.Canny(blur, 100,175)
# cv.imshow('Canny 100 blur',canny)

#Dilating the image
dilate = cv.dilate(canny, (7,7), iterations = 3)
cv.imshow('Dilate', dilate)

#Eroding
erode = cv.erode(dilate,(7,7), iterations = 5)
cv.imshow('Erode', erode)

#resize and crop the image
resize = cv.resize(img, (500,500))
cv.imshow('Resized',resize)
# cv.resize(image, (X,Y), interpolation)

# interpolation = cv.INTER_AREA   #For scling down the image
# interpolation = cv.INTER_LINEAR #for scaling up the image with lower resolution
# interpolation = cv.INTER_CUBIC  #for scaling up the image with higher reslution more time consuming

#Cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
cv.destroyAllWindows()