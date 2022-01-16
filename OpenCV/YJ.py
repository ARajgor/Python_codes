import cv2

video= cv2.VideoCapture(0)
face_cascade =cv2.CascadeClassifier("xml\\haarcascade_frontalface_default.xml")

while True:

    check, frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.7,3)

    for (x, y, w, h )in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    resize = cv2.resize(frame,(800,600))
    cv2.imshow("Frame",resize)

    if cv2.waitKey(1)&0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()