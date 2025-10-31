# Experiment 3: Image Smoothing and Sharpening Using Spatial Masks

## Objective
To perform smoothing (blurring) and sharpening (edge enhancement) on a grayscale image using spatial filters (masks) through convolution.

---

## Concept Recap

Spatial filtering works directly on the image plane, modifying each pixel based on its neighborhood.

**Mathematical Expression:**

g(x, y) = Σₛ₌₋ₐᵃ Σₜ₌₋ᵦᵇ w(s, t) ⋅ f(x + s, y + t)

Where:  
- **f(x, y)** → original image  
- **w(s, t)** → filter mask (kernel)  
- **g(x, y)** → filtered image  

---

### 1. Smoothing (Low-Pass) Filters
Reduce noise and small details by averaging nearby pixel values.

**Common Kernels:**

**Mean (Averaging) Filter (3×3):**

1/9 * [[1, 1, 1],[1, 1, 1],[1, 1, 1]]

**Gaussian Filter:** Produces a smooth blur with less distortion.

**Effect:** Blurs the image and removes noise.

---

### 2. Sharpening (High-Pass) Filters
Enhance edges and fine details by emphasizing intensity changes.

**Common Kernels:**

**Laplacian Filter:**

[[ 0, -1, 0],
[-1, 4, -1],
[ 0, -1, 0]]

**Sobel Filters:**

Gx = [[-1, 0, 1],
      [-2, 0, 2],
      [-1, 0, 1]]

Gy = [[-1, -2, -1],
      [ 0, 0, 0],
      [ 1, 2, 1]]


**Effect:** Sharpens edges and highlights boundaries.

---

## Tools Used
- OpenCV (`cv2`) – image reading and filtering  
- NumPy – defining custom kernels  
- Matplotlib (`matplotlib.pyplot`) – visualization  

---

## Recommended Images

Use a grayscale image with visible details and edges so that smoothing and sharpening effects are clear.

| Image | Reason |
|--------|---------|
| lena_gray.png | Ideal for detail and edge visualization |
| building.png | Sharp edges and textures – good for filters |
| cameraman.tif | Balanced contrast – easy to interpret |
| peppers_gray.png | Curves and gradients show smoothing well |

---

## Expected Output

| Image | Observation |
|--------|--------------|
| Original | Normal details and textures |
| Mean Filtered | Smooth, slightly blurred |
| Gaussian Filtered | Smooth with fewer artifacts |
| Median Filtered | Removes salt-and-pepper noise well |
| Laplacian Edge Map | Shows high-frequency edges |
| Sharpened Image | Edges enhanced, sharper appearance |

---

## Experiment Insights

| Filter | Type | Effect | Use Case |
|---------|------|---------|----------|
| Mean | Linear Smoothing | Blurs uniformly | Noise reduction |
| Gaussian | Linear Smoothing | Gentle blur | Pre-processing |
| Median | Non-linear | Removes impulse noise | Salt & pepper noise |
| Laplacian | High-pass | Highlights edges | Edge detection |
| Sharpened (Image + Laplacian) | Enhancement | Emphasizes edges | Image sharpening |

---

## Summary

| Step | Operation | Description |
|------|------------|--------------|
| 1 | Read grayscale image | Input |
| 2 | Apply Mean, Gaussian, Median filters | Smoothing |
| 3 | Apply Laplacian filter | Sharpening |
| 4 | Combine Laplacian + Original | Enhanced output |
| 5 | Display all results | Visual comparison |

---

## Conclusion
Smoothing filters remove noise but blur fine details.  
Sharpening filters highlight edges but may amplify noise.  
A balance of both produces clear and enhanced images for further processing.
