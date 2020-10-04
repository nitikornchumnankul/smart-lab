import numpy as np
import cv2 #ใช้แค่ในการอ่านวิดิโอเข้ามา
import dlib
import os
import pickle

path = './Face_data/'
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
FACE_DESC =[]
FACE_NAME =[]

for fn in os.listdir(path):
    if fn.endswith('.jpg'):
        img = cv2.imread(path + fn)[:,:,::-1]
        dets = detector(img,1)
        for k, d in enumerate(dets): #วนหาว่ามีรูปอะไรบ้างใน​ dets ทุกหน้าที่เจอจะผ่านการ landmark
            shape = sp(img, d) # d is bounding box
            face_desc = model.compute_face_descriptor(img,shape,1)
            FACE_DESC.append(face_desc)
            print('loading.........', fn)
            FACE_NAME.append(fn[:fn.index('_')])

pickle.dump((FACE_DESC,FACE_NAME),open('trainset.pk','wb'))
            