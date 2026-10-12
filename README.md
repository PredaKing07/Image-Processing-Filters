# Image Processing Filters

A set of standalone Python scripts showing core image-processing techniques with OpenCV: adding noise, removing it, sharpening, smoothing, edge detection and segmentation.

## Scripts

| Script | Technique | Key function |
|---|---|---|
| `Noiseip.py` | Adds **Gaussian noise** to an image, then runs **Laplacian edge detection** | `np.random.normal`, `cv2.Laplacian` |
| `Denoise.py` | **Non-Local Means denoising** for colour images | `cv2.fastNlMeansDenoisingColored` |
| `SharpeningFil.py` | **Sharpening** with a 3×3 convolution kernel | `cv2.filter2D` |
| `Smoothening.py` | **Gaussian blur** on a grayscale image | `cv2.GaussianBlur` |
| `Segment.py` | **Colour segmentation** with K-means clustering (5 clusters) | `sklearn.cluster.KMeans` |

Each script loads an image, applies its technique and shows the result in an OpenCV window.

## Tech stack
Python · OpenCV · NumPy · scikit-learn

## Setup
```bash
pip install opencv-python numpy scikit-learn
```
Set `image_path` at the top of each script to an image on your machine, then run it, for example:
```bash
python Denoise.py
```
Press any key to close the windows.
