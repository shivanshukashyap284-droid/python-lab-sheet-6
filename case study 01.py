import cv2

image = cv2.imread('input.jpg')

# alpha = contrast (1.0 = original, >1 = higher contrast)
# beta = brightness (0 = original, positive = brighter, negative = darker)
alpha = 1.5   # contrast control
beta = 50     # brightness control

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

cv2.imshow("Original Image", image)
cv2.imshow("Brightness & Contrast Adjusted", adjusted)

cv2.waitKey(0)
cv2.destroyAllWindows()
