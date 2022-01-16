import cv2,time
import numpy as np
import pickle

#"C:\\Users\Ayush Rajgor\\Downloads\\Video\\ai.mp4"
video= cv2.VideoCapture(0)
face_cascade =cv2.CascadeClassifier("D:\\Python\\Codes\\OpenCV\\xml\\haarcascade_frontalface_default.xml")
eye_cascade =cv2.CascadeClassifier("D:\\Python\\Codes\\OpenCV\\xml\\haarcascade_eye.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('D:\\Python\\Codes\\OpenCV\\trainner.yml')

labels={"person_name":1 }
with open("D:\\Python\\Codes\\OpenCV\\lables.pickle",'rb') as f:
     og_labels = pickle.load(f)
     labels={v:k for k,v in og_labels.items()}
#a=1
while True:
    #a=a+1
    check, frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.03,minNeighbors=5)

    for (x, y, w, h )in faces:
        roi_gray =gray[y:y+h,x:x+w]

        roi_color = frame[y:y + h, x:x + w]

        id_,conf=recognizer.predict(roi_gray)
        if conf>=45 and conf <=85:
            print(id_)
            print(labels[id_])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color=(255,255,255)
            stroke=2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
        img_item = "my.png"
        cv2.imwrite(img_item,roi_gray)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    #resize = cv2.resize(frame,(600,600))
    #resize = cv2.resize(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)))
    cv2.imshow("Frame",frame)

    if cv2.waitKey(1)&0xFF == ord('q'):
        break
#print()
video.release()
cv2.destroyAllWindows()