import cv2
import numpy as np
from utils import *
from PIL import Image
import os

area_threshold = 2304
images_required = 100


classes = ['ANGER', 'DISGUST', 'FEAR', 'HAPPINESS', 'NEUTRAL', 'SADNESS', 'SURPRISE']

TRAINSET = "lbpcascade_frontalface.xml"
DOWNSCALE = 4

webcam = cv2.VideoCapture(0)
cv2.namedWindow("preview")
classifier = cv2.CascadeClassifier(TRAINSET)
img_counter = 0

if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False
#print((int(frame.shape[1]/DOWNSCALE), int(frame.shape[0]/DOWNSCALE)))

for expression in classes:
    img_counter = 0
    while rval:

        # detect faces and draw bounding boxes
        minisize = (int(frame.shape[1]/DOWNSCALE), int(frame.shape[0]/DOWNSCALE))
        miniframe = cv2.resize(frame, minisize)
        
        cv2.putText(frame, "Put the expression {} and hit space to save the image".format(expression), (5, 25),
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
                img_name = save_faces(miniframe, expression, area_threshold, img_counter, 'captured_images_with_Expression/')
                if img_name == 'DonotSave' :
                    continue
                print("{} written!".format(img_name))
                img_counter += 1


            if k in [27, ord('Q'), ord('q')]: # exit on ESC
                break
        except :
            continue

