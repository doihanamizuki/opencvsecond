import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('filter') # create win with win name

cv2.createTrackbar('value gradient', # name of value
                   'filter', # win name
                   0, # min
                   10, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue
	
    v = cv2.getTrackbarPos('value gradient', 'filter')*0.1
    kernel_gradient_3x3 = np.array([
                            [ v,  v,  v],
                            [ 0,  0,  0],
                            [-v, -v, -v]
                            ], np.float32)
    img_gradient_3x3 = cv2.filter2D(frame, -1, kernel_gradient_3x3)
    cv2.imshow('filter', img_gradient_3x3)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
