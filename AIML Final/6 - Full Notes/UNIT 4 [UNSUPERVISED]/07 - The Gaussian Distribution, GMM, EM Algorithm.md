Absolutely! Let’s create **detailed, beginner-friendly yet advanced notes** on **Gaussian Distribution, Gaussian Mixture Models (GMM), and Expectation-Maximization (EM) Algorithm**. I’ll structure it so it’s easy to paste into Obsidian, with clear headings, subheadings, formulas, examples, and intuitive explanations.

---

# Gaussian Distribution, GMM, and EM Algorithm: Complete Notes

## 1. The Gaussian Distribution (Normal Distribution)

### 1.1 What is a Gaussian Distribution?

The **Gaussian Distribution**, also called **Normal Distribution**, is one of the most important probability distributions in statistics.  
It describes how values of a variable are distributed around the mean (average). Many natural phenomena (like heights, weights, test scores) follow this pattern.

**Key Idea:** Most data points cluster around the mean, and extreme values are rare.

### 1.2 Formula of Gaussian Distribution

For a **continuous random variable** (X), the probability density function (PDF) is:

[  
f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}  
]

Where:

- ( \mu ) = mean (center of the distribution)
    
- ( \sigma^2 ) = variance (spread of the distribution)
    
- ( \sigma ) = standard deviation (square root of variance)
    
- ( e ) = exponential function (~2.718)
    
- ( \pi ) = 3.14159
    

**Intuition:**

- If (x = \mu), (f(x)) is maximum → peak of the curve.
    
- As (x) moves away from (\mu), probability decreases exponentially.
    

### 1.3 Properties of Gaussian Distribution

1. **Symmetry:** The curve is symmetric about the mean.
    
2. **Bell-shaped curve:** Most values are near the mean; fewer are far from it.
    
3. **68-95-99.7 Rule:**
    
    - ~68% of data lies within 1σ
        
    - ~95% within 2σ
        
    - ~99.7% within 3σ
        
4. **Mean = Median = Mode:** All are at the center.
    

### 1.4 Standard Normal Distribution

When (\mu = 0) and (\sigma = 1), the Gaussian is called **standard normal distribution**.  
Its PDF simplifies to:

[  
f(x) = \frac{1}{\sqrt{2 \pi}} e^{-x^2/2}  
]

This is useful for calculating probabilities using **Z-scores**:

[  
Z = \frac{X - \mu}{\sigma}  
]

---

## 2. Gaussian Mixture Model (GMM)

### 2.1 What is a GMM?

Sometimes data is **not a single bell curve** but a combination of multiple distributions. For example, heights of men and women combined.  
A **Gaussian Mixture Model (GMM)** assumes that data comes from **a mixture of several Gaussian distributions** with unknown parameters.

**Key Idea:** Each data point has a probability of belonging to each Gaussian “component”.

### 2.2 Mathematical Definition

A **GMM with K components**:

[  
p(x) = \sum_{k=1}^{K} \pi_k , \mathcal{N}(x | \mu_k, \sigma_k^2)  
]

Where:

- (K) = number of Gaussian components
    
- ( \pi_k ) = weight (mixing coefficient) of component (k) (( \sum \pi_k = 1 ))
    
- ( \mathcal{N}(x | \mu_k, \sigma_k^2) ) = Gaussian PDF of component (k)
    

**Intuition:** Each Gaussian “component” contributes to the overall shape according to its weight.

### 2.3 Properties of GMM

1. Can model **complex distributions** (multi-modal, skewed).
    
2. Each component is a **normal distribution**.
    
3. **Soft clustering:** Each point has probabilities for all clusters.
    
4. Flexible: Can approximate almost any distribution if enough components are used.
    

### 2.4 Example of GMM

Suppose we have exam scores for two classes mixed together. Class A scores ~N(70, 10²), Class B scores ~N(50, 5²). The combined distribution looks bimodal. GMM can separate these two underlying distributions.

---

## 3. Expectation-Maximization (EM) Algorithm

### 3.1 What is EM?

EM is a **general algorithm to find maximum likelihood estimates** of parameters when some data is **hidden or incomplete**.

In GMM, the hidden data is **which Gaussian component each data point belongs to**.

**Steps of EM Algorithm:**

---

### 3.2 EM Algorithm Steps for GMM

**Step 0: Initialize Parameters**

- Randomly initialize ( \mu_k, \sigma_k, \pi_k ) for each Gaussian component.
    

**Step 1: Expectation (E-step)**

- Compute **responsibility** of each Gaussian for each data point:
    

[  
\gamma_{ik} = \frac{\pi_k , \mathcal{N}(x_i | \mu_k, \sigma_k^2)}{\sum_{j=1}^{K} \pi_j , \mathcal{N}(x_i | \mu_j, \sigma_j^2)}  
]

Where ( \gamma_{ik} ) = probability that (x_i) belongs to component (k).

**Step 2: Maximization (M-step)**

- Update the parameters using responsibilities:
    

[  
\mu_k = \frac{\sum_i \gamma_{ik} x_i}{\sum_i \gamma_{ik}}  
]

[  
\sigma_k^2 = \frac{\sum_i \gamma_{ik} (x_i - \mu_k)^2}{\sum_i \gamma_{ik}}  
]

[  
\pi_k = \frac{\sum_i \gamma_{ik}}{N}  
]

**Step 3: Iterate**

- Repeat E-step and M-step until convergence (parameters stop changing significantly).
    

---

### 3.3 Intuition Behind EM

- **E-step:** “Guess” which component each point belongs to.
    
- **M-step:** “Update” the Gaussian parameters based on those guesses.
    
- Repeat → gradually improves parameter estimates.
    

**Outcome:**

- EM finds **local maximum likelihood estimates** for GMM parameters.
    

---

## 4. Visualizing Gaussian, GMM, and EM

1. **Single Gaussian:** One smooth bell curve.
    
2. **GMM:** Multiple overlapping bell curves; sum gives data distribution.
    
3. **EM in Action:** Initially, guesses are random; iteratively, Gaussians move to fit the real clusters.
    

---

## 5. Applications

- **Gaussian Distribution:** Statistical analysis, hypothesis testing, quality control.
    
- **GMM:** Clustering, anomaly detection, image segmentation, speech recognition.
    
- **EM Algorithm:** Fitting models with missing/hidden data, e.g., incomplete datasets.
    

---

## 6. Summary

- **Gaussian Distribution**: Models one “bell-shaped” distribution.
    
- **GMM**: Models multiple overlapping Gaussians; captures complex patterns.
    
- **EM Algorithm**: Iteratively estimates hidden variables (like cluster assignments) and parameters; ideal for GMM fitting.
    

---
