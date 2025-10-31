import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a color image
img = cv2.imread('flower_color.jpeg')
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'color_image.jpg' is in this folder.")

# Convert from BGR to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 2: Smoothing (Blurring)

# (a) Average Filter
kernel_size = 5
blur_avg = cv2.blur(img_rgb, (kernel_size, kernel_size))

# (b) Gaussian Blur
blur_gauss = cv2.GaussianBlur(img_rgb, (7, 7), sigmaX=1.5)

# Step 3: Sharpening

# (a) Laplacian Filter (detects edges)
laplacian = cv2.Laplacian(img_rgb, cv2.CV_64F)
laplacian = np.clip(laplacian, 0, 255).astype(np.uint8)

# (b) Unsharp Masking / High-boost filtering
# Unsharp Mask = Original + k*(Original - Blurred)
k = 1.5  # sharpening strength
blur = cv2.GaussianBlur(img_rgb, (7, 7), 2)
mask = cv2.subtract(img_rgb, blur)
high_boost = cv2.addWeighted(img_rgb, 1.0, mask, k, 0)

# Step 4: Display results
plt.figure(figsize=(14, 10))

plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(blur_avg)
plt.title('Average Filter (Smoothing)')
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(blur_gauss)
plt.title('Gaussian Filter (Smoothing)')
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(laplacian)
plt.title('Laplacian (Edge Enhancement)')
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(high_boost)
plt.title('High-Boost Sharpened Image')
plt.axis('off')

plt.tight_layout()
plt.show()
