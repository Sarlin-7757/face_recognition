import cv2 as cv

img = cv.imread('Images\car3.jpg')
cv.imshow('cats' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

#simple thresholding  ---> manually set the threshold value 
threshold , thresh = cv.threshold(gray,150,255, cv.THRESH_BINARY)
cv.imshow('simple thresholded ' , thresh)

# all white parts will change to black and vice versa
threshold , thresh_inv = cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)
cv.imshow('simple thresholded inverse ' , thresh_inv)


#Adaptive thresholding --> computed the optimal threshold value on the basis of mean or on the basis of gaussian distribution 

adaptive_thres = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY_INV, 11 , 9)
cv.imshow('Adaptive thresholding', adaptive_thres)

cv.waitKey(0)