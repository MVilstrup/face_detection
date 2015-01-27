import cv2

# Simple class used to do face detection
# All the heavy lifting is done by OpenCV and face cascade crated by Rainer Lienhart
class FaceDetector:
    def __init__(self, face_cascade_path):
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)

    def detect(self, image, scale_factor = 1.2, min_neighbours = 5, min_size = (30, 30)):
        rectangles = self.face_cascade.detectMultiScale(image,
                                                        scaleFactor=scale_factor,
                                                        minNeighbors=min_neighbours,
                                                        minSize=min_size,
                                                        flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

        return rectangles
