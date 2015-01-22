# In this short snippet the fact that OpenCV treats all images as Numpy 2-dimensional arrays is utilized
# Simple operations from OpenCV such as line, rectangle and circle is demonstrated


import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")  # Create a canvas with the dimension 300x300

# CV2 stores all the colour of the pixels in reverse order (Blue, Green, Red)
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)

cv2.line(canvas, (0, 0), (300, 300), green)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.rectangle(canvas, (200, 50), (255, 125), blue, -1)

cv2.imshow("Canvas with stripes and rectangles", canvas)

canvas = np.zeros((300, 300, 3), dtype="uint8")  # Create a canvas with the dimensions 300x300s
(centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2)  # The middle of the canvas

for r in xrange(0, 175, 25):  # From 0-150 with a step value of 25
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas with circle", canvas)

canvas = np.zeros((300, 300, 3), dtype="uint8")  # Create a canvas with the dimensions 300x300s
for i in xrange(0, 25):
    radius = np.random.randint(5, high=200)
    colour = np.random.randint(0, high=256,
                               size=(3,)).tolist()  # Create three different values from 0-256 and save them as a list
    center = np.random.randint(0, high=300,
                               size=(2,)).tolist()  # Create two different values from 0-300 and save them as a list
    cv2.circle(canvas, tuple(center), radius, colour, -1)

cv2.imshow("Canvas with random spheres", canvas)
cv2.waitKey(0)
