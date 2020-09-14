import numpy as numpy
import cv2

captured_frame = cv2.VideoCapture(0)
#print(cv2.__version__)

#append all 80 types of objects detectable by coco in this list
class_names = list()
with open('coco.names', 'rt') as coco_names:
    class_names = coco_names.read().rstrip("\n").split("\n")
#print(class_names)

while(True):
    success, image = captured_frame.read()

    #cv2.imshow("Image", image)
    cv2.waitKey(1)