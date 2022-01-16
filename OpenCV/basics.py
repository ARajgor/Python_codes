import cv2
import numpy as np
video=cv2.VideoCapture(0)
img = cv2.imread("img\\alia\\download.jpg",1)
#print(img.shape)
kernal=np.ones((5,5),np.uint8)
#resize=cv2.resize(img,(600,600))
resize=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(7,7),0)
    canny=cv2.Canny(blur,10,70)
    dilation=cv2.dilate(canny,kernal,iterations=2)
    canny1=cv2.Canny(frame,100,100)
    canny2=cv2.Canny(frame,200,200)

    cv2.imshow("canny",canny)
    cv2.imshow("canny1", canny1)
    cv2.imshow("dilation", dilation)

    if cv2.waitKey(1)&0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()