import cv2
import numpy as np
lower = np.array([25, 114, 121])#Define HSV Range
upper=np.array([71, 255, 210])
capture = cv2.VideoCapture("Video 3.mp4")#Read File 
output = cv2.VideoWriter("Output3.mp4",cv2.VideoWriter_fourcc(*'mp4v'),30,(1280,720))#Save file
while capture.isOpened():
    _,frame = capture.read()
    if _ != True:
        break
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    img = cv2.inRange(img,lower,upper)#Find the points in the HSV Range
    contours = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = contours[0]
    try:
        for i in cnts:
            #Calculate moments of binary image
            M=cv2.moments(np.array(i))
            if M['m00']>0:
                #Calculate x,y coordinates of centre
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                #Highlight the center
                cv2.circle(frame,(cx,cy),2,(0,0,255),2)
    except Exception:
        print("error")
    frame = cv2.resize(frame, (1280, 720))
    cv2.imshow("video",frame)
    output.write(frame)
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
capture.release()
output.release()
cv2.destroyAllWindows()