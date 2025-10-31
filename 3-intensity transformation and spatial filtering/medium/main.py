import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load input and reference images (grayscale)
img = cv2.imread('low_contrast.png', 0)
ref = cv2.imread('cameraman.tif', 0)

if img is None or ref is None:
    raise FileNotFoundError("Image not found. Make sure both input and reference images exist.")

# Step 2: Apply Histogram Equalization
equalized = cv2.equalizeHist(img)

# Step 3: Histogram Specification (Matching)
def hist_match(source, template):
    oldshape = source.shape
    source = source.ravel()
    template = template.ravel()

    # Get unique pixel values and their corresponding cumulative distributions
    s_values, bin_idx, s_counts = np.unique(source, return_inverse=True, return_counts=True)
    t_values, t_counts = np.unique(template, return_counts=True)

    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    # Interpolate pixel values from template to source mapping
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)
    return interp_t_values[bin_idx].reshape(oldshape)

specified = hist_match(img, ref).astype(np.uint8)

# Step 4: Display images
plt.figure(figsize=(14,8))

plt.subplot(2,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(equalized, cmap='gray')
plt.title('Histogram Equalized')
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(specified, cmap='gray')
plt.title('Histogram Specified (Matched)')
plt.axis('off')

plt.subplot(2,3,4)
plt.hist(img.ravel(), 256, [0,256], color='gray')
plt.title('Original Histogram')

plt.subplot(2,3,5)
plt.hist(equalized.ravel(), 256, [0,256], color='blue')
plt.title('Equalized Histogram')

plt.subplot(2,3,6)
plt.hist(specified.ravel(), 256, [0,256], color='green')
plt.title('Specified Histogram')

plt.tight_layout()
plt.show()
