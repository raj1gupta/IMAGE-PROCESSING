# Experiment 1: Image Sampling and Quantization

## Objective
To study the effects of sampling (spatial resolution) and quantization (intensity resolution) on image quality.

---

## Concepts

### 1. Image Sampling
Reducing the number of pixels in an image.  
Controls **spatial resolution** — fewer samples → image looks blocky or pixelated.

### 2. Image Quantization
Reducing the number of gray levels per pixel.  
Controls **intensity resolution** — fewer levels → banding or posterization effect.

---

## Tools Used
- OpenCV (`cv2`) – for image loading and resizing  
- NumPy – for quantization operations  
- Matplotlib (`matplotlib.pyplot`) – for visual comparisons  

---

## Recommended Images

Use a grayscale image with smooth gradients and details to clearly observe resolution and quantization effects.

| Image | Reason |
|--------|---------|
| cameraman.tif | Standard test image with good mix of edges and smooth areas |
| lena_gray.png | Smooth gradients and fine details |
| building.png | Strong edges (clear sampling effects) |
| peppers_gray.png | Useful for quantization effects |

---

## Expected Output

| Operation | Observation |
|------------|--------------|
| Sampling ↓ | Image becomes blocky; edges appear jagged |
| Quantization ↓ | Gradual tones lost; visible gray “steps” appear |
| Sampling + Quantization | Combined loss of detail and smoothness |

---

## Experiment Insights

| Concept | Description | Effect |
|----------|--------------|--------|
| Sampling | Reduces spatial detail | Image becomes pixelated |
| Quantization | Reduces gray levels | Image loses smooth shading |
| Higher Resolution | More information stored | Better quality |
| Lower Resolution | Less information stored | Poor quality but smaller file size |

---

## Summary

| Step | Operation | Description |
|------|------------|--------------|
| 1 | Load grayscale image | Input image |
| 2 | Downsample | Reduce spatial resolution |
| 3 | Quantize | Reduce gray levels |
| 4 | Visualize | Compare all results |

---

## Conclusion
Sampling controls **spatial resolution** — fewer pixels mean less detail.  
Quantization controls **intensity resolution** — fewer gray levels mean less tonal smoothness.  
Both directly affect image quality and are fundamental to image compression and display technology.
