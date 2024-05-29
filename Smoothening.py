import cv2


image_path = r'D:\data\test\open eyes\s0001_01919_0_0_1_0_0_01.png'

# Load the image
image = cv2.imread(image_path)

# Convert to grayscale if necessary
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)  # Kernel size (5,5), sigma=0

# Output the result
#cv2.imshow('Original Image', gray_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
