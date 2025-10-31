import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load color image
img_color = cv2.imread('peppers.png')
if img_color is None:
    raise FileNotFoundError("Image not found. Make sure 'peppers.png' is in this folder.")

# Convert BGR (OpenCV default) to RGB for correct display
img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

# Step 2: Convert to Grayscale (using weighted average)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Step 3: Convert to Binary using thresholding
# You can set threshold manually or use Otsu's automatic thresholding
_, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# Optional: Otsu's method (automatic thresholding)
# _, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Step 4: Display all images
plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title('Original RGB Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(img_gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(img_binary, cmap='gray')
plt.title('Binary Image (Thresholded)')
plt.axis('off')

plt.tight_layout()
plt.show()
