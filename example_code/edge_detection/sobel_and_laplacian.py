import argparse

import numpy as np
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", image)

# To calculate the gradients of an image it is best not to use uint8 since you will miss some edges

# Calculate gradients using the laplacian method
lap = cv2.Laplacian(image,
                    cv2.CV_64F)  # Convert the image to using 64 bit floats and calculate the gradients afterwards
lap = np.uint8(np.absolute(lap))  # Convert the image back into uint8
cv2.imshow("Laplacian", lap)

# Calculate the edges using the Sobel method

# In the Sobel method the gradients are calculated both horizontally and vertically
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)  # Remember to convert into 64 bit floats
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobel_x = np.uint8(np.absolute(sobel_x))  # remember to convert back into 8 bit unsigned integers
sobel_y = np.uint8(np.absolute(sobel_y))

sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)  # Combine the two gradients to get a better result

sobel = np.hstack([
    sobel_x,
    sobel_y,
    sobel_combined
])

cv2.imshow("Sobel", sobel)

cv2.waitKey(0)