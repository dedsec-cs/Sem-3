
# **1. Introduction to K-Means Clustering**

K-Means is the **most popular partitioning-based clustering algorithm**.  
It divides the given dataset into **K non-overlapping clusters** where each cluster is represented by a **centroid (mean)**.

The algorithm tries to minimize the **intra-cluster distance** and maximize the **inter-cluster distance**.

### **Simple Explanation**

K-Means groups data points such that:

- Every point belongs to the cluster whose **centroid is nearest**
    
- Centroid = arithmetic mean of all points in a cluster
    

---

# ⭐ **2. Key Characteristics of K-Means**

- **Partitioning approach:** Divides data into K clusters
    
- **Centroid-based:** Each cluster has a center (mean vector)
    
- **Distance measure:** Typically Euclidean distance
    
- **Iterative algorithm:** Repeats until convergence
    
- **Works for numerical data** (because means cannot be computed for categorical data)
    

---

# ⭐ **3. Steps of K-Means Algorithm 

### **Step 1: Choose the value of K**

(Number of clusters required)

### **Step 2: Initialize centroids**

Randomly pick K points as initial centers.

### **Step 3: Assign each point to the nearest centroid**

Using Euclidean distance.

### **Step 4: Recompute centroid for each cluster**

Take the mean of all points assigned to each cluster.

### **Step 5: Repeat Steps 3 and 4**

Until:

- Centroids do not change
    
- Or cluster assignments stabilize
    

### **Step 6: Final clusters obtained**

---

# ⭐ **4. Distance Measure Used**

Most common: **Euclidean Distance**

d = sqrt{ (x_2 - x_1)^2 + (y_2 - y_1)^2}  

---
# ⭐ **7. Advantages of K-Means**

1. **Simple and easy to understand**
    
2. **Very fast** – good for large datasets
    
3. **Works well when clusters are distinct**
    
4. **Scales to millions of points**
    
5. **Guaranteed convergence** (in few steps)
    

---

# ⭐ **8. Disadvantages of K-Means**

1. **Must choose K manually**
    
2. **Sensitive to initial centroids**
    
3. **Sensitive to outliers/noise**
    
4. **Works only for numeric data**
    
5. **Clusters should be spherical**
    
6. **Different runs may give different results**
    

---

# ⭐ **9. Applications of K-Means**

- Image compression
    
- Customer segmentation
    
- Market research
    
- Anomaly detection
    
- Document clustering
    
- Biology (gene expression data)
    
- Recommendation systems
    

---

# ⭐ **10. Time Complexity**

- Best case: O(n k d)
    
- Worst case: O(n^k)
    

Where:  
n = number of points  
k = number of clusters  
d = dimensions
https://youtu.be/5FpsGnkbEpM?si=jqCEo1BPtdJi6VYx
---

# ⭐ **NUMERICAL EXAMPLE 1 (Easiest possible 6-mark question)**

### Points:

(2,3), (3,3), (6,8), (8,8)

### K = 2

Initial centroids:  
C1 = (2,3)  
C2 = (6,8)

---

## **Iteration 1**

### **Assign each point to nearest centroid**

We calculate distances:

1. Point (2,3):  
    – distance to C1 = 0 → goes to C1
    
2. Point (3,3):  
    – distance to C1 is smaller → goes to C1
    
3. Point (6,8):  
    – distance to C2 = 0 → goes to C2
    
4. Point (8,8):  
    – distance to C2 is smaller → goes to C2
    

### **Clusters formed:**

Cluster 1 → (2,3), (3,3)  
Cluster 2 → (6,8), (8,8)

---

## **Recalculate Centroids**

### **New C1:**

Average of (2,3) & (3,3)  
x = (2+3)/2 = 2.5  
y = (3+3)/2 = 3  
So new C1 = (2.5,3)

### **New C2:**

Average of (6,8) & (8,8)  
x = (6+8)/2 = 7  
y = (8+8)/2 = 8  
So new C2 = (7,8)

---

## **Iteration 2**

Reassign points — assignments stay the same.  
Means centroids are stable → **algorithm stops**.

---

### ⭐ **FINAL ANSWER**

Cluster 1 = (2,3), (3,3)  
Cluster 2 = (6,8), (8,8)

---

# ⭐ **NUMERICAL EXAMPLE 2 (Very common! For exams)**

### Data:

(1,2), (1,4), (1,0), (10,2), (10,4), (10,0)

### K = 2

Initial centroids:  
C1 = (1,2)  
C2 = (10,2)

---

## **Iteration 1**

Left-side points are closer to C1  
Right-side points are closer to C2

So:

Cluster 1 = (1,2), (1,4), (1,0)  
Cluster 2 = (10,2), (10,4), (10,0)

---

## **Recalculate Centroids**

### New C1:

Mean of y = (2+4+0)/3 = 2  
x = 1 (all x = 1)  
C1 = (1,2)

### New C2:

Mean of y = (2+4+0)/3 = 2  
x = 10 (all x = 10)  
C2 = (10,2)

Centroids didn’t change → Stop.

---

### ⭐ **FINAL ANSWER**

Cluster 1: all points with x = 1  
Cluster 2: all points with x = 10

---

# ⭐ **NUMERICAL EXAMPLE 3 (1-D K-Means — very easy & frequently asked)**

### Data:

2, 4, 5, 10, 12, 15

### K = 2

Initial means:  
C1 = 4  
C2 = 12

---

## **Iteration 1**

Points near 4 → 2, 4, 5  
Points near 12 → 10, 12, 15

---

## **Recalculate Means**

### New C1:

(2+4+5)/3 = 3.67

### New C2:

(10+12+15)/3 = 12.33

Assignments won’t change → Stop.

---

### ⭐ **FINAL ANSWER**

Cluster 1 = 2, 4, 5  
Cluster 2 = 10, 12, 15

---

