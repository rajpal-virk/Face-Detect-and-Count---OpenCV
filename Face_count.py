#!/usr/bin/env python
# coding: utf-8

# Import required libraries
import cv2
from random import randint            # this is to generate a random number which will be used to save the output image

# Load Image
img = cv2.imread("image1.jpg")
cv2.imshow("Original Image", img)

# Convert Image to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow("Grayed Image", gray)

# Haar Cascade Algorithm to detect frontal face
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Deploying Haar Cascade algorithm 
faces = face_cascade.detectMultiScale(gray, 1.3,5)

# set a counter to count the face detected
count = 0

# Add and Count Bounding boxes
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 4)
    count = count+1

# Add count to image
cv2.putText(img, str(count),(0,200), cv2.FONT_ITALIC, 2,(255,255,255),2,cv2.LINE_AA)


# output image name set up using random number between 0 - 100 and set output as .jpg
result_image = ('result_image ' + str(randint(0,100)) + '.jpg')     

# save the output image
cv2.imwrite(result_image, img)

# Print output
print("Total number of faces in image: ", count)
cv2.imshow("Output Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

