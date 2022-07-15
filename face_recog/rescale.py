# resizind and reshaping 

import cv2 as cv

img =cv.imread('Images\car3.jpg')
cv.imshow('Cat' , img)

def rescaleFrame(frame , scale=0.75): #scale the value down to .75
    #this method can be used for videos , images and live videos 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]* scale)
    
    dimensions = (width, height)

    return cv.resize(frame , dimensions , interpolation = cv.INTER_AREA)

# reading images
resized_image = rescaleFrame(img)

cv.imshow('Image' , resized_image)

# change resolution for live video 
def changeRes(width,height):
    # this method can be used only for live videos and not for alredy existed videos  
    capture.set(3,width) # 3 refers to width 
    capture.set(4,height) # 4 refers to height these are inbuilt methods 


# reading videos
capture = cv.VideoCapture('videos/Dog1.mp4') 

while True:
    isTrue, frame = capture.read() 
    
    frame_resized = rescaleFrame(frame , scale=.75)

    cv.imshow('Video' , frame) 
    cv.imshow('Video Resized' , frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'): 
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
