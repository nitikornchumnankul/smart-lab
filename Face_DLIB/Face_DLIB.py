
import cv2
import numpy as np
import dlib
import pickle
import serial


serialPort = serial.Serial("/dev/ttyUSB0", 9600)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_reco_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
FACE_DESC,FACE_NAME = pickle.load(open('trainset.pk', 'rb'))
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def sw1Pressed():
    serialPort.write("SW1 Pressed".encode('utf-8'))
    
    
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face_reco_model:
        img = frame[y-10:y+h+10, x-10:x+w+10][:,:,::-1]
        dets = detector(img,1)
        
        for k, d in enumerate(dets): #วนหาว่ามีรูปอะไรบ้างใน​ dets ทุกหน้าที่เจอจะผ่านการ landmark
            shape = predictor(img, d) # d is bounding box
            face_desc0 = face_reco_model.compute_face_descriptor(img,shape,1)            
            d = []
            
            for face_desc in FACE_DESC:
                d.append(np.linalg.norm(np.array(face_desc) - np.array(face_desc0)))
            d = np.array(d)
            idx = np.argmin(d)
            
            if d[idx] < 0.5:
                name = FACE_NAME[idx]
                print(name)
                cv2.rectangle(frame,(x, y),(x+w, y+h),(0,0,255),2)
                cv2.putText(frame, name, (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,255), 2)
                sw1Pressed()
                
   
            
    cv2.imshow('frame',frame)
    cv2.waitKey(1)