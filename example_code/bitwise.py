import numpy as np
import cv2

rectangle = np.zeros((300, 300), dtype= "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwise_and = cv2.bitwise_and(rectangle, circle) # Checks if pixels in the same position greater than 0 in both images
cv2.imshow("AND", bitwise_and)

bitwise_or = cv2.bitwise_or(rectangle, circle) # Checks if pixels in the same position greater than 0 in either image
cv2.imshow("OR", bitwise_or)

bitwise_xor = cv2.bitwise_xor(rectangle, circle) # Pixels in the same position greater than 0 in either image but not both
cv2.imshow("XOR", bitwise_xor)

bitwise_not = cv2.bitwise_not(rectangle, circle) # A bitwise NOT inverts the on and off pixels in an image.
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
