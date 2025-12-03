
# **1. Introduction to Clustering**

Clustering is one of the most important techniques used in **Unsupervised Machine Learning**.  
Unsupervised learning means learning from data **without labels**, meaning the machine is not told what the correct output is. Instead, it tries to **identify patterns automatically**.

Clustering specifically focuses on **grouping similar objects** together. A cluster is a collection of data points that are similar to each other and dissimilar to points in other clusters.

### **Clustering Basic Idea**

Suppose you enter a shopping mall and observe customers buying different products.  
Even without knowing anything about them, you may notice:

- Some quickly buy essentials (milk, bread, vegetables)
    
- Some spend time browsing expensive items
    
- Some only buy junk food or snacks
    

These natural groups form **clusters**.

---

## ⭐ **1.1 Formal Definition of Clustering**

Clustering is the task of organizing a dataset into groups such that:

- **Points within the same group (cluster) have high similarity**
    
- **Points in different groups have low similarity**
    

Mathematically:

- Similarity is often measured using **distance metrics** (like Euclidean distance)
    
- Lesser distance → higher similarity → same cluster
    

---

## ⭐ **1.2 Why Clustering is Needed? 

Clustering is essential in real-world data analysis because:

### **1. Data is Often Unlabeled**

In industries like healthcare, finance, e-commerce, and security:

- Data is generated in enormous amounts
    
- It is impossible to manually categorize it  
    Clustering helps organize this data automatically.
    

### **2. Data Exploration and Understanding**

Before training any ML model, analysts want to understand:

- How many patterns exist?
    
- What segments naturally form?
    
- Are there any outliers?
    

Clustering answers all these.

### **3. Reduces Complexity**

Instead of working with millions of individual data points, clustering allows us to work with **cluster representatives**.

### **4. Foundation for Many ML Tasks**

Clustering is used as:

- Preprocessing step for classification
    
- Basis of recommendation engines
    
- Tool for anomaly detection
    
- Feature engineering technique
    

---

## ⭐ **1.3 Real-Life Applications of Clustering

### **1. Customer Segmentation**

Businesses use clustering to categorize customers into groups like:

- High spenders
    
- Low spenders
    
- Seasonal buyers
    
- Frequent buyers
    

This helps in:

- Personalized marketing
    
- Customized discount strategies
    
- Product recommendation
    

---

### **2. Medical Diagnosis**

Doctors analyze patient data using clustering:

- Symptoms
    
- Blood reports
    
- Medical histories
    
- Scans
    

Clustering helps identify:

- Disease subtypes
    
- Patient risk groups
    
- Response to treatments
    

---

### **3. Image Segmentation**

In image processing, clustering helps identify regions:

- In MRI → tumor vs healthy tissue
    
- In satellite images → water, forest, land, buildings
    
- In object detection → grouping similar pixels
    

---

### **4. Social Media Analytics**

Clustering helps platforms like Instagram, YouTube, and Twitter:

- Group users based on interests
    
- Suggest content
    
- Detect spam accounts
    
- Analyze trends
    

---

### **5. Fraud Detection**

Banks use clustering to detect:

- Unusual transactions
    
- Suspicious patterns
    
- New types of fraud
    

Points that do not fall into any cluster are considered **anomalies**.

---

# ⭐ **1.4 How Clustering Works?

Clustering works by measuring the **similarity or dissimilarity** between data points.  
Similarity is often calculated using **distance**.

### **Common Distance Measures**

1. **Euclidean Distance**
    
    - Straight-line distance
        
    - Used in K-Means
        
2. **Manhattan Distance**
    
    - Grid-based distance
        
    - Used in K-Medoids
        
3. **Cosine Similarity**
    
    - Used in text mining
        
    - Measures angle between vectors
        
4. **Jaccard Distance**
    
    - Used for categorical data
        
    - Measures mismatch between sets
        

The algorithm groups points that are **closest** in terms of distance.

---

# ⭐ **1.5 Clustering Process (Step-by-Step)**

1. **Input dataset**
    
    - Contains unlabeled data
        
2. **Choose similarity measure**
    
    - Euclidean, Manhattan, etc.
        
3. **Select clustering algorithm**
    
    - K-Means, Hierarchical, DBSCAN, etc.
        
4. **Algorithm identifies natural groupings**
    
5. **Output clusters**
    
    - Each cluster contains similar points
        

---

# ⭐ **1.6 Simple Diagram to Visualize Clustering**

### **Before Clustering**

```
•  •      •    •       •   •
      •     •      •
```

### **After Clustering**

