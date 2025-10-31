# Experiment 3: Smoothing (Low-Pass) Filtering with Mean, Gaussian, and Median Filters

## Objective
To apply and compare the effects of different spatial smoothing filters — Mean, Gaussian, and Median — on a noisy grayscale image, in order to understand how each reduces noise and smooths the image.

---

## Concept Recap

| Filter Type | Nature | Purpose | Key Property |
|--------------|---------|----------|---------------|
| Mean (Average) | Linear | Reduces random noise | Simple averaging of neighbors |
| Gaussian | Linear | Smooths while preserving edges better | Weighted average (center > edges) |
| Median | Non-linear | Removes salt-and-pepper noise | Replaces pixel with the median of neighbors |

All three are **Low-Pass Filters** — they allow low-frequency (smooth) components to pass and suppress high-frequency (sharp/noisy) ones.

---

## Which Image to Use
Use a grayscale image with fine details or added noise for comparison.

**Recommended images:**
- noisy_image.jpg  
- cameraman.tif  
- lena_gray.png  
- peppers_gray.png  

Alternatively, you can generate a noisy version from a clean image (using salt & pepper noise).

---

## Expected Output

| Image | Effect |
|--------|---------|
| Original | Clean grayscale image |
| Noisy | Random white and black dots (salt & pepper noise) |
| Mean Filter | Smooths noise but blurs edges |
| Gaussian Filter | Better smoothing, preserves edges more |
| Median Filter | Removes salt & pepper noise effectively, edges preserved |

---

## Explanation

| Filter | Mechanism | Result |
|---------|------------|--------|
| Mean | Replaces each pixel with the average of its 5×5 neighborhood | Smooths uniformly; edges blurred |
| Gaussian | Weights central pixels more than surrounding ones | Natural blur; edges less affected |
| Median | Replaces each pixel with the median intensity value | Best for impulse noise (salt & pepper) |

---



## Conclusion
- **Mean Filtering:** Simplest technique but tends to blur fine details.  
- **Gaussian Filtering:** Produces smoother, more natural results with better edge preservation.  
- **Median Filtering:** Most effective for removing salt & pepper noise while maintaining edges.

