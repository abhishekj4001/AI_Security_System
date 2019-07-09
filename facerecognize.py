#!/usr/bin/python

import face_recognition
import cv2
import pickle
import time
import os
import numpy as np

def face_recon(arg,arg1):
    path = "datasets"
#    camera_port = 0
#    camera = cv2.VideoCapture(camera_port)
#    __, im = camera.read() 
#    (width, height) = (130, 100)
#    haar_file = 'haarcascade_frontalface_default.xml'
#    face_cascade = cv2.CascadeClassifier(haar_file)
#    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
#    for (x,y,w,h) in faces:
#        cv2.rectangle(faces,(x,y),(x+w,y+h),(255,0,0),2)
#        face = gray[y:y + h, x:x + w]
#       face_resize = cv2.resize(face, (width, height))
    
    gray = cv2.cvtColor(arg, cv2.COLOR_BGR2GRAY)
    small_frame = cv2.resize(gray, (0, 0), fx=0.25, fy=0.25)
    cv2.imwrite("%s/%s.png" % (path,arg1), small_frame)

                                                                                                    

def face_identify(im):
    path = "datasets"
    name = "unknown"
    process_this_frame = True
    #    camera_port = 0
    #    camera = cv2.VideoCapture(camera_port)
    #    __, im = camera.read() 
#    (width, height) = (130, 100)
#    haar_file = 'haarcascade_frontalface_default.xml'
#    face_cascade = cv2.CascadeClassifier(haar_file)
#    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
#    for (x,y,w,h) in faces:
#        cv2.rectangle(faces,(x,y),(x+w,y+h),(255,0,0),2)
#        face = gray[y:y + h, x:x + w]
#        face_resize = cv2.resize(face, (width, height))
#        cv2.imwrite("%s.png" % (name), face_resize)
     
#    for  k in range(len(os.listdir(path))):
#        for filename in os.listdir(path):
#            path1 = path + '/' + filename
#        known_image = face_recognition.load_image_file(path1)
#        k = face_recognition.face_encodings(known_image)[0]
#        known_faces_encodings = []
#        known_faces_encodings.append(k)



    image1 = face_recognition.load_image_file("datasets/1.png")
    encoding1 = face_recognition.face_encodings(image1)[0]
    
    image2 = face_recognition.load_image_file("datasets/2.png")
    encoding2 = face_recognition.face_encodings(image2)[0]
    known_encodings = [encoding1, encoding2]
    
    face_locations = []
    face_encodings = []
    small_frame = cv2.resize(im, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding)

            if True in matches:
                return "Access Granted"
            else:
                return "Access Denied"



            
            
