import cv2 as cv

img = cv.imread('Images\park.jpeg')
cv.imshow('Park', img)

# averaging

average = cv.blur(img, (3, 3))  # (7,7) kernel size ---> more blur
cv.imshow('average_blur', average)

# gaussian blur -- > more natural  --->  a certain weight is given to the pixels surrounding the centre while computing

gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('gaussin_blur', gauss)


#median blur --> same thing as average except we find the median instead of average of surrounding pixels.
median = cv.medianBlur(img , 3) # here 7 is kernel size but not a tuple as it will be automatically assumed by the openCV
cv.imshow('median_show' , median)


#bilateral blurring --> it blurs the image but retains the edges

bilat = cv.bilateralFilter(img, 10, 35 , 25)
cv.imshow('bilateral', bilat)

cv.waitKey(0)
