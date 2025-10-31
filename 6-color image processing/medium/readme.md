# Experiment 2: RGB ↔ HSI Color Space Conversion and Intensity Adjustment

## Objective
To understand color space conversion by transforming an RGB image to the HSI (Hue, Saturation, Intensity) color model, modifying the intensity component, and converting it back to RGB.

---

## Concept Recap

| Model | Components | Description |
|--------|-------------|--------------|
| RGB | Red, Green, Blue | How colors are stored in most images |
| HSI | Hue, Saturation, Intensity | Represents color as perceived by humans; allows brightness control without changing hue |

HSI is closer to human perception of color — enabling independent adjustment of brightness while preserving color tone.

---

## You’ll Use
- cv2 — for reading images and basic operations  
- numpy — for channel-level mathematical processing  
- matplotlib.pyplot — for displaying results  

---

## Which Image to Use
You can use any colorful natural image such as:

- color_image.jpg (rename accordingly)  
- Lena.png  
- Peppers.png  
- Flowers.jpg  
- Landscape.jpg  

Ensure the image contains a good mix of colors and brightness variations so that intensity adjustments are clearly visible.

---

## Expected Output

| Before | After |
|---------|--------|
| Original RGB Image | Same image, but noticeably brighter with preserved colors |

### Observations
- Hue (color tone) and saturation remain the same.  
- Intensity (brightness) increases uniformly.  

---

## Experiment Notes

| Parameter | Description |
|------------|-------------|
| I_new = np.clip(I * 1.3, 0, 1) | Controls brightness; use <1.0 to darken |
| H & S remain unchanged | Color tones preserved |
| Output | Demonstrates perceptual color processing in HSI space |
