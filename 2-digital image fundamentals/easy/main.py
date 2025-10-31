import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load grayscale image
img = cv2.imread('cameraman.tif', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'cameraman.tif' is in this folder.")

# Step 2: Sampling (Downsampling the image)
# Reduce spatial resolution by resizing
sampled_2 = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv2.INTER_NEAREST)
sampled_4 = cv2.resize(img, (img.shape[1]//4, img.shape[0]//4), interpolation=cv2.INTER_NEAREST)
sampled_8 = cv2.resize(img, (img.shape[1]//8, img.shape[0]//8), interpolation=cv2.INTER_NEAREST)

# Step 3: Upscale them back to original size for visualization
sampled_2_up = cv2.resize(sampled_2, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
sampled_4_up = cv2.resize(sampled_4, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
sampled_8_up = cv2.resize(sampled_8, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

# Step 4: Quantization (Reduce intensity levels)
def quantize(img, levels):
    step = 256 // levels
    return np.floor(img / step) * step

quant_256 = img                   # Original (8-bit = 256 levels)
quant_64 = quantize(img, 64).astype(np.uint8)
quant_32 = quantize(img, 32).astype(np.uint8)
quant_8 = quantize(img, 8).astype(np.uint8)

# Step 5: Display results
plt.figure(figsize=(13,10))

# Original
plt.subplot(3,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original (256x256, 256 levels)')
plt.axis('off')

# Sampling results
plt.subplot(3,3,2)
plt.imshow(sampled_2_up, cmap='gray')
plt.title('Downsampled by 2 (128x128)')
plt.axis('off')

plt.subplot(3,3,3)
plt.imshow(sampled_4_up, cmap='gray')
plt.title('Downsampled by 4 (64x64)')
plt.axis('off')

plt.subplot(3,3,4)
plt.imshow(sampled_8_up, cmap='gray')
plt.title('Downsampled by 8 (32x32)')
plt.axis('off')

# Quantization results
plt.subplot(3,3,5)
plt.imshow(quant_256, cmap='gray')
plt.title('Quantized: 256 Levels')
plt.axis('off')

plt.subplot(3,3,6)
plt.imshow(quant_64, cmap='gray')
plt.title('Quantized: 64 Levels')
plt.axis('off')

plt.subplot(3,3,7)
plt.imshow(quant_32, cmap='gray')
plt.title('Quantized: 32 Levels')
plt.axis('off')

plt.subplot(3,3,8)
plt.imshow(quant_8, cmap='gray')
plt.title('Quantized: 8 Levels')
plt.axis('off')

plt.tight_layout()
plt.show()
