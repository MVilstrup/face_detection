import argparse

import cv2

from utils import imutils


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Create a new image that is only 150 pixels wide manually
ratio = 150.0 / image.shape[1]  # Calculate the ratio between the original width and the new width
dim = (150, int(image.shape[0] * ratio))  # Create new dimensions for the image

resized = cv2.resize(image, dim,
                     interpolation=cv2.INTER_AREA)  # INTER_AREA: The algorithm used to calculate the interpolation
cv2.imshow("Resized (Width)", resized)


# Create a new image this is only 50 pixels high manually
ratio = 50.0 / image.shape[0]  # Calculate the ratio between the original height and the new height
dim = (int(image.shape[0] * ratio), 50)  # Create new dimensions for the image

resized = cv2.resize(image, dim,
                     interpolation=cv2.INTER_AREA)  # INTER_AREA: The algorithm used to calculate the interpolation
cv2.imshow("Resized (Height)", resized)


# Use the utils function to resize the image based on a new height
resized = imutils.resize(image, height=200)
cv2.imshow("Resized with utils", resized)

cv2.waitKey(0)