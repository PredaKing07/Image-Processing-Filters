import cv2
import numpy as np

# Function to add Gaussian noise to an image
def add_gaussian_noise(image, mean=0, sigma=25):
    """Add Gaussian noise to the given image."""
    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy_image = np.clip(image + gauss, 0, 255)
    return noisy_image.astype(np.uint8)


image_path = r'C:\Users\Akshat\OneDrive\Desktop\WhatsApp Image 2024-05-07 at 11.14.09_85738241.jpg'


image = cv2.imread(image_path)

# Add Gaussian noise to the image
noisy_image = add_gaussian_noise(image)

# Convert to grayscale if necessary
gray_image = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2GRAY)

# Apply Laplacian filter for edge detection
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

# Convert the result back to uint8
sharpened_image = np.uint8(np.absolute(laplacian))

# Output the result
cv2.imshow('Noisy Image', noisy_image)
#cv2.imshow('Original Image', gray_image)
#cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
