import argparse

import numpy as np
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (9, 9), 0)  # For canny edge detection to work best, remember to blur the images
cv2.imshow("Blurred", image)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)

# RETR_EXTERNAL only takes the outermost contours
# CHAIN_APPROX_SIMPLE saves both computation and memory, by compressing all segments into their endpoint
(contours, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # We only need the contours

print "I count  %d coins in this image" % (len(contours))  # The contours are returned as a list

coins = image.copy()
# Draw a green circle around all contours with 1 pixel width
cv2.drawContours(coins, contours, -1, (0, 255, 0), 1)  # the -1 parameter tells the function to draw all contours
cv2.imshow("Coins", coins)


# Crop all the coins from the image
for (i, c) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(c)

    coin_name = "Coin #%d" % (i + 1)
    coin = image[y:y + h, x:x + w]

    mask = np.zeros(image.shape[:2], dtype="uint8")
    ((center_x, center_y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(center_x), int(center_y)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    masked_coin_name = "Masked %s" % coin_name
    cv2.imshow(masked_coin_name, cv2.bitwise_and(coin, coin, mask=mask))

cv2.waitKey(0)