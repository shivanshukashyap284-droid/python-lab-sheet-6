import cv2

# Read image
image = cv2.imread('input.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display original and grayscale
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
