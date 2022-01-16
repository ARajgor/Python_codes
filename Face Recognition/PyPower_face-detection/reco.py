import face_recognition
import cv2
from datetime import datetime

known_faces=[]
known_names=[]

imgayush = face_recognition.load_image_file('1.jpg')
imgayush_encoding = face_recognition.face_encodings(imgayush)[0]
#known_face_names = ['ayush']
known_faces.append(imgayush_encoding)
known_names.append('ayush')

image=face_recognition.load_image_file('a.png')
locations = face_recognition.face_locations(image)
encoding=face_recognition.face_encodings(image,locations)
image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)


for face_encoding, face_location in zip(encoding, locations):
    results = face_recognition.compare_faces(known_faces, face_encoding)
    print("result", results)
    match = None
    if True in results:
        match = known_names[results.index(True)]
        print(f"Match found: {match}")
    else:
        print("No")


with open('Attendance.csv', 'r+') as f:
    myDataList = f.readlines()
    nameList = []
    for line in myDataList:
        entry = line.split(',')
        nameList.append(entry[0])
    if 'ayush' not in nameList:
        now = datetime.now()
        dtString = now.strftime('%H:%M:%S')
        f.writelines(f'\nayush,{dtString}')