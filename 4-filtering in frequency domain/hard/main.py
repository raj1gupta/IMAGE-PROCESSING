import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load grayscale image
img = cv2.imread('cameraman.tif', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'cameraman.tif' is in this folder.")

# Step 2: Perform Fourier Transform and shift origin to center
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

# Step 3: Create High-Pass Filters
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
D0 = 40  # Cutoff frequency
n = 2    # Order of Butterworth filter

# Meshgrid for distance calculation
U, V = np.meshgrid(np.arange(cols), np.arange(rows))
D = np.sqrt((U - ccol)**2 + (V - crow)**2)

# (a) Gaussian High-Pass Filter (GHPF)
H_gaussian = 1 - np.exp(-(D**2) / (2 * (D0**2)))

# (b) Butterworth High-Pass Filter (BHPF)
H_butterworth = 1 / (1 + (D0 / (D + 1e-5))**(2*n))

# Step 4: Apply both filters
filtered_gaussian = dft_shift * H_gaussian
filtered_butterworth = dft_shift * H_butterworth

# Step 5: Inverse FFT to get sharpened images
img_gaussian = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_gaussian)))
img_butterworth = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_butterworth)))

# Step 6: Normalize results for display
img_gaussian = cv2.normalize(img_gaussian, None, 0, 255, cv2.NORM_MINMAX)
img_butterworth = cv2.normalize(img_butterworth, None, 0, 255, cv2.NORM_MINMAX)

# Step 7: Display all results
plt.figure(figsize=(13,8))

plt.subplot(2,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(H_gaussian, cmap='gray')
plt.title(f'Gaussian HPF Mask (D0={D0})')
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(H_butterworth, cmap='gray')
plt.title(f'Butterworth HPF Mask (n={n}, D0={D0})')
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(img_gaussian, cmap='gray')
plt.title('Gaussian HPF Result')
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(img_butterworth, cmap='gray')
plt.title('Butterworth HPF Result')
plt.axis('off')

plt.subplot(2,3,6)
plt.imshow(np.log(1 + np.abs(dft_shift)), cmap='gray')
plt.title('Fourier Spectrum')
plt.axis('off')

plt.tight_layout()
plt.show()
