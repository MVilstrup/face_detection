from facedetector import FaceDetector
import argparse

import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="path to where the face cascade resides")
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Load the face cascade into the face detector
face_detector = FaceDetector(args["face"])

# Detect all the faces on the image
face_rectangles = face_detector.detect(gray)

print "I found %d face(s)" % len(face_rectangles)

# Draw rectangles around the faces found on the image
for (x, y, w, h) in face_rectangles:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)
