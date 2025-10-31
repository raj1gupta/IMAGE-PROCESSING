import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load grayscale image
img = cv2.imread('moon.tif', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'moon.tif' is in this folder.")

# Step 2: Image Negative Transformation
L = 256  # Maximum intensity value
negative_img = L - 1 - img

# Step 3: Logarithmic Transformation
img_float = img / 255.0  # Normalize to [0,1]
c = 255 / np.log(1 + np.max(img_float))
log_img = c * np.log(1 + img_float)
log_img = np.array(log_img, dtype=np.uint8)

# Step 4: Display Results
plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(negative_img, cmap='gray')
plt.title('Negative Transformation')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(log_img, cmap='gray')
plt.title('Logarithmic Transformation')
plt.axis('off')

plt.tight_layout()
plt.show()

# Step 5 (Optional): Show histograms for analysis
plt.figure(figsize=(10,4))
plt.hist(img.ravel(), 256, [0,256], color='gray', label='Original')
plt.hist(negative_img.ravel(), 256, [0,256], color='red', alpha=0.5, label='Negative')
plt.hist(log_img.ravel(), 256, [0,256], color='blue', alpha=0.5, label='Logarithmic')
plt.title('Histogram Comparison')

plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.legend()
plt.show()
