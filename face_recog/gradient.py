import cv2 as cv
import numpy as np 

img = cv.imread('Images\park.jpeg')
cv.imshow('park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

#laplacian method  

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian' , lap)


# Sobel 

sobelx = cv.Sobel(gray , cv.CV_64F , 1 ,0)
sobely = cv.Sobel(gray , cv.CV_64F , 0 ,1)
combined_sobel = cv.bitwise_or(sobelx , sobely)



cv.imshow('Sobel X' , sobelx) # --> computed along the y axis 
cv.imshow('Sobel Y' , sobely) # -- computed along the x axis
cv.imshow('conbined_sovel' , combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('canny' , canny)

cv.waitKey(0)