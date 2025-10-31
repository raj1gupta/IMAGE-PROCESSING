import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load grayscale image
img = cv2.imread('moon.tif', 0)
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'cameraman.tif' is in this folder.")

# Step 2: Perform Fourier Transform and shift to center
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

# Step 3: Create Gaussian Low-Pass Filter (GLPF)
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
D0 = 50  # cutoff frequency

# Create GLPF mask
U, V = np.meshgrid(np.arange(cols), np.arange(rows))
D = np.sqrt((U - ccol)**2 + (V - crow)**2)
H_gaussian = np.exp(-(D**2) / (2 * (D0**2)))

# Step 4: Also create Ideal Low-Pass Filter for comparison
H_ideal = np.zeros((rows, cols))
H_ideal[D <= D0] = 1

# Step 5: Apply both filters
filtered_gaussian = dft_shift * H_gaussian
filtered_ideal = dft_shift * H_ideal

# Step 6: Inverse FFT to get spatial domain images
img_gaussian = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_gaussian)))
img_ideal = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_ideal)))

# Step 7: Display results
plt.figure(figsize=(13,8))

plt.subplot(2,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(np.log(1 + np.abs(dft_shift)), cmap='gray')
plt.title('Centered Fourier Spectrum')
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(H_gaussian, cmap='gray')
plt.title(f'Gaussian LPF (D0={D0})')
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(img_ideal, cmap='gray')
plt.title('Ideal LPF Output')
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(img_gaussian, cmap='gray')
plt.title('Gaussian LPF Output')
plt.axis('off')

plt.subplot(2,3,6)
plt.imshow(np.log(1 + np.abs(filtered_gaussian)), cmap='gray')
plt.title('Filtered Spectrum (Gaussian)')
plt.axis('off')

plt.tight_layout()
plt.show()
