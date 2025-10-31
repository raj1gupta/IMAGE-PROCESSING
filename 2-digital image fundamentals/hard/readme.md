# Experiment 3: RGB → Grayscale → Binary Conversion

## Objective
To understand and implement how a color image is represented in digital form and how to convert it into grayscale and binary representations for further processing.

## Concept Recap

### 1. RGB Color Image
A color image consists of three channels — Red (R), Green (G), and Blue (B).  
Each pixel has three intensity values:  
**(R, G, B) ∈ [0, 255]**

### 2. Grayscale Image
Converts RGB to a single intensity channel representing brightness.  
Human eyes are more sensitive to green, so the weighted formula is:  

**Gray = 0.299R + 0.587G + 0.114B**  

**Effect:** Removes color, preserves brightness and contrast.

### 3. Binary Image
Converts grayscale to only two levels: 0 (black) or 255 (white) using a threshold value **T**:

g(x,y) = 255, if f(x,y) > T
g(x,y) = 0, if f(x,y) ≤ T


**Effect:** Simplifies the image for segmentation and object detection.

## Tools Used
- OpenCV (`cv2`) – Image input/output and conversions  
- NumPy – Numerical operations  
- Matplotlib (`matplotlib.pyplot`) – Visualization  

## Recommended Image
Use a color image with clear objects and brightness variation for better results.

| Image | Reason |
|--------|--------|
| peppers.png | Classic color test image; ideal for RGB → grayscale conversion |
| fruits.jpg | High color diversity; shows tone compression well |
| lena_color.jpg | Balanced brightness and smooth gradients |
| building_color.jpg | Strong edges and clear threshold separation |

If none of these are available, use any colorful image and rename it as `peppers.png`.

## Expected Output

| Image Type | Description |
|-------------|--------------|
| RGB Image | Full color — 3 channels (R, G, B) |
| Grayscale Image | Intensity-based brightness — 1 channel |
| Binary Image | Two levels (0 and 255) — object vs. background |

## Experiment Insights

| Process | Input | Output | Observation |
|----------|--------|---------|--------------|
| RGB → Grayscale | 3 channels | 1 channel | Removes color, keeps brightness |
| Grayscale → Binary | Continuous gray tones | Black & white image | Simplifies segmentation |
| Threshold (T) | Controls binary separation | Varies object/background ratio | Choose carefully or use Otsu’s method |

## Summary

| Step | Operation | Description |
|------|------------|--------------|
| 1 | Load RGB image | Input color image |
| 2 | Convert to Grayscale | Weighted brightness conversion |
| 3 | Apply Threshold | Binary segmentation |
| 4 | Display results | Compare visually |

## Conclusion
RGB → Grayscale conversion compresses color information into luminance.  
Grayscale → Binary conversion isolates objects by intensity thresholding.  
These steps are fundamental for image segmentation, pattern recognition, and object detection.
