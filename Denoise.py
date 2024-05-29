import cv2

# Function to denoise image using Non-Local Means Denoising
def denoise_image(image):
    """Denoise the given image using Non-Local Means Denoising."""
    # Convert the image to the correct format (CV_8UC3)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Denoise the image
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

    return denoised_image

# Load the image
image_path = r'C:\Users\Akshat\OneDrive\Desktop\WhatsApp Image 2024-05-07 at 11.14.09_85738241.jpg'
image = cv2.imread(image_path)

# Denoise the image
denoised_image = denoise_image(image)

# Display the original and denoised images
cv2.imshow('Original Image', image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

