import cv2
#creat a CascadeClassifier Object
face_cascade =cv2.CascadeClassifier("xml\\haarcascade_frontalface_alt.xml")
#Reading the image as it is
img =cv2.imread("i.jpg")
#Reading the image as gray scale img
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#search the co-ordinates of the img
faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.03, minNeighbors=3)

print(type(faces))
print(faces)
total=0
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    total=total+1
resize=cv2.resize(img,(1280,1024))
print(total)

cv2.imshow("Screenshot (78)",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()