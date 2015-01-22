import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Blurring using the averaged function, where all the pixels in the neighborhood have equal weight
blurred = np.hstack([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))
])

cv2.imshow("Averaged", blurred)

# Blurring using the Gaussian function where pixels closer to the pixels color gets a higher weight
blurred = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)
])

cv2.imshow("Gaussian", blurred)


# Blurring using the median function where the kernel is replaced with the median pixel of the kernel neighborhood
# Median blur is usually the best function to remove noise from the image
blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)
])

cv2.imshow("Median", blurred)


# Blurring using the bilateral function, that uses two Gaussian distributions to remove noise yet retain edges
# This method has great results yet are much slower than the other functions
blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)
])

cv2.imshow("Bilateral", blurred)

cv2.waitKey(0)

