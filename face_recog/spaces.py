import cv2 as cv

import matplotlib.pyplot as plt

img = cv.imread('Images\car3.jpg')

cv.imshow('Cat' , img)

# plt.imshow(img)
# plt.show()


#BGR to GRAYSCALE

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

# BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv' , hsv)

# BGR to L*a*b
lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)


# BGR to RGB

rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)
cv.imshow('RGb' , rgb)

# HSV to BGR

hsv_bgr = cv.cvtColor(img , cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR' , hsv_bgr)


#lab to BGR

lab_bgr = cv.cvtColor(img , cv.COLOR_LAB2BGR)
cv.imshow('LAB-->BGR' , lab_bgr)





cv.waitKey(0)