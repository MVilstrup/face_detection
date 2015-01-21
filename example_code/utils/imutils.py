import numpy as np
import cv2

def translate(image, x, y):
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, angle, center = None, scale = 1.0):
    (height, width) = image.shape[:2]

    if center is None:
        center = (width / 2, height / 2)

    matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, matrix, (width, height))

    return rotated