import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a color image (RGB)
img = cv2.imread('raj_color.jpg')
if img is None:
    raise FileNotFoundError("Image not found. Make sure 'color_image.jpg' is in this folder.")

# Convert from BGR (OpenCV default) to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_rgb = img_rgb / 255.0  # normalize to [0,1]

# Step 2: Separate RGB channels
R, G, B = img_rgb[:,:,0], img_rgb[:,:,1], img_rgb[:,:,2]

# Step 3: Compute H, S, I channels
num = 0.5 * ((R - G) + (R - B))
den = np.sqrt((R - G)**2 + (R - B)*(G - B)) + 1e-6  # avoid divide-by-zero

theta = np.arccos(num / den)

H = np.where(B <= G, theta, 2*np.pi - theta)
H = H / (2*np.pi)  # normalize hue to [0,1]

S = 1 - (3 / (R + G + B + 1e-6)) * np.minimum(np.minimum(R, G), B)
I = (R + G + B) / 3

# Step 4: Modify Intensity (increase brightness)
I_new = np.clip(I * 1.3, 0, 1)  # increase brightness by 30%

# Step 5: Convert HSI back to RGB
H = H * 2 * np.pi
R_new, G_new, B_new = np.zeros_like(H), np.zeros_like(H), np.zeros_like(H)

# Sector 1: 0 ≤ H < 2π/3
idx = (H >= 0) & (H < 2*np.pi/3)
B_new[idx] = I_new[idx] * (1 - S[idx])
R_new[idx] = I_new[idx] * (1 + (S[idx] * np.cos(H[idx])) / (np.cos(np.pi/3 - H[idx])))
G_new[idx] = 3*I_new[idx] - (R_new[idx] + B_new[idx])

# Sector 2: 2π/3 ≤ H < 4π/3
idx = (H >= 2*np.pi/3) & (H < 4*np.pi/3)
H2 = H[idx] - 2*np.pi/3
R_new[idx] = I_new[idx] * (1 - S[idx])
G_new[idx] = I_new[idx] * (1 + (S[idx] * np.cos(H2)) / (np.cos(np.pi/3 - H2)))
B_new[idx] = 3*I_new[idx] - (R_new[idx] + G_new[idx])

# Sector 3: 4π/3 ≤ H ≤ 2π
idx = (H >= 4*np.pi/3) & (H <= 2*np.pi)
H3 = H[idx] - 4*np.pi/3
G_new[idx] = I_new[idx] * (1 - S[idx])
B_new[idx] = I_new[idx] * (1 + (S[idx] * np.cos(H3)) / (np.cos(np.pi/3 - H3)))
R_new[idx] = 3*I_new[idx] - (G_new[idx] + B_new[idx])

# Stack and clip to [0,1]
rgb_new = np.dstack((R_new, G_new, B_new))
rgb_new = np.clip(rgb_new, 0, 1)

# Step 6: Display results
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title('Original RGB Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(rgb_new)
plt.title('HSI → RGB (Increased Intensity)')
plt.axis('off')
plt.show()
