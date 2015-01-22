from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Calculate a flattened histogram from the three RGB colors
channels = cv2.split(image)
colors = ("b", "g", "r") # OpenCV stores the color values in opposite order
plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (channel, color) in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256]) # Calculate the histogram for each channel
    plt.plot(hist, color = color) # Plot the calculated histogram
    plt.xlim([0, 256]) # Limit the x-axis to 0-256

plt.show()

# Calculate a two-dimensional histogram to see the combination of the colors
two_dim = plt.figure()

ax = two_dim.add_subplot(131)
hist = cv2.calcHist([channels[1], channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for Green and Blue"
)
plt.colorbar(p)

ax = two_dim.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for Green and Red"
)
plt.colorbar(p)

ax = two_dim.add_subplot(133)
hist = cv2.calcHist([channels[0], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for Blue and Red"
)
plt.colorbar(p)

plt.show()

# Calculate a three-dimensional histogram to see the combinations of all three colours
hist = cv2.calcHist([image], [0,1,2], None,[8,8,8],[0,256,0,256,0,256])
print "3D histogram shape: %s, with %d values" % (hist.shape, hist.flatten().shape[0])

cv2.waitKey(0)

