import argparse

import numpy as np
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")  # Create a mask that is the size of the original image with only zeros
(center_x, center_y) = (image.shape[1] / 2, image.shape[0] / 2)  # Calculate the center of the image
cv2.rectangle(mask,
              (center_x - 75, center_y - 75),
              (center_x + 75, center_y + 75),
              255, -1)  # Create a 75x75 square with the same center filled with white pixels

cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (center_x, center_y), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Circular masked image", masked)

cv2.waitKey(0)

