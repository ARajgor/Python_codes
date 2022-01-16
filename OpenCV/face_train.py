import os
from PIL import Image
import numpy as np
import cv2
import pickle
base_dir=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(base_dir,"img")

face_cascade =cv2.CascadeClassifier("xml\\haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id=0
label_id={}
y_labels =[]
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label =os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            #print(label,path)
            if not label in label_id:
                label_id[label]=current_id
                current_id=current_id+1
            id=label_id[label]
            print(label_id)
            #y_labels.append(label) #some number
            #x_train.append(path)  #verify this image, turn into a NUMPY array
            pil_image=Image.open(path).convert("L") #grayscale
            #size=(550,550)
            #final_img=pil_image.resize(pil_image, Image.ANTIALIAS)
            image_array=np.array(pil_image,"uint8")

            faces =face_cascade.detectMultiScale(image_array,1.5,5)
            for (x, y, w, h) in faces:
                roi = image_array[y:y + h, x:x + w]
                x_train.append(roi)
                y_labels.append(id)
# print(y_labels)
# print(x_train)

with open("lables.pickle",'wb') as f:
    pickle.dump(label_id,f)

recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainner.yml")