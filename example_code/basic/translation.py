import argparse

import numpy as np
import cv2

from utils.imutils import translate


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)


# Matrix done manually for demonstrations purposes
M = np.float32([[1, 0, -50], [0, 1, -90]])  # 50 pixels left and 90 pixels up
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# Using the utils created
shifted = translate(image, 0, 100)
cv2.imshow("Shifted Down and Right", shifted)

cv2.waitKey(0)