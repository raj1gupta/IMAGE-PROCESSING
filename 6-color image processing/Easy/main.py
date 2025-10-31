import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load grayscale image
img = cv2.imread('Original_lena_gray.jpg', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'grayscale_image.png' is in the same folder.")

# 2. Create an empty color image (same height, width)
rows, cols = img.shape
color_img = np.zeros((rows, cols, 3), dtype=np.uint8)

# 3. Define intensity ranges and corresponding colors (BGR format for OpenCV)
# Example: (lower, upper, (B, G, R))
ranges = [
    (0, 85, (255, 0, 0)),     # Blue for dark regions
    (86, 170, (0, 255, 0)),   # Green for mid intensity
    (171, 255, (0, 0, 255))   # Red for bright regions
]

# 4. Apply color mapping based on intensity slicing
for lower, upper, color in ranges:
    mask = cv2.inRange(img, lower, upper)
    color_img[mask > 0] = color

# 5. Display results
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))
plt.title('Intensity Sliced Pseudocolor Image')
plt.axis('off')

plt.show()
