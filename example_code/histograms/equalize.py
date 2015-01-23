import argparse

import numpy as np
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, equalized]))

cv2.waitKey(0)