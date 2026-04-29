import cv2

image = cv2.imread('input.jpg')

# Flip horizontally
flip_horizontal = cv2.flip(image, 1)

# Flip vertically
flip_vertical = cv2.flip(image, 0)

# Flip both axes
flip_both = cv2.flip(image, -1)

cv2.imshow("Horizontal Flip", flip_horizontal)
cv2.imshow("Vertical Flip", flip_vertical)
cv2.imshow("Both Flips", flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
