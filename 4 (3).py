import cv2

image = cv2.imread('input.jpg')

# Resize to half
resized = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))

cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
