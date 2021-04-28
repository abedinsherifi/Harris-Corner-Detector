"""
Abedin Sherifi
RBE595
09/25/2020
"""

"""
Harris Corner Detection on Video Stream
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Open computer webcam
capture = cv2.VideoCapture(0)

#Open manually if it fails to open initially.
if not(capture.isOpened()):
    capture.open()

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') 
videoWriter = cv2.VideoWriter('Harris_Corner_Detection_Video.mp4', fourcc, 10.0, (640, 480))

while(True):
    #Capture frame-by-frame
    ret, current_frame = capture.read()
    if type(current_frame) == type(None):
        print("!!! Couldn't read frame!")
        break

    #Reading input current frame and converting it from BGR to Gray.
    gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    R = np.zeros(gray.shape)

    #Gaussian filter applied with a 9 by 9 kernel and sigmax and sigmay of 3.
    gray = cv2.GaussianBlur(gray,(9,9),3)

    #This step gets the Y and X gradients using sobel filter with kernel size of 9 by 9. 
    Ix = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=9) 
    Iy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=9)

    #This step gives the product of the gradient components for the Matrix M.
    Ix_2 = cv2.GaussianBlur(np.multiply(Ix, Ix),(9,9),3) 
    Iy_2 = cv2.GaussianBlur(np.multiply(Iy, Iy),(9,9),3)  
    IxIy = cv2.GaussianBlur(np.multiply(Ix, Iy),(9,9),3)

    #This step calculates the corner response matrix. 
    k = 0.06
    R = np.multiply(Ix_2,Iy_2)-np.square(IxIy)-k*np.square(Ix_2+Iy_2)

    #This step determines the corners. Threshold is chosen as 0.5% of maximum value. If value is larger than this threshold, then result is a corner. This step performs maximum suppression. 
    max_Value = 0.005*R.max()
    counter = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    for row_n,row in enumerate(R):
        for col_n,col in enumerate(row):
            if col > max_Value:
                current_frame[row_n,col_n] = [0,255,255]
                counter = counter + 1 
            else: 
                pass
    print("Counter", counter)
    #Display the resulting frame
    count_text = "Corner Detected %s" % str(counter)
    cv2.putText(current_frame, count_text, (0, 30), font, 1, (0, 0, 255), 2, cv2.LINE_4)
    cv2.imshow('Video Frame',current_frame)
    videoWriter.write(current_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the capture
capture.release()
videoWriter.release()
cv2.destroyAllWindows()

