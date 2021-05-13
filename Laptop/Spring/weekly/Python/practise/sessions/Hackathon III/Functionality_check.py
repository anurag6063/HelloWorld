import base64
from exp_recognition import *
from face_recognition import *
from utils import *
def encode_image(file_name):
	with open(file_name, "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
	return encoded_string

area_threshold = 2000
TRAINSET = "haarcascade_frontalface_default.xml"
DOWNSCALE = 4
webcam = cv2.VideoCapture(0)
cv2.namedWindow("preview")
classifier = cv2.CascadeClassifier(TRAINSET)
img_counter = 0
if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False

if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False


while rval:
	try:
	    minisize = (int(frame.shape[1]/DOWNSCALE), int(frame.shape[0]/DOWNSCALE))
	    miniframe = cv2.resize(frame, minisize)
	    faces = classifier.detectMultiScale(miniframe)
	    face_cropped = get_large_face(miniframe, faces, area_threshold)
	    for f in faces:
	        print(f)
	        x, y, w, h = [ v*DOWNSCALE for v in f ]
	        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255))
	        if w*h >= area_threshold and isinstance(face_cropped, np.ndarray):
	        	cv2.imwrite('VC_image.png',miniframe)
	        	expression = get_expression(encode_image('VC_image.png'))
	        	face_c = get_face_class(encode_image('VC_image.png'))
	        	print(expression, face_c)
	       	cv2.putText(frame, expression, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
	       	cv2.putText(frame, face_c, (x, y+h),
	                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
	    cv2.putText(frame, "Press ESC to close.", (5, 25),
	                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
	    cv2.imshow("preview", frame)
	    # get next frame
	    rval, frame = webcam.read()

	    key = cv2.waitKey(20)
	    if key in [27, ord('Q'), ord('q')]: # exit on ESC
	        break
	except:
		continue