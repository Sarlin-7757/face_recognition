import cv2 as cv

#reading images 

img = cv.imread(('Images/car3.jpg'))

cv.imshow('Cat', img)

cv.waitKey(0)


# reading videos

capture = cv.VideoCapture('videos/Dog1.mp4') # capture is the instance of the VideoCapture Class 

while True:
    isTrue, frame = capture.read() # we gramp the video frame by frame using capture.read() method 
    cv.imshow('Video' , frame) # to display the video frame by frame.(to display each frame of video) 

    if cv.waitKey(20) & 0xFF==ord('d'): #to stop the video play indefinitly  (press d)
        break

capture.release()
cv.destroyAllWindows()

# (-215:Assertion failed) -- basically means that the program cannot find the frame at that specific location so it comes automatically out of the while loop 
