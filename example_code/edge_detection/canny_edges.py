import argparse

import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)  # For canny edge detection to work best, remember to blur the images
cv2.imshow("Blurred", image)

# Canny uses the sobel gradient detection to calculate the gradients in both axes.
canny = cv2.Canny(image, 30, 150)  # The values given are two thresholds in the gradients (30 = non edges, 150 = edges)
cv2.imshow("Canny", canny)

cv2.waitKey(0)
