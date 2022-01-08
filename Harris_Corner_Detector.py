"""
Abedin Sherifi
"""

"""
Harris Corner Detection on an Image
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def Harris_Corner_Detector():

    #Reading input image through imread and converting image from BGR to Gray. 
    image_input = cv2.imread("Pic_Test.jpg") 
    image_input_gray = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY) 
    R = np.zeros(image_input_gray.shape) 

    #Gaussian filter applied with a 9 by 9 kernel and sigmax and sigmay of 3.
    image_input_gray = cv2.GaussianBlur(image_input_gray,(9,9),3)

    #This step gets the Y and X gradients using sobel filter with kernel size of 9 by 9. 
    Ix = cv2.Sobel(image_input_gray, cv2.CV_64F, 1, 0, ksize=9) 
    Iy = cv2.Sobel(image_input_gray, cv2.CV_64F, 0, 1, ksize=9)

    #This step gives the product of the gradient components for the Matrix M.
    Ix_2 = cv2.GaussianBlur(np.multiply(Ix, Ix),(9,9),3) 
    Iy_2 = cv2.GaussianBlur(np.multiply(Iy, Iy),(9,9),3)  
    IxIy = cv2.GaussianBlur(np.multiply(Ix, Iy),(9,9),3)   

    #This step calculates the corner response matrix. 
    k = 0.05
    R = np.multiply(Ix_2,Iy_2)-np.square(IxIy)-k*np.square(Ix_2+Iy_2)

    #This step determines the corners. Threshold is chosen as 0.5% of maximum value. If value is larger than this threshold, then result is a corner. This step performs maximum suppression. 
    corner_count = 0
    max_Value = 0.005*R.max()
    for row_n,row in enumerate(R):
        for col_n,col in enumerate(row):
            if col > max_Value:
                corner_count += 1
                image_input[row_n,col_n] = [0,255,255] 
            else: 
                pass

    font = cv2.FONT_HERSHEY_SIMPLEX
    count_text = "Corners Detected %s" % str(corner_count)
    cv2.putText(image_input, count_text, (0, 30), font, 1, (0, 0, 255), 2, cv2.LINE_4)
    cv2.imshow("Detected Corners", image_input)
    output_file = "Harris_Corners.png"
    cv2.imwrite(output_file, image_input)
    if cv2.waitKey(0) & 0xff == ord('q'):
    	cv2.destroyAllWindows()

if __name__ == "__main__":
    Harris_Corner_Detector()
