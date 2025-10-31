# Experiment 2: Histogram Equalization and Comparison

## Objective
To enhance the contrast of a grayscale image using Histogram Equalization, and to compare the results with the original image.

---

## Concept Recap

### What is Histogram Equalization?
Histogram Equalization improves the global contrast of an image by redistributing pixel intensity values so that they span the full range (0–255).

### Mathematical Idea
If `r_k` represents intensity levels, the transformation is:

s_k = (L − 1) * Σ (from j=0 to k) p_r(r_j)

Where:  
- L = number of gray levels (usually 256)  
- p_r(r_j) = probability of intensity level r_j  
- s_k = equalized intensity  

**Result:** The histogram becomes approximately uniform, improving contrast.

---

## You’ll Use
- cv2 — to read and equalize the image  
- numpy — for histogram calculations  
- matplotlib.pyplot — for visualization  

---

## Which Image to Use
Choose a grayscale image with poor contrast — the best results come from images where brightness is concentrated in a small range.

### Recommended examples:
- gray_image.jpg (rename your image to this name)  
- pout-dark.png  
- moon.tif  
- lowcontrast_mri.png  
- building_shadow.jpg  
- Any grayscale portrait or X-ray image  

---

## Expected Output

| Image | Result |
|--------|---------|
| Original | Dull, low contrast |
| Equalized | Brighter, better contrast |
| Histogram (before) | Narrow intensity distribution |
| Histogram (after) | More uniform spread across full 0–255 range |

---

## Explanation
**Before Equalization:** Most pixels occupy a narrow intensity range → flat/dull look.  
**After Equalization:** Intensities redistributed → details in dark and bright regions appear clearer.

---

## Applications
- Medical imaging (CT, MRI)  
- Satellite and aerial image enhancement  
- Old photo restoration  
- Document enhancement (scanned text clarity)

---

## Summary

| Parameter | Original | After Equalization |
|------------|-----------|--------------------|
| Brightness Range | Narrow (e.g., 70–130) | Wide (0–255) |
| Contrast | Low | High |
| Histogram Shape | Concentrated | Spread uniformly |
| Visual Clarity | Poor | Improved |
