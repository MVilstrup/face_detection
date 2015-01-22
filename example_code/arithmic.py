import numpy as np
import argparse
from utils import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# OpenCV utilizes clipping, and will never exceed 255 or go below 0
print "max of 255: %s" % str(cv2.add(np.uint8([200]), np.uint8([100])))
print "min of 0: %s" % str(cv2.subtract(np.uint8([50]), np.uint8([100])))

# Numpy utilizes wrap around when reaching the maximum or minimum value
print "Wrap around %s" % str(np.uint8([200]) + np.uint8([100]))
print "Wrap around %s" % str(np.uint8([50]) - np.uint8([100]))

matrix = np.ones(image.shape, dtype="uint8") * 100 # Create a matrix with the dimensions of image, and 100 in each slot
added = cv2.add(image, matrix) # Add 100 to all pixel values
cv2.imshow("Added", added)

matrix = np.ones(image.shape, dtype="uint8") * 50 # Create a matrix with the dimensions of image, and 50 in each slot
subtracted = cv2.subtract(image, matrix) # Subtract 50 from all pixel values
cv2.imshow("Subratcted", subtracted)

cv2.waitKey(0)

