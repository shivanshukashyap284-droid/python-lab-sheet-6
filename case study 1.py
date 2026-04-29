import cv2
import numpy as np

image = cv2.imread('input.jpg')
rows, cols = image.shape[:2]

# Translation matrix: shift right by 100, down by 50
M = np.float32([[1, 0, 100], [0, 1, 50]])

translated = cv2.warpAffine(image, M, (cols, rows))

cv2.imshow("Translated Image", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
