# This small snippet demonstrates some of the functionality of Numpy and OpenCV
#
# Notice the image is stored as a 2-dimensional array and ability to select a section of an image
# with a simple range.
#

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(b, g, r) = image[0, 0] # CV2 stores all the colour of the pixels in reverse order (Blue, Green, Red)
print "Pixel at (0, 0) - Red: %d, Green: %d, Blue %d" % (r, g, b)

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print "Pixel at (0, 0) - Red: %d, Green: %d, Blue %d" % (r, g, b)

corner = image[0:100, 0:100]
cv2.imshow("Upper Left Corner", corner)

image[0:100, 0:100] = (0, 255, 0) # CV2 stores all the colour of the pixels in reverse order (Blue, Green, Red)

cv2.imshow("Updated", image)

cv2.waitKey(0)