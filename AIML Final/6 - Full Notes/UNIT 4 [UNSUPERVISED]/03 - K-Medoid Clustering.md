## 1. Introduction

K-Medoid clustering divides data into **K clusters**, where each cluster is represented by one actual data point known as a **Medoid**.  
It minimizes the sum of **dissimilarities** (usually distance) between data points and the medoid of their cluster.

> The medoid is simply the **most central actual point** of a cluster.

---

## 2. What Is A Medoid?

A **medoid** is a data point **within the dataset** for which the total distance to all other points in the same cluster is minimal.

This means:

- It is a real point
    
- It best represents the center of the cluster
    
- Outliers cannot drag it away like means
    

Example concept  
If you have 10 houses and want a meetup spot **inside those houses**, you choose the house closest to all others.

---

## 3. Why Do We Need K-Medoid?

To deal with **outliers and noise** in data.

Comparison to K-Means:

- K-Means uses Mean → sensitive to outliers
    
- K-Medoid uses Actual Point → resistant to outliers
    

Because means can move far away if even one extreme value enters.

K-Medoid = Safer and more real-world friendly

---

## 4. Distance Metric Used

Can use any distance metric:

- Manhattan distance
    
- Euclidean distance
    
- Cosine dissimilarity
    
- Jaccard distance for categorical data
    

Flexibility makes it suitable for mixed data types.

---

## 5. Working of K-Medoid Algorithm (General Flow)

```
1. Select K data points as initial medoids
2. Assign each point to the nearest medoid
3. Compute total cost (sum of distances to medoid)
4. Try swapping medoids with non-medoids
5. If cost improves → accept swap
6. Repeat until no improvement
```

> Goal: Minimize total dissimilarity in clustering.

---

## 6. Popular Algorithms for K-Medoid

### a) PAM (Partitioning Around Medoids)

- Best known algorithm
    
- Accurate but slower for very large data
    

### b) CLARA (Clustering Large Applications)

- Uses sampling to reduce computation
    

### c) CLARANS (Clustering Large Applications based on Randomized Search)

- Randomized optimization for large datasets
    

Hierarchy of scalability:  
PAM (slow) → CLARA (faster) → CLARANS (fastest for huge data)

---

## 7. Example (Conceptual)

Data points:

```
2, 4, 5, 10, 12
K = 2
```

Initial Medoids: 4 and 10

Cluster assignment:

- Cluster 1 → 2, 4, 5
    
- Cluster 2 → 10, 12
    

Find new medoids:

- Cluster 1 median-like point → 4 or 5
    
- Cluster 2 median-like point → 10
    

Best medoids remain: 4 and 10  
Algorithm stops

Medoids always come from data points  
Unlike K-Means where centroids can be imaginary values.

---

## 8. Advantages

- Very robust to outliers
    
- Can work with any type of distance measure
    
- Medoids are real data → interpretability is easier
    
- Suitable for categorical + numerical mixed data
    

---

## 9. Disadvantages

- Computationally expensive for large datasets
    
- Many distance calculations needed
    
- Must specify K in advance
    
- Slower convergence than K-Means
    

---

## 10. K-Means vs K-Median vs K-Medoid

|Feature|K-Means|K-Median|K-Medoid|
|---|---|---|---|
|Cluster center|Mean|Median|Actual data point|
|Robust to outliers|Poor|Good|Excellent|
|Distance metric|Euclidean only|Manhattan|Flexible|
|Speed|Fastest|Medium|Slowest|
|Real-world representativeness|Low|Medium|High|
|Handles mixed data|No|No|Yes|

**Simple Memory Tip**  
Mean gets affected  
Median resists  
Medoid fights like a champion

---

## 11. Mathematical Formulation

Minimize:

```
Total Cost (TC) = Σ Σ D(xi, mj)
```

Where:

- xi = data point
    
- mj = medoid of cluster j
    
- D = chosen dissimilarity/distance metric
    

Goal: find medoids that give **minimum total dissimilarity**.

---

## 12. Applications

K-Medoid is best in noisy, real-world clustering:

- Market basket segmentation in retail
    
- Fraud detection in financial datasets
    
- Healthcare clustering (patients based on symptoms)
    
- Telecommunications network planning
    
- Transport and route optimization
    
- Social media behavior groups
    
- Facial recognition with noisy images
    

Where an actual representative sample is needed  
Medoids make results actionable.

---

## 14. Summary Box

> K-Medoid Clustering
> 
> - Unsupervised learning
>     
> - Cluster center = actual data point (medoid)
>     
> - Minimizes total dissimilarity
>     
> - Highly robust to noise and outliers
>     
> - Works on many distance metrics
>     
> - Slightly slower but more realistic
>     

Shortcut Memory  
Real data wants a real representative  
So choose medoid
https://youtu.be/FosEwkYIGmU?si=prRpmJIEDzvUFeGz
---
