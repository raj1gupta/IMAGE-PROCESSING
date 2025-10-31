import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the grayscale image
img = cv2.imread('lena_gray.gif', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'gray_image.jpg' is in this folder.")

# Step 2: Apply Histogram Equalization using OpenCV
equalized_img = cv2.equalizeHist(img)

# Step 3: Compute histograms (for comparison)
hist_original = cv2.calcHist([img], [0], None, [256], [0,256])
hist_equalized = cv2.calcHist([equalized_img], [0], None, [256], [0,256])

# Step 4: Display results
plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2,2,3)
plt.plot(hist_original, color='gray')
plt.title('Histogram of Original Image')
plt.xlabel('Intensity Value')
plt.ylabel('Pixel Count')

plt.subplot(2,2,4)
plt.plot(hist_equalized, color='black')
plt.title('Histogram of Equalized Image')
plt.xlabel('Intensity Value')
plt.ylabel('Pixel Count')

plt.tight_layout()
plt.show()
