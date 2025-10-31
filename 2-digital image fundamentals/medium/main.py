import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a simple binary image (7x7)
img = np.zeros((7,7), dtype=np.uint8)

# Make a few white pixels (foreground)
img[3,3] = 255  # central pixel
img[3,2] = 255  # left neighbor
img[3,4] = 255  # right neighbor
img[2,3] = 255  # top neighbor
img[4,3] = 255  # bottom neighbor
img[2,2] = 255  # top-left diagonal
img[4,4] = 255  # bottom-right diagonal

# Step 2: Select central pixel coordinates
x, y = 3, 3

# Step 3: Define neighbor positions
neighbors_4 = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
neighbors_8 = neighbors_4 + [(x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]

# Step 4: Visualization
plt.figure(figsize=(8,4))

# 4-Neighborhood
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('4-Neighborhood Visualization')

# Highlight 4 neighbors in red
for (i,j) in neighbors_4:
    plt.scatter(j, i, color='red', s=100)

# Highlight central pixel in blue
plt.scatter(y, x, color='blue', s=120, label='Central Pixel')
plt.legend(loc='upper right')

# 8-Neighborhood
plt.subplot(1,2,2)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('8-Neighborhood Visualization')

# Highlight 8 neighbors in green
for (i,j) in neighbors_8:
    plt.scatter(j, i, color='lime', s=100)

# Highlight central pixel in blue
plt.scatter(y, x, color='blue', s=120, label='Central Pixel')
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()
