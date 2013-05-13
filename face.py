import cv2
import numpy

class FaceDetector:

    HAAR_CASCADE_PATH_DEF = "haarcascade_frontalface_default.xml"
    HAAR_CASCADE_PATH_ALT = "haarcascades_haarcascade_frontalface_alt.xml"
    LBP_CASCADE_PATH = "lbpcascade_frontalface.xml"

    def __init__(self, type):
        if type == 1:
            self.cascade_path = self.HAAR_CASCADE_PATH_DEF
        elif type == 2:
            self.cascade_path = self.HAAR_CASCADE_PATH_ALT
        else:
            self.cascade_path = self.LBP_CASCADE_PATH
        self.cascade = cv2.CascadeClassifier(self.cascade_path)

    def detect_faces(self, image):
        faces = []
        detected = self.cascade.detectMultiScale(image, 1.2, 2, cv2.CASCADE_DO_CANNY_PRUNING, (100,100))
        if type(detected) is numpy.ndarray:
            for (x,y,w,h)in detected:
                faces.append((x,y,w,h))
        return faces

if __name__ == '__main__':
    capture = cv2.VideoCapture(0)
    detector = FaceDetector(0)
    faces = []

    if capture.isOpened():
        returnValue, image = capture.read()
    else:
        returnValue = False;

    while returnValue:
        framegray = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)
        
        faces = detector.detect_faces(image)

        for (x,y,w,h) in faces:                     
            cv2.rectangle(framegray, (x,y), (x+w,y+h), 255)  
            print 'detected' 
        
        cv2.imshow("test", framegray)
        returnValue, image = capture.read()