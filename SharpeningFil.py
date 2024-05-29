import cv2
import numpy as np

# Function to apply sharpening filter
def sharpen_image(image):
    """Apply sharpening filter to the given image."""
    # Define the sharpening kernel
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    # Apply the kernel to the image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    return sharpened_image

# Load the image
image_path = r'C:\Users\Akshat\OneDrive\Desktop\WhatsApp Image 2024-05-07 at 11.14.09_85738241.jpg'
image = cv2.imread(image_path)

# Apply sharpening filter
sharpened_image = sharpen_image(image)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
