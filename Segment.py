import cv2
import numpy as np
from sklearn.cluster import KMeans

# Function to perform image segmentation using K-means clustering
def segment_image(image, num_clusters):
    """Segment the given image into the specified number of clusters."""
    # Reshape the image into a 2D array of pixels
    pixels = image.reshape((-1, 3))

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(pixels)

    # Get the labels and centroids of clusters
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # Reshape labels to original image shape
    segmented_image = labels.reshape(image.shape[0], image.shape[1])

    return segmented_image

# Load the image
image_path = r'C:\Users\Akshat\OneDrive\Desktop\WhatsApp Image 2024-05-07 at 11.14.09_85738241.jpg'
image = cv2.imread(image_path)

# Convert image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Number of clusters for segmentation
num_clusters = 5

# Perform image segmentation
segmented_image = segment_image(image_rgb, num_clusters)

# Convert segmented image to uint8 data type
segmented_image_uint8 = (segmented_image * (255/num_clusters)).astype(np.uint8)

# Display the segmented image
cv2.imshow('Segmented Image', segmented_image_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()
