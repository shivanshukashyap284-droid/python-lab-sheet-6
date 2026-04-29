import cv2
import numpy as np

# Load image
image = cv2.imread('input.jpg')

# Get image dimensions
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Rotation matrix: 45 degrees
M = cv2.getRotationMatrix2D(center, 45, 1.0)

# Apply rotation
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
