## AGNES Algorithm (Agglomerative Nesting)

---
## 1. Introduction

AGNES is a **hierarchical clustering** algorithm that follows a **bottom-up approach**.

Meaning:  
Start with each data point as a **single cluster** and gradually **merge** them until all points belong to one cluster.

AGNES builds the cluster structure step-by-step and displays it using a **dendrogram**.

---

## 2. Key Idea

Merge the **two closest clusters** repeatedly.

Clusters become bigger as merging continues.

> From individual → small groups → one final group

---

## 3. Steps of AGNES

```
1. Treat each data point as a separate cluster
2. Compute distance matrix between all clusters
3. Merge the two closest clusters
4. Update distance matrix using linkage method
5. Repeat until only one cluster remains
```

No splitting occurs once merged.

---

## 4. Linkage Methods Used with AGNES

- **Single Linkage** → minimum distance between clusters
    
- **Complete Linkage** → maximum distance
    
- **Average Linkage** → average pairwise distance
    
- **Centroid Linkage** → centroid distance
    

Different linkage = different dendrogram shapes

---
## AGNES Numerical Example (Bottom–Up)

---

## Given Distance Matrix

```markdown
|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 2 | 6 |10 |
| B | 2 | 0 | 5 | 9 |
| C | 6 | 5 | 0 | 4 |
| D |10 | 9 | 4 | 0 |
```

## Step-by-Step Clustering (Using Single Linkage)

### Step 1

Find shortest distance:  
A – B = 2  
→ Merge (A, B)

Current clusters:

```
{AB}, {C}, {D}
```

### Updated Distance Matrix

Rule: Single linkage → minimum distance

```markdown
|     | AB | C | D |
|-----|----|---|---|
| AB  | 0  | 5 | 9 |
| C   | 5  | 0 | 4 |
| D   | 9  | 4 | 0 |
```

---

### Step 2

Next shortest distance:  
C – D = 4  
→ Merge (C, D)

Current clusters:

```
{AB}, {CD}
```

### Updated Distance Matrix

Distances between AB and CD:

- AB–C = 5
    
- AB–D = 9  
    → Single linkage: min = 5
    

```markdown
|     | AB | CD |
|-----|----|----|
| AB  | 0  | 5  |
| CD  | 5  | 0  |
```

---

### Step 3

Next shortest distance:  
AB – CD = 5 → Merge all

Final cluster:

```
{ABCD}
```

---

### Final Dendrogram Formation Order

1. A, B merge first
    
2. C, D merge second
    
3. (AB) merges with (CD)
    

---

## 6. Advantages

- No need to predefine number of clusters
    
- Dendrogram shows clear merging hierarchy
    
- Simple interpretation
    

---

## 7. Disadvantages

- Once merged → cannot undo
    
- Slow for large datasets (time complexity high)
    
- Can be sensitive to outliers (especially single linkage)
    

---

## 8. Applications

- Bioinformatics (gene grouping)
    
- Text mining
    
- Social network structure discovery
    
- Image analysis
    
- Market segmentation
    

---

## 10. Summary Box

> AGNES
> 
> - Bottom-up approach
>     
> - Starts with individual points
>     
> - Repeatedly merges closest clusters
>     
> - Represented with dendrogram
>     
> - Popular hierarchical clustering technique
>     

Mnemonic:  
**AGNES = Aggregates clusters upward**

---

---

# DIANA Algorithm (Divisive Analysis)

---

## 1. Introduction

DIANA is a **hierarchical clustering** algorithm that follows a **top-down approach**.

Meaning:  
Start with **one single cluster** and **split** it step-by-step into smaller clusters.

Opposite concept of AGNES.

---

## 2. Key Idea

Split the **most dissimilar** points first.

Clusters become smaller as splitting continues.

> From one large group → separated meaningful groups → individual points

---

## 3. Steps of DIANA

```
1. Start with all data points in one cluster
2. Find the most dissimilar object in the cluster
3. Move it to a new cluster
4. Check if other points are closer to the new cluster than old
5. Continue splitting until each point becomes individual or desired clusters reached
```

---

## 4. Dissimilarity Concept in DIANA

- Identifies **largest internal distance**
    
- Object most far away → most likely outlier → split first
    

Very useful to detect **strong subgroup separation** and **outliers**

---

# DIANA Numerical Example (Top–Down)

---

## Given Distance Matrix

```markdown
|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 2 | 6 |10 |
| B | 2 | 0 | 5 | 9 |
| C | 6 | 5 | 0 | 4 |
| D |10 | 9 | 4 | 0 |
```

## Step-by-Step Clustering

### Step 1

Start with one large cluster:

```
{A, B, C, D}
```

Find most dissimilar object:  
D has large distances (10, 9, 4)  
→ Split out D

Clusters:

```
{A, B, C}, {D}
```

---

### Step 2 (Inside {A,B,C})

Largest separation:  
A – C = 6  
→ Split C

Clusters:

```
{A, B}, {C}, {D}
```

---

### Step 3 (Inside {A,B})

A – B = 2 (close)  
→ Stop splitting here

Final clusters:

```
{A, B}, {C}, {D}
```

---

### Final Splitting Order

1. D split first (outlier)
    
2. Then C split out
    
3. A & B stay together
    

---

## 6. Advantages

- Detects outliers early
    
- Good when dataset has clear category separation
    
- Provides strong structural insight
    

---

## 7. Disadvantages

- Very computationally expensive
    
- Requires analyzing dissimilarities repeatedly
    
- Less commonly used on large datasets
    

---

## 8. Applications

- Fraud detection
    
- Population-based grouping
    
- Medical diagnosis classifications
    
- Detecting abnormal behavior groups
    

Outliers detected as first splits.

---

## 10. Summary Box

> DIANA
> 
> - Top-down approach
>     
> - Starts with one big cluster
>     
> - Splits using dissimilarity
>     
> - Good for detecting outliers
>     
> - Computationally heavy
>     

Mnemonic:  
**DIANA = Divides clusters downward**

---

### Combined Comparison Table: Agglomerative vs Divisive Clustering

|S.No.|Parameters|Agglomerative Clustering|Divisive Clustering|
|---|---|---|---|
|1|Category|Bottom-up approach|Top-down approach|
|2|Approach|Each data point starts in its own cluster, and the algorithm recursively merges the closest pairs of clusters until a single cluster containing all data points is formed.|All data points start in one single cluster, and the algorithm recursively splits it into smaller sub-clusters until each data point is in its own cluster.|
|3|Complexity Level|More computationally expensive for large datasets due to calculation of pairwise distances.|Comparatively less expensive as splitting focuses on inter-cluster distances, reducing computation.|
|4|Outliers|Handles outliers better because they can be absorbed into larger clusters.|Often creates separate clusters around outliers, leading to suboptimal grouping.|
|5|Interpretability|Highly interpretable; dendrogram shows full merging hierarchy, allowing user-selected cluster granularity.|Less interpretable; dendrogram shows splits and user must decide a stopping criterion to obtain clusters.|
|6|Implementation Support|Well supported in Scikit-learn with Ward, Complete, Average, and Single linkage options.|Not currently implemented in Scikit-learn.|
|7|Applications / Examples|Image segmentation, Customer segmentation, Social network analysis, Document clustering, Genetics & genomics, etc.|Market segmentation, Anomaly detection, Biological classification, Natural language processing, etc.|

---
