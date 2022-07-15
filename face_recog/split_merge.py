import cv2 as cv
import numpy as np

img = cv.imread('Images\park.jpeg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2] , dtype = 'uint8')


b,g,r = cv.split(img)

# distribution of images in their original colour channel

blue = cv.merge([b ,blank , blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue' , blue)
cv.imshow('Green', green)
cv.imshow('Red' , red)



# cv.imshow('blue', b)
# cv.imshow('green', g)
# cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)



merged = cv.merge([b,g,r])
cv.imshow('merged_image', merged)

cv.waitKey(0)