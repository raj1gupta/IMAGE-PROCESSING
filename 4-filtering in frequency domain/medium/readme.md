# Experiment 2: Apply Gaussian Low-Pass Filter (GLPF) and Compare with Ideal Filter

## Objective
To perform image smoothing in the frequency domain using a Gaussian Low-Pass Filter (GLPF) and compare the results with the Ideal Low-Pass Filter (ILPF).

---

## Concept Recap

### 1. Why Gaussian Low-Pass Filter?
- The Ideal filter cuts frequencies sharply, which causes ringing (ripples around edges).  
- The Gaussian filter smoothly decreases the frequency response, producing a more natural blur.

---

### 2. Mathematical Formula
The transfer function for the Gaussian Low-Pass Filter is:

\[
H(u,v) = e^{-\frac{D^2(u,v)}{2D_0^2}}
\]

where  

\[
D(u,v) = \sqrt{(u - M/2)^2 + (v - N/2)^2}
\]

and  

- \( D_0 \): cutoff frequency (controls the blur amount)

**Effect:**  
High frequencies (edges, noise) are reduced gradually instead of being cut abruptly.

---

## Tools and Libraries Used
- cv2 – to read the image  
- numpy – to compute Fourier Transform and create filters  
- matplotlib.pyplot – to visualize results  

---

## Which Image to Use
Use a grayscale image with sharp details and edges (so blurring is clearly visible).

**Recommended images:**
- cameraman.tif — best for this experiment (standard in DIP)
- lena_gray.png
- building.png
- moon.tif
- peppers_gray.png

If you don’t have these, use any clear grayscale photo (convert color → grayscale using `cv2.cvtColor()` if needed).

---

## Expected Output

| Image | Observation |
|--------|--------------|
| Original Image | Normal sharp image |
| Gaussian LPF Mask | Smooth, grayish circle (gradual decay from center) |
| Ideal LPF Mask | Sharp-edged white circle (abrupt cutoff) |
| Ideal LPF Output | Strong blur, with possible ringing near edges |
| Gaussian LPF Output | Smooth blur, more natural and gentle |

---

## Experiment Insights

| Parameter | Effect |
|------------|---------|
| Cutoff Frequency (D₀) small | Strong blur (removes most details) |
| Cutoff Frequency (D₀) large | Slight blur (preserves details) |
| Gaussian Filter | Smooth falloff → no ringing artifacts |
| Ideal Filter | Sharp cutoff → visible ripples (ringing) |

---

## Conceptual Comparison

| Property | Ideal LPF | Gaussian LPF |
|-----------|------------|--------------|
| Transition | Abrupt | Smooth |
| Ringing | High | None |
| Realism | Less natural | More natural |
| Computation | Simple | Slightly complex (exponential) |

---

## Summary of Steps

| Step | Operation | Description |
|------|------------|-------------|
| 1 | Read grayscale image | Input data |
| 2 | Compute DFT | Convert to frequency domain |
| 3 | Create Gaussian LPF | Smooth attenuation of high frequencies |
| 4 | Apply filter | Multiply DFT × mask |
| 5 | Inverse FFT | Convert back to spatial domain |
| 6 | Display and compare | Ideal vs Gaussian smoothing |

---

## Conclusion
- Both filters smooth the image by suppressing high frequencies.  
- Gaussian LPF provides smoother results without ringing artifacts.  
- Ideal LPF causes unnatural transitions and edge ripples.  
