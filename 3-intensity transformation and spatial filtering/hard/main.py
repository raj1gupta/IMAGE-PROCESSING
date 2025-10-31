import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load grayscale image
img = cv2.imread('lena_gray.png', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'lena_gray.png' exists in the folder.")

# Step 2: Define smoothing filters
mean_kernel = np.ones((3,3), np.float32) / 9
gaussian_kernel = cv2.getGaussianKernel(3, 1)
gaussian_kernel = gaussian_kernel @ gaussian_kernel.T  # 2D Gaussian filter

# Step 3: Apply smoothing filters
mean_filtered = cv2.filter2D(img, -1, mean_kernel)
gaussian_filtered = cv2.filter2D(img, -1, gaussian_kernel)
median_filtered = cv2.medianBlur(img, 3)  # Median filter

# Step 4: Define sharpening filters
laplacian_kernel = np.array([[0, -1, 0],
                             [-1, 4, -1],
                             [0, -1, 0]])

# Apply Laplacian filter
laplacian = cv2.filter2D(img, cv2.CV_64F, laplacian_kernel)
sharpened = cv2.addWeighted(img.astype(np.float64), 1.0, laplacian, 1.0, 0)

# Step 5: Display results
plt.figure(figsize=(14,8))

plt.subplot(2,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(mean_filtered, cmap='gray')
plt.title('Mean Filtered (3x3)')
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(gaussian_filtered, cmap='gray')
plt.title('Gaussian Filtered (σ=1)')
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(median_filtered, cmap='gray')
plt.title('Median Filtered (3x3)')
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(np.abs(laplacian), cmap='gray')
plt.title('Laplacian Edge Map')
plt.axis('off')

plt.subplot(2,3,6)
plt.imshow(np.clip(sharpened, 0, 255).astype(np.uint8), cmap='gray')
plt.title('Sharpened Image')
plt.axis('off')

plt.tight_layout()
plt.show()
