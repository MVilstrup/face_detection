from matplotlib import pyplot as plt
import argparse

import numpy as np
import cv2


def plot_flattened_histogram(image, title, mask=None):
    channels = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

    for (channel, color) in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

plot_flattened_histogram(image, "Histogram for Original Image")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15, 15), (130, 130), 255, -1)

plot_flattened_histogram(image, "Histogram for Masked Image", mask=mask)
