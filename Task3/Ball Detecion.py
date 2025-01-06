import cv2 as cv
import numpy as np

vid = cv.VideoCapture('Ball_Tracking.mp4')

while vid.isOpened():
    ret, frame = vid.read()

    if not ret:
        break

    lower_range = np.array([40, 40, 40])
    upper_range = np.array([80, 255, 255])
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    masked_image = cv.inRange(frame_hsv, lower_range, upper_range)
    contours, hierarchy = cv.findContours(masked_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, width, height = cv.boundingRect(max(contours, key=cv.contourArea))
        cv.circle(frame, (int(x+(width/2)),int(y+(height/2))), int((width+height)/4), (255,0,0),2)
        #cv.rectangle(frame, (x ,y) ,(x+width ,y+height),(255,0,0),2)
    
    cv.imshow("Ball Tracking",frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
