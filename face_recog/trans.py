# IMAGE TRANSFORMATIONs


import cv2 as cv
import numpy as np

img = cv.imread('Images/car3.jpg')

cv.imshow('Cat' , img)
#translate function 

def translate(img , x , y):
    transMAT = np.float32([[1,0,x] , [0,1,y]]) # store as a MATRIX
    dimensions = (img.shape[1] , img.shape[0])   #img.shape[1] - width and img.shape[0] - height 
    return cv.warpAffine(img , transMAT , dimensions)


# (-x val) implies  ----> left shift  
# (-y val) implies ---> up shift 
# (+x val) implies ---> right shift 
# (-y val) implies -----> down shift

translated = translate(img , -100 , -100 )
cv.imshow('translated' , translated)


#rotation 

def rotate(img, angle , rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2 , height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint , angle , 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img , rotMat , dimensions)

rotated  = rotate(img, 45)
cv.imshow('rotate' , rotated)

rotated_rotated = rotate(rotated , -90)
cv.imshow("rotated_rotated" , rotated_rotated)


#resizing

resized  = cv.resize(img , (500 , 500 ) , interpolation = cv.INTER_CUBIC) # INTER_CUBIC AND LINEAR for enlarging image and INTER_AREA for shrinking image 
cv.imshow('resize' , resized)

#fliping 

flip = cv.flip(img , -1) # flip it vertically - 0  flip horizontally - 1 to flip both vertically and horizontally - (-1)
cv.imshow('flip' , flip)


#cropping 

cropped = img[200:400 , 300:400]
cv.imshow("cropped" , cropped)

cv.waitKey(0)

