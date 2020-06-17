#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import required libraries
import cv2
from random import randint            # this is to generate a random number which will be used to save the output image
import matplotlib.pyplot as plt       # to display images


# In[2]:


img = cv2.imread("image1.jpg")
# plt.imshow(img)
cv2.imshow("Original Image", img)



# In[3]:


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to gray scale
#plt.imshow(gray)
cv2.imshow("Grayed Image", gray)



# In[4]:


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')   # Algorithm to detect frontal face
faces = face_cascade.detectMultiScale(gray, 1.3,5) # deploying algorithm on our image to detect face


# In[5]:


count = 0 # set a counter to count the face detected
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 4)                              # add rectange on faces
    count = count+1 # update count
cv2.putText(img, str(count),(0,200), cv2.FONT_ITALIC, 2,(0,0,0),2,cv2.LINE_AA)         # adding the count text on image

result_image = ('result_image ' + str(randint(0,100)) + '.jpg')     # output image name set up using random number between 0 - 100 and set output as .jpg
cv2.imwrite(result_image, img)                                      # save the output image
print("Total number of faces in image: ", count)
#plt.imshow(img)
cv2.imshow("Output Image", img)
cv2.waitKey(0)                          # enter esc to continue the code
cv2.destroyAllWindows()                 # to close all windows

