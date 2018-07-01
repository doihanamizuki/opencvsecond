import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('colorchange') # create win with win name

cv2.createTrackbar('red', 'colorchange',  0, 100, myfunc) # callback func
cv2.createTrackbar('green', 'colorchange',  0, 100, myfunc) # callback func
cv2.createTrackbar('blue', 'colorchange',  0, 100, myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue
    frame = frame/255
    r = cv2.getTrackbarPos('red', 'colorchange')*0.01# of the win
    frame[:,:,2] *= r
    g = cv2.getTrackbarPos('green', 'colorchange')*0.01# of the win
    frame[:,:,1 ]*= g
    b = cv2.getTrackbarPos('blue', 'colorchange')*0.01# of the win
    frame[:,:,0] *= b

    cv2.imshow('colorchange', frame)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
