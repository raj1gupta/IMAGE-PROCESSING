import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load grayscale image
img = cv2.imread('cameraman.png', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'cameraman.tif' is in this folder.")

# Step 2: Perform Fourier Transform and shift the origin to the center
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

# Step 3: Create Ideal Low-Pass Filter (ILPF)
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2  # center
D0 = 50  # cutoff frequency (adjust to control blur)

# Create circular mask with ones inside cutoff circle
mask = np.zeros((rows, cols), np.uint8)
for u in range(rows):
    for v in range(cols):
        D = np.sqrt((u - crow)**2 + (v - ccol)**2)
        if D <= D0:
            mask[u, v] = 1

# Step 4: Apply the filter
filtered_dft = dft_shift * mask

# Step 5: Inverse FFT to get the filtered image
f_ishift = np.fft.ifftshift(filtered_dft)
img_filtered = np.fft.ifft2(f_ishift)
img_filtered = np.abs(img_filtered)

# Step 6: Display results
plt.figure(figsize=(12,6))

plt.subplot(2,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(np.log(1 + np.abs(dft_shift)), cmap='gray')
plt.title('Fourier Spectrum (Centered)')
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(mask, cmap='gray')
plt.title(f'ILPF Mask (D0={D0})')
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(np.log(1 + np.abs(filtered_dft)), cmap='gray')
plt.title('Filtered Spectrum')
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(img_filtered, cmap='gray')
plt.title('Filtered Image (Smoothed)')
plt.axis('off')

plt.tight_layout()
plt.show()
