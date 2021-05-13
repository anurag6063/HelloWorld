import cv2
import numpy as np
from PIL import Image
from utils import *
import os
import sys

area_threshold = 2304
images_required = 100


classes = ['Person1', 'Person2', 'Person3', 'Person4', 'Person5', 'Person6', 'Person7']


DOWNSCALE = 4
webcam = cv2.VideoCapture(0)
cv2.namedWindow("preview")
img_counter = 0

if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False
#print((int(frame.shape[1]/DOWNSCALE), int(frame.shape[0]/DOWNSCALE)))

for person in classes:
    img_counter = 0
    while rval:

        # detect faces and draw bounding boxes
        minisize = (int(frame.shape[1]/DOWNSCALE), int(frame.shape[0]/DOWNSCALE))
        miniframe = cv2.resize(frame, minisize)
        
        cv2.putText(frame, "Subject : {} , show up and hit space to save the image".format(person), (5, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
        cv2.imshow("Training Images", frame)
        # get next frame
        rval, frame = webcam.read()
        if img_counter > images_required:
            break
        if not rval:
            breaka
        k = cv2.waitKey(1)
        try :
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = save_faces(miniframe, person, area_threshold, img_counter, 'captured_face_images/')
                if img_name == 'DonotSave' :
                    continue
                print("{} written!".format(img_name))
                img_counter += 1


            if k in [27, ord('Q'), ord('q')]: # exit on ESC
                break
        except :
            continue

