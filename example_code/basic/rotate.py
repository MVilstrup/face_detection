import argparse

import cv2

from utils import imutils


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Showcase of the manual way of rotation an image

(height, width) = image.shape[:2]  # get the two first values of the image which is height and width
center = (width / 2, height / 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("Rotated by 45 Degrees", rotated)

# Showcase of rotating an image using the defined utils function rotate
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)

cv2.waitKey(0)