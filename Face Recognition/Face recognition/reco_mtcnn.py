import mtcnn
import face_recognition
import cv2
import tensorflow
# initialise the detector class.
detector = mtcnn.MTCNN()
# load an image as an array
image = face_recognition.load_image_file("my.jpg")
# detect faces from input image.
face_locations = detector.detect_faces(image)
# draw bounding box and five facial landmarks of detected face
for face in zip(face_locations):
    (x, y, w, h) = face[0]['box']
    landmarks = face[0]['keypoints']
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
    # for key, point in landmarks.items():
    #     cv2.circle(image, point, 2, (255, 0, 0), 6)
resize=cv2.resize(image,(800,800))
cv2.imshow('image',resize)
cv2.waitKey(0)
cv2.destroyAllWindows()