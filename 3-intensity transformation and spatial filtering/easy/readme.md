# Experiment 1: Image Negative and Log Transformation

## Objective
To perform negative and logarithmic transformations on a grayscale image to enhance its visual quality and understand pixel-level intensity mapping.

---

## Concept Recap
In the spatial domain, intensity transformations operate directly on pixel values.

---

## Which Image to Use
Use a grayscale image with dark regions, where contrast enhancement is visible.

**Recommended images:**
- moon.tif (classic DIP example)
- low_light_building.jpg
- dark_room.png
- spine_xray.tif
- cameraman.tif

---

## Expected Output

| Image | Observation |
|--------|--------------|
| Original | Dull gray image with dark regions |
| Negative | Inverted brightness — dark becomes light and vice versa |
| Log Transformation | Dark regions enhanced, bright regions compressed |

---

## Experiment Insights

| Transformation | Effect | Use Case |
|----------------|---------|-----------|
| Negative | Inverts intensities | Medical or microscopic images |
| Logarithmic | Enhances low intensity, compresses high intensity | Satellite or astronomical imaging |

---

## Additional Notes
- You can adjust scaling constant **c** to control brightness.  
- For very dark images, try increasing normalization contrast.  
- Combine transformations (like sqrt or gamma correction) for advanced enhancement.

---

## Summary

| Step | Operation | Description |
|------|------------|-------------|
| 1 | Load grayscale image | Input data |
| 2 | Apply Negative Transform | Invert intensities |
| 3 | Apply Log Transform | Expand dark details |
| 4 | Display and compare | Visual + histogram analysis |

---

## 1. Image Negative Transformation

**Formula:**  
\[
s = L - 1 - r
\]

Where:  
- \( r \) = input intensity  
- \( s \) = output intensity  
- \( L \) = maximum gray level (typically 256)  

**Effect:**  
Bright regions become dark and vice versa — useful for medical images or where dark details are important.

---

## 2. Logarithmic Transformation

**Formula:**  
\[
s = c \cdot \log(1 + r)
\]

Where:  
- \( r \) = input intensity (normalized to [0,1])  
- \( c = \frac{255}{\log(1 + \max(r))} \)  

**Effect:**  
- Expands dark pixel values.  
- Compresses bright pixel values.  
- Enhances dark details — great for satellite or X-ray images.

---

## Tools and Libraries Used
- cv2 – to load images  
- numpy – for mathematical operations  
- matplotlib.pyplot – to display results  

---
