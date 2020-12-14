# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:25:31 2020

@author: panindra
"""
import numpy as np
import cv2

img = cv2.imread('./test5.png')
#cv2.imshow("img",img)

## Masking is filtering the color channels  

#Red Mask 
lower_red = np.array([[0,50,50]]) 
upper_red = np.array([[10,255,255]]) 
 
# green mask
lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255,255])

# Blue mask
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

#convert image to hsv
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) 
## Apply red mask to filter only red
mask = cv2.inRange(hsv, lower_red, upper_red)

## Apply filters on green
mask_green = cv2.inRange(hsv, lower_green, upper_green)

#apply filters on blue
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
print(mask)




result = cv2.bitwise_and(img, img, mask = mask) 
result_green = cv2.bitwise_and(img, img, mask = mask_green)
result_blue = cv2.bitwise_and(img, img, mask = mask_blue)  
cv2.imshow("Red Filter",result)
cv2.imshow("Green Filter",result_green)
cv2.imshow("Blue Filter",result_blue)
#while True:
cv2.waitKey(1000)
        
                   