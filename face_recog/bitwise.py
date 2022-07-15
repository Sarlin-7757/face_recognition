import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# bitwise and
# return the intersection or common region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)

# bitwise or

# put together and get the result also can be said both interescting and non-intersecting region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)

# bitiwse xor

bitwise_xor = cv.bitwise_xor(rectangle,circle) # gives the non intersecting part 
cv.imshow('bitwise_xor' , bitwise_xor)

# bitwise not

bitwise_not = cv.bitwise_not(rectangle) #invert the white pixels to black and black to white 
cv.imshow('bitwise_not' , bitwise_not) 

cv.waitKey(0)
