import cv2 as cv 
import numpy as np 

# to create a dummy/blank image 

blank = np.zeros((500,500,3) , dtype='uint8')  #(height,width,num of colour channels)
cv.imshow("Blank" , blank)

# paint the image in certain colour 

blank[200:300 , 300:400] = 0,0,255
cv.imshow("Green" , blank)

# (blank.shape[1]//2 , blank.shape[0]//2),   this line means to divide the taken area in half

# draw a rectangle

cv.rectangle(blank , (0,0) , (250,250) , (0,255,0) , thickness= cv.FILLED)
cv.rectangle(blank , (0,0) , (blank.shape[1]//2 , blank.shape[0]//2), (0,255,0) , thickness= 2)
cv.imshow('Rectangle', blank)



#draw a circle

cv.circle(blank , (blank.shape[1]//2 , blank.shape[0]//2) , 40 ,(0,0,255), thickness=3)
cv.imshow('Circle' , blank)


#draw a line 

cv.line(blank , (100,250) ,(300,400), (255,255,255) , thickness= 2)
cv.imshow('Line' , blank) 


#write text in an image 

cv.putText(blank, 'Hello,my name is saransh', (0,225) , cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0,255,0) , thickness= 2)
cv.imshow("Text" ,blank)


cv.waitKey(0)