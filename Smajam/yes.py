import cv2
import numpy as np


image = cv2.imread("apple.jpg")                
# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define blue color range
light_blue = np.array([254,132,132])
dark_blue = np.array([107,0,0])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, light_blue, dark_blue)

# Bitwise-AND mask and original image
output = cv2.bitwise_and(image,image, mask= mask)
    
cv2.imshow("Color Detected", np.hstack((image,output)))
cv2.waitKey(0)
cv2.destroyAllWindows()