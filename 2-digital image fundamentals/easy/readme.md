**Experiment 1: Image Sampling and Quantization**

**Objective**

To study how sampling (spatial resolution) and quantization (intensity resolution) affect image quality in digital images.

1️⃣ Image Sampling

Reduces the number of pixels in an image.

Controls spatial resolution.

Fewer samples → image becomes blocky or pixelated.

2️⃣ Image Quantization

Reduces the number of gray levels (intensity values).

Controls intensity resolution.

Fewer levels → produces banding or posterization effects.

🧰 Tools & Libraries

✅ OpenCV (cv2) – Image loading and resizing

✅ NumPy – Mathematical and quantization operations

✅ Matplotlib.pyplot – Visualization and comparison

🧾 Expected Output
Operation	Observation
Sampling ↓	Image becomes blocky, edges jagged
Quantization ↓	Gradual tones lost, visible gray “steps” appear
Sampling + Quantization	Combined loss of detail and smoothness
⚙️ Experiment Insights
Concept	Description	Effect
Sampling	Reduces spatial detail	Image becomes pixelated
Quantization	Reduces gray levels	Image loses smooth shading
Higher Resolution	More information stored	Better quality
Lower Resolution	Less information stored	Poor quality, smaller file size
✅ Step-by-Step Summary
Step	Operation	Description
1	Load grayscale image	Input test image
2	Downsample	Reduce spatial resolution
3	Quantize	Reduce intensity levels
4	Visualize	Compare original, sampled, quantized, and combined results
🧩 Suggested Test Image

Use standard grayscale test images such as:

cameraman.tif

lena_gray.gif

peppers.png

These are classical images recommended in Chapter 2 – Digital Image Fundamentals of Gonzalez & Woods

Gonzales,Woods-Digital.Image.Pr…


🧠 Conclusion

Sampling controls spatial resolution → fewer pixels → less detail.

Quantization controls intensity resolution → fewer gray levels → less tonal smoothness.

Both directly influence perceived image quality, crucial in compression, transmission, and display systems.
