import os
import imutils
import cv2
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

import sys
sys.path.append('../')
from utils import load_image_as_array

confidence = 0.5
mean_subtract_values = (104, 177, 123)


class face_recognition:
    '''
    Define paths for the openface module, resnet module 
    '''
    def __init__(self, prototxt_path='./opencv_face_recognition/face_detector/deploy.prototxt',
                 model_path='./opencv_face_recognition/face_detector/res10_300x300_ssd_iter_140000_fp16.caffemodel',
                 embedding_model='./opencv_face_recognition/openface/nn4.small2.v1.t7',
                 labels_file=False, recogniser_file=False):
        self.detector = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
        self.embedder = cv2.dnn.readNetFromTorch(embedding_model)
        self.labels = []
        self.embeddings = {'names': [], 'embeddings': []}
        if labels_file:
            self.le = pickle.load(open(labels_file, 'rb'))
        else:
            self.le = LabelEncoder()
        if recogniser_file:
            self.recogniser = pickle.load(open(recogniser_file, 'rb'))
        else:
            self.recogniser = SVC(C=1.0, kernel="linear", probability=True)

    # Internal function
    def _detect_faces(self, image, all=False):
        # Resize images to 300x300
        resized_image = cv2.resize(image, (300, 300))
        # Extract image blob
        image_blob = cv2.dnn.blobFromImage(resized_image, 1.0, (300, 300),
                                           mean_subtract_values, swapRB=False, crop=False)
        self.detector.setInput(image_blob)
        detections = self.detector.forward()
        num_detections = detections.shape[2]
        return num_detections, detections

    # Internal function
    def _get_face_vec(self, face):
        face_blob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                          (96, 96), (0, 0, 0), swapRB=False, crop=False) #set swapRB to true if you need gray scale images
        self.embedder.setInput(face_blob)
        return self.embedder.forward()

    # Internal function
    def _get_face_bbox(self, detection, image_dimensions):
        (h, w) = image_dimensions
        box = detection[3:7] * np.array([w, h, w, h])
        start_x, start_y, end_x, end_y = box.astype("int")
        return start_x, start_y, end_x, end_y

    # Internal function
    def get_face_embeddings_from_image(self, image, all=False):
        results = []
        vec = []
        start_x, start_y, end_x, end_y = 0, 0, 0, 0

        # Detect faces in the image
        num_detections, detections = self._detect_faces(image)
        # As this is for training our classifier, take the face with the highest confidence
        if num_detections:
            if not all:
                d = np.argmax(detections[0, 0, :, 2])
                detections = detections[:, :, [d], :]
                num_detections = 1
            # Loop over detected faces
            for i in range(0, num_detections):
                conf = detections[0, 0, i, 2]

                # Check OpenCV has a high enough confidence in this being a face
                if conf > confidence:
                    start_x, start_y, end_x, end_y = self._get_face_bbox(detections[0, 0, i], image.shape[:2])
                    # Extract this face from the image and if it is sufficiently large, get the vector for it
                    face = image[start_y:end_y, start_x:end_x]
                    if face.shape[0] >= 20 and face.shape[1] > 20:
                        vec = self._get_face_vec(face)
                        results.append(((start_x, start_y, end_x, end_y), vec))
        return results

    def _build_embeddings(self, X, y):
        for i, (image_path, name) in enumerate(zip(X, y)):
            print(image_path)
            image = load_image_as_array(image_path)
            print('Processing image {}'.format(image_path))
            _, face_embedding_vector = self.get_face_embeddings_from_image(image, all=False)[0]
            if face_embedding_vector != []:
                self.embeddings['names'].append(name)
                self.embeddings['embeddings'].append(face_embedding_vector[0])

    def recognise(self, image):
        results = self.get_face_embeddings_from_image(image, all=True)
        if len(results):
            for box, vec in results:
                predictions = self.recogniser.predict_proba(vec)[0]
                if len(predictions) > 0:
                    j = np.argmax(predictions)
                    proba = predictions[j]
                    name = self.le.classes_[j]
                    start_x, start_y, end_x, end_y = box
                    text = "{}: {:.2f}%".format(name, proba * 100)
                    y = start_y - 10 if start_y - 10 > 10 else start_y + 10
                    # Uses RGB for color. 
                    cv2.rectangle(image, (start_x, start_y), (end_x, end_y),
                                  (0, 255, 255), 3)
                    cv2.putText(image, text, (start_x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        return image

    def train(self, X, y):
        print('Training model with {} sample images'.format(len(X)))
        self._build_embeddings(X, y)
        self.labels = self.le.fit_transform(self.embeddings['names'])
        self.recogniser.fit(self.embeddings['embeddings'], self.labels)
        print('Training complete')