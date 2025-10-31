# Experiment 3: Frequency-Domain Image Sharpening Using Gaussian and Butterworth High-Pass Filters (HPF)

## Objective
To enhance image details and edges by applying High-Pass Filters in the frequency domain, specifically:
- Gaussian High-Pass Filter (GHPF)
- Butterworth High-Pass Filter (BHPF)

and compare their performance.

---

## Concept Recap

### 1. Idea Behind High-Pass Filtering
- Low frequencies represent smooth areas and illumination.  
- High frequencies represent edges, details, and textures.  

High-Pass Filters (HPFs) pass high frequencies and block low frequencies — resulting in image sharpening.

---

### 2. Mathematical Formulas

**(a) Gaussian High-Pass Filter:**  
\[
H(u,v) = 1 - e^{-\frac{D^2(u,v)}{2D_0^2}}
\]

**(b) Butterworth High-Pass Filter:**  
\[
H(u,v) = \frac{1}{1 + \left(\frac{D_0}{D(u,v)}\right)^{2n}}
\]

where  

\[
D(u,v) = \sqrt{(u - M/2)^2 + (v - N/2)^2}
\]

and  
- \( D_0 \) = cutoff frequency  
- \( n \) = filter order  

---

## Tools and Libraries Used
- cv2 — for image I/O  
- numpy — for DFT and filter creation  
- matplotlib.pyplot — for plotting and visualization  

---

## Which Image to Use
Use a grayscale image with strong edges and fine texture, so sharpening is clearly visible.

**Recommended examples:**
- cameraman.tif — standard reference for sharpening  
- building.png — for architectural edge enhancement  
- lena_gray.png — for smooth textures and details  
- moon.tif — for edge enhancement in natural scenes  

---

## Expected Output

| Image | Observation |
|--------|--------------|
| Original Image | Normal image with standard contrast |
| Gaussian HPF Mask | Dark center, bright edges (smooth transition) |
| Butterworth HPF Mask | Similar shape but slightly sharper transition |
| Gaussian HPF Result | Smooth edge enhancement, natural sharpening |
| Butterworth HPF Result | Stronger sharpening, slightly higher contrast edges |

---

## Experiment Insights

| Parameter | Effect |
|------------|---------|
| Cutoff (D₀) small | Emphasizes high frequencies strongly (sharp but noisy) |
| Cutoff (D₀) large | Mild sharpening |
| Filter Order (n) (for Butterworth) | Higher → steeper transition between low and high frequencies |
| Gaussian HPF | Smooth, natural edges |
| Butterworth HPF | Stronger, but risk of ringing if n is high |

---

## Comparison Summary

| Property | Gaussian HPF | Butterworth HPF |
|-----------|---------------|----------------|
| Mathematical Form | Exponential decay | Rational (controlled by order n) |
| Sharpness | Moderate | Stronger |
| Ringing Artifacts | Very low | Slightly higher for large n |
| Naturalness | High | Moderate |

---

## Summary of Steps

| Step | Operation | Description |
|------|------------|-------------|
| 1 | Read grayscale image | Input |
| 2 | Compute FFT and shift | Move origin to center |
| 3 | Create HPF masks | Gaussian & Butterworth |
| 4 | Multiply filter × spectrum | Apply in frequency domain |
| 5 | Inverse FFT | Back to spatial domain |
| 6 | Display and compare | Sharpened images |

---

## Conclusion
- Both filters enhance edges and highlight details.  
- Gaussian HPF gives smooth sharpening, best for natural scenes.  
- Butterworth HPF gives stronger sharpening, suitable for structural images (buildings, text).  
- Increasing cutoff or order adjusts the sharpening strength.  

---



<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->
