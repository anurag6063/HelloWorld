import cv2
import numpy as np
import os
def save_faces(miniframe, exp, area_threshold, img_counter, folder):
    TRAINSET = "lbpcascade_frontalface.xml"
    classifier = cv2.CascadeClassifier(TRAINSET)
    faces = classifier.detectMultiScale(miniframe)
    Image = get_large_face(miniframe, faces, area_threshold)
    if not isinstance(Image, np.ndarray):
        return "DonotSave"
    img_name = "{}_{}.png".format(exp, img_counter)
    if os.path.exists(folder+exp):
        cv2.imwrite(folder+exp+'/'+img_name, Image)
    else :
        os.mkdir(folder+exp)
        cv2.imwrite(folder+exp+'/'+img_name, Image)
    return img_name



def get_large_face(miniframe, faces, area_threshold):
    images = []
    face_areas = []
    required_image = 0
    for x,y,w,h in faces:
        #miniframe[y:y+h, x:x+w]
        face_cropped = miniframe[y:y+h, x:x+w]
        face_areas.append(w*h)
        images.append(face_cropped)
        required_image = images[np.argmax(face_areas)]
    if not face_areas:
        return 0
    if face_areas[np.argmax(face_areas)] < area_threshold:
        return 0
    #required_image = Image.fromarray(required_image)
    return required_image