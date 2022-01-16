import cv2,time
#"C:\\Users\Ayush Rajgor\\Downloads\\Video\\ai.mp4"
video= cv2.VideoCapture(0)
face_cascade =cv2.CascadeClassifier("xml\\haarcascade_frontalface_default.xml")
side_cascade =cv2.CascadeClassifier("xml\\haarcascade_profileface.xml")
up_cascade =cv2.CascadeClassifier("haarcascade_eye.xml")
a=1

while True:
    a=a+1
    check, frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.7,3)
    #sides=side_cascade.detectMultiScale(gray,1.5,5)
    #upp = up_cascade.detectMultiScale(gray, 1.8, 7)

    for (x, y, w, h )in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        #print(x,y,w,h)
    #for (x, y, w, h )in sides:
         #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255,0 ), 3)
    #for (x, y, w, h )in upp:
       # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0,255 ), 2)

    resize = cv2.resize(frame,(800,600))
    #resize = cv2.resize(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)))
    cv2.imshow("Frame",resize)

    if cv2.waitKey(1)&0xFF == ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()