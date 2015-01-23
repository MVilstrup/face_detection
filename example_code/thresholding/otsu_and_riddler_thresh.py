import argparse

import mahotas

import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)


# Finding the threshold using Otsu's method
T = mahotas.thresholding.otsu(blurred)  # Calculate the threshold using Otsu's method
print  "Otsu's threshold %d" % (T)
thresh = image.copy()
thresh[thresh > T] = 255  # Make all pixels above the threshold white
thresh[thresh <= T] = 0  # Make all pixels below the threshold black
thresh = cv2.bitwise_not(thresh)  # A bitwise NOT inverts the on and off pixels in an image.
cv2.imshow("Otsu", thresh)

# Finding the threshold using the Riddler-calvard method
T = mahotas.thresholding.rc(blurred)
print "Riddler-Calvard: %d" % (T)
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh <= T] = 0
thresh = cv2.bitwise_not(thresh)  # A bitwise NOT inverts the on and off pixels in an image.
cv2.imshow("Riddler-Calvard", thresh)

cv2.waitKey(0)
