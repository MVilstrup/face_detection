# Simple splitting and merging functionality using the RGB colours of an image
# The image could also be split into HSV or L*a*b but RGB is the standard in OpenCV

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(blue, green, red) = cv2.split(image) # Split the three channels of the image

# One way to visualize the different colours in the image
cv2.imshow("Red", red)
cv2.imshow("Green", green)
cv2.imshow("Blue", blue)

merged = cv2.merge([blue, green, red])
cv2.imshow("Merged", merged)

cv2.waitKey(0)

# Another way to visualize the colour channels
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, red]))
cv2.imshow("Green", cv2.merge([zeros, green, zeros]))
cv2.imshow("Blue", cv2.merge([blue, zeros, zeros]))

cv2.waitKey(0)