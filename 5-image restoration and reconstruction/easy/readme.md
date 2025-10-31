# Experiment 1: Contrast Stretching and Log Transformation

## Objective
To enhance the visual appearance of a low-contrast grayscale image using:
1. Contrast Stretching  
2. Logarithmic Transformation

---

## Concept Recap

| Technique | Formula | Purpose |
|------------|----------|----------|
| Contrast Stretching | s = ((r - r_min) / (r_max - r_min)) × 255 | Expands narrow intensity range to full [0, 255] range |
| Log Transformation | s = c · log(1 + r) | Expands dark pixel values and compresses bright ones |

Both methods enhance visibility by manipulating intensity values.

---

## You’ll Use
- cv2 — for reading and manipulating images  
- numpy — for pixel operations  
- matplotlib.pyplot — for displaying results  

---

## Which Image to Use
Use a low-contrast grayscale image so that the transformation effect is clear.

### Recommended options:
- low_contrast_image.jpg (rename yours to this name)  
- pout-dark.png  
- moon.tif  
- lowcontrast_mri.png  
- dark_room.jpg  

---

## Expected Output

| Image | Result |
|--------|---------|
| Original | Dull, low brightness and contrast |
| Contrast Stretched | Brighter, full dynamic range used |
| Log Transformed | Dark regions become more visible; highlights compressed |

---

## Experiment Insights

| Method | Effect | Suitable For |
|---------|---------|--------------|
| Contrast Stretching | Improves visibility in uniformly dull images | General low-contrast photos |
| Log Transformation | Enhances dark regions (like X-rays, satellite images) | Images with large dark areas |
