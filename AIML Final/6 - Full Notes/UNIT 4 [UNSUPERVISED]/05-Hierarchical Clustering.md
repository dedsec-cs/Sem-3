## 1. Introduction

Hierarchical clustering is an **Unsupervised Learning** technique that forms clusters in a **tree-like structure**.  
Instead of forming all clusters at once, it builds them **step-by-step**, either by merging or splitting.

Key Idea  
Similar points are grouped first, then gradually combined into bigger clusters until only one large group remains.

Output Representation  
A special diagram called a **Dendrogram**.

---

## 2. Why is it called Hierarchical?

It creates a **hierarchy** of clusters:

- Small clusters at lower levels
    
- Large groups formed by combining smaller clusters
    

This gives **multi-level** clustering  
Different cuts give different cluster numbers.

> You do not need to fix the number of clusters at the start.
![[Pasted image 20251202233429.png]]
---

## 3. Types of Hierarchical Clustering

There are **two main approaches**:

### A) Agglomerative Clustering

- Bottom-Up approach
    
- Start with each data point as an individual cluster
    
- Merge clusters step-by-step
    

Flow:

```
Every point → small clusters → merged → one final cluster
```

This is the **most commonly used** method.
![[Pasted image 20251202233453.png]]
---

### B) Divisive Clustering

- Top-Down approach
    
- Start with one large cluster
    
- Split clusters step-by-step until each point stands alone
    

Flow:

```
Single cluster → split → smaller clusters → individual points
```

Used less often due to higher computational complexity.
![[Pasted image 20251202233506.png]]
---

## 4. Dendrogram

A **tree-structured diagram** showing how clusters were formed.

How to read:

- The **vertical axis** shows dissimilarity (distance)
    
- Clusters joined at **low height** → more similar
    
- Clusters joined at **high height** → less similar
    

To choose number of clusters:

- Cut the dendrogram horizontally at a height
    
- Number of vertical lines intersected = number of clusters
    

Dendrogram reveals:

- Natural cluster count
    
- Similarity levels between clusters
    
- Outliers (nodes far apart)
    

---
# Clades in Hierarchical Clustering

## 1. What is a Clade?

A **clade** is a branch or subgroup that forms on a dendrogram during hierarchical clustering.

In simple words:  
A clade is a **set of data points** that have been grouped together because they are more similar to each other than to points in other groups.

### Key Characteristics

- Created at each **merge step** in agglomerative clustering
    
- Represents a **cluster** formed at a particular **similarity level**
    
- Found by reading the **tree structure** of the dendrogram
    

A clade grows bigger as the height of the dendrogram increases.

---

## 2. Types of Clades Based on Number of Leaves

In hierarchical clustering terminology, **leaves** are the **individual data points** at the bottom of the dendrogram.

Clades are sometimes described by **how many leaves they contain**:

|Clade Type|Meaning|Example Symbolism|
|---|---|---|
|**Simplicifolius**|A clade containing **one** leaf|A single isolated data point|
|**Bifolius**|A clade with **two** leaves|Two very similar points cluster early|
|**Trifolius**|A clade with **three** leaves|Three closely similar points|
|**Multifolius**|A clade with **more than three** leaves|Larger cluster groups|

### Intuition

- **Simplicifolius** = A point not yet merged with others
    
- **Bifolius** = A pair cluster (strong similarity)
    
- **Trifolius** = Trio forming a mini-cluster
    
- **Multifolius** = A completed cluster of multiple members

![[Pasted image 20251202233852.png]]

---

## 5. Cluster Distance Measures (Linkage Methods)

How do we decide which clusters to merge?

Different rules exist:

### 1) Single Linkage

Distance = Minimum distance between one point in cluster A and one point in cluster B

- Can form long “chain-like” clusters
    
- Sensitive to noise
    
![[Pasted image 20251202233545.png]]
### 2) Complete Linkage

Distance = Maximum distance between points in the clusters

- Forms compact clusters
    
- Less noise-sensitive
![[Pasted image 20251202233557.png]]

### 3) Average Linkage

Distance = Average pairwise distances between clusters

- Balanced approach
    

### 4) Centroid Linkage

Distance = Distance between the centroids of clusters

- Can cause inversions in dendrograms sometimes
    

Choosing linkage affects cluster shapes.
![[Pasted image 20251202233609.png]]

---
