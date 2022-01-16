# import face_recognition
# from PIL import Image
# img=face_recognition.load_image_file('i.jpg')
# f=face_recognition.face_locations(img)
# print("I found {} face(s) in this photo.".format(len(f)))
# for fi in f:
#     t,r,b,l=fi
#     f_i=img[t:b,l:r]
#     p_i=Image.fromarray(f_i)
#     p_i.show()

#-------------canny edge--------------------
# import matplotlib
# import numpy as np
# import cv2
#
#
# def sketchImage(image):
#     img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
#     canny_edges = cv2.Canny(img_gray_blur, 10, 70)
#     ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
#     return mask
#
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     cv2.imshow('Live Sketch', sketchImage(frame))
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#------------------------- for img----------------------------------

import face_recognition
import os
import cv2

KNOWN_FACES_DIR ="known"
UNKNOWN_FACES_DIR ="unknown"
TOLERANCE = 0.6
FRAME_THICKNESS =3
FONT_THICKNESS =2
MODEL="hog"

known_faces=[]
known_names=[]

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        encoding=face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)

print("processing unkown faces")
for filename in os.listdir(UNKNOWN_FACES_DIR):
    print(filename)
    image=face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
    locations = face_recognition.face_locations(image,model=MODEL)
    print("location",locations)

    encoding=face_recognition.face_encodings(image,locations)
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encoding,locations):
        results=face_recognition.compare_faces(known_faces,face_encoding,TOLERANCE)
        print("result",results)
        match = None
        if True in results:
            match=known_names[results.index(True)]
            print(f"Match found: {match}")
            # for (x, y, w, h) in locations:
            #     i = image[y:y + h, x:x + w]
            #     n = "my.png"
            #     cv2.imwrite(n, i)
            #     break
            top_left=(face_location[3],face_location[0])
            bottom_right=(face_location[1],face_location[2])
            color=[0,255,0]
            cv2.rectangle(image,top_left,bottom_right,color,FRAME_THICKNESS)

            top_left=(face_location[3],face_location[2])
            bottom_right=(face_location[1],face_location[2]+22)
            cv2.rectangle(image,top_left,bottom_right,color,cv2.FILLED)
            cv2.putText(image,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,200,200),FONT_THICKNESS)

    resize = cv2.resize(image, (1280, 1024))
    #cv2.imwrite(filename,face_location)
    cv2.imshow(filename,resize)
    cv2.waitKey(10000)
    #cv2.destroyWindow(filename)