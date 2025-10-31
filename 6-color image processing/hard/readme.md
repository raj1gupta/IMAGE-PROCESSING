# Experiment 3: Color Image Smoothing and Sharpening Using Spatial Filtering

## Objective
To perform smoothing (blurring) and sharpening operations on a color image using spatial filters (neighborhood processing) applied to each RGB channel.

---

## Concept Recap

| Operation | Purpose | Example Filter |
|------------|----------|----------------|
| Smoothing (Low-pass) | Removes noise / reduces detail | Average filter, Gaussian filter |
| Sharpening (High-pass) | Enhances edges and details | Laplacian, High-boost filter |

We will:
- Smooth the color image using a Gaussian blur and a mean filter.  
- Sharpen the image using Laplacian filtering and unsharp masking (high-boost).

---

## You’ll Use
- cv2 — OpenCV for filters  
- numpy — for array processing  
- matplotlib.pyplot — for visualization  

---

## Which Image to Use
Choose a colorful, detailed image so that smoothing and sharpening effects are visually distinct.

### Recommended examples:
- color_image.jpg  
- Lena.png  
- Peppers.png  
- Mandrill.jpg  
- A natural or textured image (flowers, buildings, etc.)  

Ensure the image is in the same directory as your Python file.

---

## Expected Output

| Image | Effect |
|--------|---------|
| Average Filter | Smooths out edges; reduces detail (soft blur) |
| Gaussian Filter | More natural blur; edges preserved slightly |
| Laplacian Filter | Highlights edges (bright borders) |
| High-Boost | Sharpened image with stronger edges and textures |

---

## Key Concepts

| Technique | Formula | Description |
|------------|----------|-------------|
| Averaging Filter | g(x,y) = (1 / m·n) Σ f(x,y) | Replaces each pixel with the average of its neighborhood |
| Gaussian Blur | Weighted smoothing (center has more weight) | Reduces noise and preserves edges better |
| Laplacian | ∇²f = ∂²f/∂x² + ∂²f/∂y² | Detects intensity changes (edges) |
| High-Boost | g = f + k(f − f_blur) | Adds high-frequency detail to sharpen the image |

---

## Optional Extensions
- Compare **per-channel filtering** (RGB) vs **grayscale filtering**.  
- Try different kernel sizes (3×3, 5×5, 9×9) and observe blur/sharpness.  
- Implement a custom sharpening kernel:

```python
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharpen_custom = cv2.filter2D(img_rgb, -1, kernel)

## Summary Table

| Level | Experiment | Main Concept | Result |
|--------|-------------|--------------|---------|
| Easy | Intensity Slicing | Pseudocolor Visualization | False-colored grayscale |
| Medium | RGB ↔ HSI + Intensity Adjustment | Color Model Understanding | Brightened image, same hue |
| Hard | Smoothing & Sharpening | Spatial Filtering | Blur vs edge enhancement |
