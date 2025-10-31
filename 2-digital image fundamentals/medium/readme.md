# Experiment 2: Pixel Neighborhoods and Adjacency Visualization

## Objective
To visualize and understand pixel neighborhoods (4-neighbors, 8-neighbors) and connectivity relationships in a binary image.

## Concept Recap

### 1. Pixel Neighborhoods
Each pixel in a digital image has neighboring pixels that define its local region.

#### (a) 4-Neighborhood (N₄)
The four directly adjacent pixels (up, down, left, right):

**N₄(p) = {(x+1, y), (x−1, y), (x, y+1), (x, y−1)}**

#### (b) Diagonal Neighbors (Nᴰ)
The four diagonal neighbors:

**Nᴰ(p) = {(x+1, y+1), (x+1, y−1), (x−1, y+1), (x−1, y−1)}**

#### (c) 8-Neighborhood (N₈)
Combines both N₄ and Nᴰ:

**N₈(p) = N₄(p) ∪ Nᴰ(p)**

---

### 2. Pixel Adjacency
Defines whether two pixels are considered connected:

- **4-adjacency:** share a side  
- **8-adjacency:** share a side or a corner  
- **m-adjacency (mixed):** avoids ambiguous connectivity  

---

## Tools Used
- NumPy – for binary image creation  
- Matplotlib – for visualization  
- OpenCV (`cv2`) – optional, for image loading and conversion  

---

## Expected Output

| Visualization | Description |
|----------------|--------------|
| 4-Neighborhood | Only top, bottom, left, right neighbors highlighted (red) |
| 8-Neighborhood | Includes diagonals (green) — total 8 surrounding pixels |
| Central Pixel | Highlighted in blue |

---

## Experiment Insights

| Concept | Description |
|----------|--------------|
| 4-Connectivity | Simplifies regions but may disconnect diagonally touching pixels |
| 8-Connectivity | Connects diagonal pixels — more inclusive |
| m-Connectivity | Hybrid approach to avoid ambiguities |

---

## Summary

| Step | Operation | Description |
|------|------------|--------------|
| 1 | Create binary image | Simple 0–255 array |
| 2 | Define pixel and neighbors | Central + surrounding |
| 3 | Visualize 4- and 8-connectivity | Using color markers |
| 4 | Compare adjacency patterns | Observe pixel relationships |

---

## Conclusion
Pixel neighborhoods define how local operations (like filtering or segmentation) are applied.  
Connectivity determines whether pixels belong to the same region.  
Understanding 4- and 8-neighbor systems is essential for region labeling, morphological operations, and edge-based segmentation.
