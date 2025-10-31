import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load grayscale image
img = cv2.imread('cameraman.png', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'noisy_image.jpg' is in this folder.")

# Step 2: (Optional) Add artificial noise for testing
# Add salt & pepper noise
noisy = img.copy()
prob = 0.02  # noise probability
for i in range(noisy.shape[0]):
    for j in range(noisy.shape[1]):
        rnd = np.random.rand()
        if rnd < prob/2:
            noisy[i, j] = 0
        elif rnd < prob:
            noisy[i, j] = 255

# Step 3: Apply smoothing filters

# (a) Mean Filter (Averaging)
mean_filtered = cv2.blur(noisy, (5,5))  # 5x5 kernel

# (b) Gaussian Filter
gaussian_filtered = cv2.GaussianBlur(noisy, (5,5), sigmaX=1.0)

# (c) Median Filter
median_filtered = cv2.medianBlur(noisy, 5)

# Step 4: Display all images
plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(noisy, cmap='gray')
plt.title('Noisy Image (Salt & Pepper)')
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(mean_filtered, cmap='gray')
plt.title('Mean Filter Result')
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(gaussian_filtered, cmap='gray')
plt.title('Gaussian Filter Result')
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(median_filtered, cmap='gray')
plt.title('Median Filter Result')
plt.axis('off')

plt.tight_layout()
plt.show()
