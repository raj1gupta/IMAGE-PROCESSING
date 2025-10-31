# Experiment 1: Intensity Slicing and Color Mapping

## Concept Recap
Intensity slicing (pseudocoloring) maps different gray-level ranges to specific colors to enhance visualization.

**Example:**
- Dark regions → Blue  
- Mid-tone regions → Green  
- Bright regions → Red  

---

## You’ll Use
- cv2 — for image I/O and manipulation  
- numpy — for pixel-level operations  
- matplotlib.pyplot — for displaying the result  

---

## How It Works

| Step | Operation | Explanation |
|------|------------|--------------|
| 1 | Load grayscale image | Input in 0–255 range |
| 2 | Create color output | 3-channel RGB result |
| 3 | Define ranges | Choose 3 intensity zones |
| 4 | Map each range to color | Mask & assign color |
| 5 | Show images | Display side-by-side |

---

## Experiment Notes
- You can use any grayscale image (`.png`, `.jpg`, `.bmp`), such as a medical scan, satellite, or Lena image.  
- You can tune ranges and colors to highlight different intensity zones.  
- Try more slices for better visualization, for example:

```python
ranges = [
    (0, 50, (0, 0, 128)),
    (51, 100, (0, 128, 255)),
    (101, 150, (0, 255, 255)),
    (151, 200, (0, 255, 0)),
    (201, 255, (255, 0, 0))
]
