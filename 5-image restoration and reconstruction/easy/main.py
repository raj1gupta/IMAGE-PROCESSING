import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a grayscale image
img = cv2.imread('moon.tif', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'low_contrast_image.jpg' is in this folder.")

# Step 2: Contrast Stretching
r_min, r_max = np.min(img), np.max(img)
contrast_stretched = ((img - r_min) / (r_max - r_min)) * 255
contrast_stretched = np.clip(contrast_stretched, 0, 255).astype(np.uint8)

# Step 3: Log Transformation
# Convert to float and normalize
img_float = img / 255.0
c = 255 / np.log(1 + np.max(img_float))
log_transformed = c * np.log(1 + img_float)
log_transformed = np.clip(log_transformed, 0, 255).astype(np.uint8)

# Step 4: Display results
plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Low-Contrast Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(contrast_stretched, cmap='gray')
plt.title('After Contrast Stretching')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(log_transformed, cmap='gray')
plt.title('After Log Transformation')
plt.axis('off')

plt.tight_layout()
plt.show()

# Step 5: Optional - Display histograms
plt.figure(figsize=(10,4))
plt.hist(img.ravel(), 256, [0,256], label='Original', color='gray', alpha=0.5)
plt.hist(contrast_stretched.ravel(), 256, [0,256], label='Contrast Stretched', color='blue', alpha=0.5)
plt.hist(log_transformed.ravel(), 256, [0,256], label='Log Transformed', color='red', alpha=0.5)
plt.legend()
plt.title('Histogram Comparison')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
