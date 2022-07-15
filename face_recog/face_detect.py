import cv2 as cv
 
img = cv.imread('Images\group2.jpg')
cv.imshow('group of people' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray people' , gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')


faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor = 1.2, minNeighbors = 3)

print(f'number of faces found ={len(faces_rect)}')

# to draw rectangle over the face 
for (x,y,w,h) in faces_rect:
    cv.rectangle(img , (x,y) ,(x+w,y+h) , (0,255,0) , thickness = 2 )
    
cv.imshow('detected faces' , img)

cv.waitKey(0)