```
Cluster 1 (Red):      ● ● ● ●
Cluster 2 (Blue):     ▲ ▲ ▲ 
Cluster 3 (Green):    ■ ■ ■ ■
```

---

# ⭐ **1.7 Numerical Example – Distance Used in Clustering**

Let two points be:  
A(2,3), B(6,9)

### **Euclidean Distance**

d = sqrt{ (6-2)^2 + (9-3)^2 }  
= sqrt{52}  
= 7.21  

### **Manhattan Distance**

d = |6-2| + |9-3| = 10  

Lower distance = higher similarity → same cluster.

---

# ⭐ **TOPIC 2: TYPES OF CLUSTERING 

Clustering techniques differ in how they form clusters.  
Here are the **major types**, explained in full detail.

---

# **2.1 Hard Clustering (Exclusive Clustering)**

In hard clustering:

- Each data point belongs to **only one** cluster
    
- No overlapping
    
- Clusters are clearly separated
    

### **Example:**

If we group students based on height:

- Cluster 1: Short
    
- Cluster 2: Medium
    
- Cluster 3: Tall
    

A student cannot be “both short and medium”.

### **Algorithm Example**

- K-Means
    

### **When to Use**

- When clusters are clearly separated
    
- When you want strict grouping
    

---

# **2.2 Soft Clustering (Fuzzy Clustering)**

In soft clustering:

- Each data point can belong to **multiple clusters** with probabilities
    
- Suitable when cluster boundaries are not clear
    

### **Example**

A movie may be:

- 40% Comedy
    
- 30% Drama
    
- 30% Romance
    

### **Algorithm Example**

- Gaussian Mixture Models (GMM)
    

### **When to Use**

- For natural overlaps (e.g., emotions, topics, user interests)
    

---

# **2.3 Partitioning Clustering**

This clustering **divides data into K non-overlapping clusters**.

It chooses:

- **Centroid → K-Means**
    
- **Medoid → K-Medoids**
    
- **Mode → K-Modes**
    

The goal is to minimize intra-cluster dissimilarity.

### **Examples**

- K-Means
    
- K-Medoids
    
- K-Modes
    

---

# **2.4 Hierarchical Clustering**

Hierarchical clustering builds a **tree-like structure (dendrogram)** of clusters.

Two approaches:

---

## ⭐ **A. Agglomerative (Bottom-Up) – AGNES**

- Start with **each point as a separate cluster**
    
- Merge clusters step-by-step based on similarity
    
- Ends with **one big cluster**
    

### **Used When**

- Number of clusters is unknown
    
- Need detailed cluster relationships
    

---

## ⭐ **B. Divisive (Top-Down) – DIANA**

- Start with **one big cluster**
    
- Recursively split into smaller clusters
    

### **Used When**

- Big clusters need to be split finely
    
- Need opposite of AGNES
    

---

### **Dendrogram Example**

```
          ┌────────────── A
     ┌────┤
     │    └────────────── B
─────┤
     │       ┌─────────── C
     └───────┤
             └─────────── D
```

Height shows similarity.

---

# **2.5 Density-Based Clustering**

Clusters are formed based on point **density**.

### **High-density area → Cluster**

### **Low-density area → Noise**

### **Why Important?**

It can identify:

- Arbitrary shapes
    
- Non-linear boundaries
    
- Noise and outliers
    

### **Algorithm Example**

- DBSCAN
    

### **Used In**

- Geographic data
    
- Spatial analysis
    
- Real-world noisy datasets
    

---

# ⭐ **2.6 Grid-Based Clustering**

- Divides data into **grids (cells)**
    
- Each cell’s density determines clusters
    
- Very fast for huge datasets
    

**Example Algorithms:**

- STING
    
- CLIQUE
    

---

# ⭐ **2.7 Model-Based Clustering**

Assumes data is generated by different statistical models.

Example:

- Gaussian Mixture Models (GMM)
    
    - Each cluster = Gaussian distribution
        

Used in:

- Speech recognition
    
- Probability-based classification
    

---

# ⭐ **2.8 Summary – Differences Between Clustering Types 

|Type|Explanation|Best For|
|---|---|---|
|Hard Clustering|Each point in **one** cluster|Clear, separate clusters|
|Soft Clustering|Points belong to **multiple** clusters|Overlapping data|
|Partitioning|Dividing data into **K groups**|Medium data, simple structure|
|Hierarchical|Tree-based merging/splitting|Unknown K, analysis|
|Density-Based|Clusters = dense regions|Arbitrary shapes, noise|
|Grid-Based|Divide space into grids|Huge datasets|
|Model-Based|Statistical distribution models|Complex structures|

---
![[Pasted image 20251202202614.png]]