# Cropping in OpenCV simply utilizes array slicing in Numpy.

import argparse

import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# cropping an image manually
cropped = image[30:120, 240:335]  # If used on the image trex.png this encapsulates its head
cv2.imshow("Cropped image", cropped)

cv2.waitKey(0)
