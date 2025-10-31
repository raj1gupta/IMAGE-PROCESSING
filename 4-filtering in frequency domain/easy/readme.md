# Experiment 1: Implement an Ideal Low-Pass Filter (ILPF)

## Objective
To smooth an image by removing high-frequency components (edges and noise) using an Ideal Low-Pass Filter in the frequency domain.

---

## Concept Recap

### 1. Theoretical Background
In the frequency domain, filtering is performed by:
1. Taking the Fourier Transform of the image.
2. Multiplying by a filter mask (such as ILPF).
3. Applying the Inverse Fourier Transform to reconstruct the filtered image.

---

### 2. Ideal Low-Pass Filter (ILPF)
The transfer function for the Ideal Low-Pass Filter is:

\[
H(u,v) =
\begin{cases} 
1, & D(u,v) \le D_0 \\
0, & D(u,v) > D_0
\end{cases}
\]

where  

\[
D(u,v) = \sqrt{(u - M/2)^2 + (v - N/2)^2}
\]

and  
- \( D_0 \): cutoff frequency  
- \( D(u,v) \): distance from the center of the frequency plane  

**Interpretation:**  
- Low frequencies (smooth regions) are allowed to pass.  
- High frequencies (edges and noise) are blocked.

---

## Which Image to Use
Use a grayscale image containing edges and fine details to visualize smoothing effectively.

**Recommended images:**
- cameraman.tif — classic standard in DIP
- lena_gray.png
- building.png
- moon.tif
- peppers_gray.png

Cameraman.tif is particularly suitable for this experiment.

---

## Expected Output

| Image | Observation |
|--------|--------------|
| Original Image | Sharp edges and full detail |
| Fourier Spectrum | Bright center (low frequencies), darker edges (high frequencies) |
| ILPF Mask | White circular region at center (passes low frequencies) |
| Filtered Spectrum | Only low frequencies retained |
| Filtered Image | Smoothed or blurred version of the original image |

---

## Experiment Insights

| Parameter | Effect |
|------------|---------|
| Cutoff (D₀) small | Strong blur (heavy smoothing) |
| Cutoff (D₀) large | Mild blur (preserves more details) |
| Ideal Filter | Sharp cutoff can cause ringing artifacts in output |

---

## Extension Ideas (Optional)
- Experiment with different cutoff values (e.g., D₀ = 20, 50, 100) to observe varying degrees of blur.  
- Compare the ILPF with a Gaussian Low-Pass Filter (GLPF) for smoother results without ringing effects.

---

## Summary of Steps

| Step | Operation | Concept |
|------|------------|----------|
| 1 | Read grayscale image | Input image |
| 2 | Compute DFT and shift | Convert to frequency domain |
| 3 | Create ILPF mask | Allow low frequencies to pass |
| 4 | Multiply with DFT | Apply the filter |
| 5 | Inverse FFT | Return to spatial domain |
| 6 | Display results | Visualize smoothed output |

---

## Conclusion
The Ideal Low-Pass Filter effectively smooths an image by removing high-frequency components.  
However, due to its sharp cutoff, it may introduce ringing artifacts near edges.  
It serves as a fundamental baseline for understanding frequency-domain filtering before moving to smoother alternatives like the Gaussian Low-Pass Filter (GLPF).
