import cv2 as cv

img = cv.imread('Images\car3.jpg')

cv.imshow('Cat', img )

# converting img to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('GRAY' , gray)

# blur an image 

blur = cv.GaussianBlur(img , (7,7) , cv.BORDER_DEFAULT)
cv.imshow("Blur" , blur)



#create Edge cascade
canny = cv.Canny(img , 125 , 175) # to reduce or get rid of edges we use blur 
cv.imshow('canny' , canny)

# dilating the image 

dilated = cv.dilate(canny , (7,7) , iterations = 3)
cv.imshow('Dilated' , dilated)


#eroding 

eroded = cv.erode(dilated , (7,7) , iterations = 1)
cv.imshow('Eroded', eroded)


#resize 

resize = cv.resize(img , (500,500) , interpolation  = cv.INTER_CUBIC)
cv.imshow('resized' , resize)

#cropping 

cropped = img[50:200 , 200:400]
cv.imshow("cropped" , cropped)

cv.waitKey(0)