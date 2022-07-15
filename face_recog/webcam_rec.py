import cv2 

haar_casscade = cv2.CascadeClassifier('haar_face.xml')
capture = cv2.VideoCapture(0)

while True:
    isTrue , img = capture.read()
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    
    faces = haar_casscade.detectMultiScale(gray , 1.1 , 4)
    
    for(x,y,w,h) in faces:
        cv2.putText(img , 'face' , (100,60) , cv2.FONT_HERSHEY_COMPLEX , 1.0 , (0,255,0) , thickness=2)
        cv2.rectangle(img , (x,y) , (x+w , y+h) , (0,255,0), 2)
        
    cv2.imshow('img' , img)
    
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    
    
capture.release()