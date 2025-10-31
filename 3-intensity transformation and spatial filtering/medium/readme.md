# Experiment 2: Histogram Equalization and Specification
<a href="https://opencv.org/">
  <img src="https://cdn.dribbble.com/users/926537/screenshots/4502924/python-2.gif" alt="Image Processing" width="1000" align="right">
</a>

## Objective
To enhance the contrast of a grayscale image using Histogram Equalization and to modify the image’s tonal distribution to match a reference image using Histogram Specification (Matching).

---

## Concept Recap

### 1. Histogram Equalization
Histogram Equalization aims to redistribute pixel intensities so that they cover the full intensity range more uniformly.  

**Formula:**  
\[
s_k = (L - 1) \sum_{j=0}^{k} p_r(r_j)
\]

Where:  
- \( p_r(r_j) \): Probability (normalized histogram) of gray level \( r_j \)  
- \( s_k \): New intensity value  

**Effect:**  
Improves contrast, especially in low-contrast (dull) images.

---

### 2. Histogram Specification (Matching)
In Histogram Specification, we modify one image’s histogram to match another (reference) image’s histogram.  

**Conceptually:**  
1. Perform histogram equalization on both images.  
2. Map the equalized histogram of the input image to match the reference histogram.  
3. Replace pixel intensities accordingly.  

**Effect:**  
Makes one image appear as if it has the tonal characteristics of another.

---

## Tools and Libraries Used
- cv2 — for reading and processing images  
- numpy — for histogram manipulation  
- matplotlib.pyplot — for displaying and plotting  

---

## Images Used

| Type | Image | Reason |
|------|--------|--------|
| Input (Low Contrast) | low_contrast.png / moon.tif | Dull brightness; ideal for equalization |
| Reference (Good Contrast) | cameraman.tif / lena_gray.png | Balanced histogram for specification |

---

## Expected Output

| Image | Observation |
|--------|--------------|
| Original | Dull, low contrast |
| Equalized | Increased brightness range, higher contrast |
| Specified | Matches reference image’s tonal distribution |

---

## Experiment Insights

| Operation | Description | Effect |
|------------|--------------|--------|
| Histogram Equalization | Redistributes intensities to occupy full range | Better global contrast |
| Histogram Specification | Matches intensity distribution of another image | Customized contrast appearance |
| Equalization | Global enhancement |  |
| Specification | Targeted enhancement using reference histogram |  |

---

## Tips for Analysis
- Compare histograms carefully — equalized histograms should be flatter.  
- In specification, notice tonal resemblance to the reference image.  
- Try different reference images to observe varying results.  

---

## Summary

| Step | Operation | Description |
|------|------------|-------------|
| 1 | Read images | Input and reference |
| 2 | Equalize | Enhance contrast |
| 3 | Match histogram | Transfer tonal style |
| 4 | Display | Compare results visually and via histogram |

---

## Conclusion
- Histogram Equalization improves contrast automatically.  
- Histogram Specification allows you to match the contrast and brightness style of another image.  
- Both are powerful tools for image enhancement in the spatial domain.
