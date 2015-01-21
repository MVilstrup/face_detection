import numpy as np
import cv2

def translate(image, x, y):
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    return shifted
