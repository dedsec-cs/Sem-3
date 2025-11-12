## 1. Introduction to Machine Learning

Machine Learning (ML) is a branch of **Artificial Intelligence (AI)** that enables machines to _learn patterns from data_ and improve performance based on experience — **without being explicitly programmed**.

> Traditional programming = Rules + Data → Output  
> Machine Learning = Data + Output → Algorithm learns rules

ML algorithms learn a function:

[  
f(X) --> Y  
]

Where:

- ( X ) = input features
    
- ( Y ) = target/output we want to predict
    

---

### Why ML is needed?

- Impossible to manually define rules for large/complex data (Face recognition, Spam filtering)
    
- Massive availability of structured & unstructured data
    
- ML models adapt as patterns change
    

---

### ML Applications

- Fraud detection (finance)
    
- Disease prediction (healthcare)
    
- Self-driving cars (reinforcement learning)
    
- Recommendation systems (Netflix, Amazon)
    

---

### 📌 Diagram: Machine Learning Overview

```
                ┌─────────────────────────┐
                │     Machine Learning     │
                └─────────────┬───────────┘
                              │
      ┌───────────────────────┼────────────────────────┐
      │                       │                        │
┌──────────────┐      ┌───────────────┐       ┌────────────────┐
│ Supervised    │      │ Unsupervised  │       │ Reinforcement  │
│ (Labeled Data)│      │ (Unlabeled)   │       │ Learning        │
└─────┬─────────┘      └──────┬────────┘       └───────┬────────┘
      │                        │                        │
      │                        │                        │
┌────────────┐         ┌─────────────┐         ┌────────────────┐
│ Regression  │         │ Clustering  │         │ Agent interacts │
│ (Predict #) │         │ (Groups)    │         │ + learns policy │
└─────────────┘         └────────────┘         └────────────────┘
┌────────────┐
│ Classification │
│ (Predict Class)│
└───────────────┘
```

---

## 2. Types of Machine Learning

### ✅ 2.1 Supervised Learning

- Uses **labeled data**
    
- Learns mapping between input features ( X ) and target ( Y )
    

Examples:

- Predicting house price → Regression
    
- Classifying emails (Spam/Not spam) → Classification
    

---

### ✅ 2.2 Unsupervised Learning

- Uses **unlabeled data**
    
- Model discovers hidden patterns or structures
    

Examples:

- Customer segmentation (Clustering)
    
- Dimensionality reduction → PCA
    

---

### ✅ 2.3 Reinforcement Learning

- System (agent) interacts with environment
    
- Learns a strategy (policy) based on **reward / penalty**
    

Examples:

- Robotics movement
    
- Game playing (Chess / Pac-Man)
    

---

### 📌 Diagram: Comparison

```
Supervised        → learns from labeled data (X, Y)
Unsupervised      → learns from structure of X only
Reinforcement     → learns by interacting (actions → reward)
```

---

## 3. Feature Engineering 

Feature Engineering is **the art and science of converting raw data into meaningful features** that improve model performance.

> “Better features → better results, even with simple models.”

---

### Why Feature Engineering is Important?

|Benefit|Reason|
|---|---|
|Improves accuracy|Features carry key information|
|Reduces overfitting|Removes irrelevant/noisy data|
|Faster training|Fewer features = less computation|
|Improves interpretability|Helps explain model decisions|

---

### Major Steps in Feature Engineering

```
                ┌──────────────────────────┐
                │   RAW DATA (collected)   │
                └───────────┬─────────────┘
                            │
                            ▼
          ┌────────────────────────────────────┐
          │ 1. Data Cleaning                   │
          │ remove duplicates, fix formatting  │
          └───────────┬───────────────────────┘
                      │
                      ▼
          ┌────────────────────────────────────┐
          │ 2. Handling Missing Data            │
          │ drop / impute / flag                │
          └───────────┬───────────────────────┘
                      │
                      ▼
          ┌────────────────────────────────────┐
          │ 3. Encoding Categorical Data        │
          │ Label / One-Hot / Target encoding   │
          └───────────┬───────────────────────┘
                      │
                      ▼
          ┌────────────────────────────────────┐
          │ 4. Feature Scaling                  │
          │ Z-score / Min-Max / Robust scaling  │
          └───────────┬───────────────────────┘
                      │
                      ▼
          ┌────────────────────────────────────┐
          │ 5. Selection / Extraction           │
          │ Reduce features (Filter / PCA)      │
          └─────────────────────────────────────┘
```

---

## 4. Features and Their Types

|Type|Meaning|Examples|
|---|---|---|
|**Numerical**|Measurable numeric values|Age, Salary, Height|
|**Categorical**|Values represent categories|Gender, City|
|**Ordinal**|Categories with order|Low < Medium < High|
|**Text Features**|Derived from text|Word count, TF-IDF|
|**Datetime Features**|Derived from timestamps|Year, Month, Weekend|

---

📌 **Diagram: Types of Features**

```
                       Features
                           │
     ┌─────────────────────┼─────────────────────┐
     │                     │                     │
 Numerical           Categorical              Datetime
     │                     │                     │
 ┌────┴────┐         ┌────┴─────┐              └─> year, month,
 │Discrete │         │Nominal   │                 weekday, etc.
 │Continuous│        │Ordinal   │
 └─────────┘         └─────────┘
```

---

## 5. Handling Missing Data (Very Important)

Missing values negatively affect algorithms.

### Causes of Missing Data

- System failures (sensor not capturing value)
    
- Human entry mistake
    
- Value not applicable
    

---

### Strategies to Handle Missing Data

|Method|When to Use|
|---|---|
|**Remove rows**|When only few rows are missing|
|**Remove column**|When > 60% values are missing|
|**Impute (fill values)**|For essential features|
|**Flag missingness**|When missing value itself is meaningful|

---

📌 **Diagram: Missing Data Decision**

```
                       Missing Data?
                              │
            ┌────────┬────────┴──────────┬─────────┐
            │        │                   │          │
        Drop rows   Drop column     Impute values   Flag missing
        (rare)      (too many NA)   (mean/median)   (add feature)
```

---

## 6. Dealing with Categorical Features (Encoding)

ML algorithms **require numeric data**, so categorical values must be converted.

|Encoding|Use Case|
|---|---|
|**Label Encoding**|Ordinal categories (rating: low < medium < high)|
|**One-Hot Encoding (OHE)**|Nominal categories (city, gender)|
|**Target Encoding**|High-cardinality categories (zip code)|
|**Frequency Encoding**|Categories represent count behavior|

---

📌 **Diagram: Encoding Selection**

```
                   Categorical Feature
                            │
         ┌───────────┬───────────────┬─────────────┐
         │           │               │             │
   Is Ordered?    Few Categories?   Many?     Target correlated?
      │               │              │               │
Label Encoding     One-Hot        Frequency      Target Encoding
```

# 🔵 DEALING WITH CATEGORICAL FEATURES (Encoding)

> 📌 From PPT:
> 
> - _“Categorical variables need to be converted to numerical values before modeling.”_
>     
> - _“Encoding is required because ML algorithms cannot understand text values.”_
>     
> - _“Two types of categorical data: Nominal and Ordinal.”_
>     

Categorical features represent labels or groups.  
They can’t be directly fed into ML models because models perform numeric computations.

Examples from PPT:

- Gender (Male/Female)
    
- Stream (Arts/Commerce/Science)
    

---

### ➤ Types of Categorical Features (PPT Mapping)

|PPT Mentioned|Meaning|Examples|
|---|---|---|
|**Nominal**|No ordering between categories|City, Gender, Country|
|**Ordinal**|Ordering exists|Low < Medium < High (rating), Class levels|

---

### ➤ PPT: “Methods to encode categorical data”

```
               Handling Categorical Data
                         │
     ┌───────────────────┼──────────────────┐
     │                   │                  │
 Label Encoding     One Hot Encoding   Target/Frequency Encoding
```

---

### ✅ Label Encoding

> PPT point: _“Assigns numerical values to categories.”_

Use for: **Ordinal Data**

Example from PPT (slide with ranking example):

```
Low → 0
Medium → 1
High → 2
```

---

### ✅ One-Hot Encoding

> PPT point: _“Creates binary columns for each category.”_

Use for: **Nominal Data**

```
Gender:
Male   → [1 0]
Female → [0 1]
```

🔹 PPT mentioned the problem of **dimensionality increase** when many categories exist.

---

### ✅ Target / Frequency Encoding

> PPT point: _“Used when categories are too many.”_

Use when a feature contains **hundreds or thousands of categories**, e.g., ZIP codes, product IDs.

---

---

# 🔵 FEATURE SCALING

> 📌 From PPT:
> 
> - _“Scaling ensures all features contribute equally to the result.”_
>     
> - _“Required when data varies in magnitude.”_
>     
> - _“Improves accuracy of distance-based algorithms.”_
>     

Scaling makes numerical features fall within **similar ranges**, avoiding bias toward features with large values.

Example from PPT:

- Age → 18 to 60
    
- Salary → 30,000 to 120,000
    

---

### ➤ PPT: “When scaling is needed?”

Algorithms requiring scaling (PPT list matches this):

```
✔ K-Means
✔ K-Nearest Neighbors (KNN)
✔ Support Vector Machine (SVM)
✔ Logistic Regression
✔ Neural Networks
✔ PCA (MUST scale before PCA)
```

Algorithms where scaling is **not required** (from PPT):

```
✘ Decision Trees
✘ Random Forest
✘ XGBoost
```

---

### ➤ PPT: "Types of Scaling"

|Type (as in PPT)|Explanation|Where used|
|---|---|---|
|Standardization|Centers data|Most ML algorithms|
|Normalization|Converts to fixed range (0–1)|Neural networks|
|Robust Scaling|Uses median; handles outliers|Data with outliers|

---

### 📌 PPT Included Example

> "After scaling, all values lie in a similar range, improving model performance."

---

---

# 🔵 FEATURE SELECTION

> 📌 From PPT:
> 
> - _“Used to reduce overfitting and increase accuracy.”_
>     
> - _“Removes irrelevant or redundant features.”_
>     
> - _“Reduces computation time.”_
>     

Feature Selection identifies **the most useful features**.

---

### ➤ PPT: “Why do we select features?”

|PPT Benefit|Meaning|
|---|---|
|Reduce overfitting|Remove noise + unnecessary columns|
|Faster training|Less data → faster computation|
|Improves model accuracy|More relevant inputs = better model|

---

### ➤ PPT Categorization

```
                Feature Selection
                        │
        ┌──────────────┼──────────────┐
        │              │              │
      Filter         Wrapper        Embedded
```

---

### ✅ Filter Methods (PPT)

- Based on **statistics**
    
- Fastest method
    

PPT examples:

- Correlation matrix
    
- Chi-square test
    

---

### ✅ Wrapper Methods (PPT)

- Try subsets of features by _training the model repeatedly_
    

Examples:

- RFE (Recursive Feature Elimination)
    
- Forward selection
    
- Backward elimination
    

---

### ✅ Embedded Methods (PPT)

- Feature selection happens **during training**
    

Examples from PPT:

- LASSO (L1 feature elimination)
    
- Decision Tree Feature Importance
    

---

---

# 🔵 FEATURE EXTRACTION (PCA Algorithm)

> 📌 From PPT:
> 
> - _"PCA reduces dimensionality while retaining maximum information."_
>     
> - _"Transforms correlated variables into new uncorrelated components."_
>     
> - _"Helps improve model efficiency."_
>     

**Feature Selection = remove columns**  
**Feature Extraction = convert existing columns into new meaningful columns**

---

## ✅ PCA (Principal Component Analysis)

PPT summary:

- Used to reduce number of features
    
- Makes visualization possible (2D/3D)
    
- Converts correlated features into new independent components (PC1, PC2 …)
    

---

### ➤ PPT: “Steps in PCA”

```
Step 1: Standardize data
Step 2: Calculate the covariance matrix
Step 3: Identify principal components
Step 4: Sort components (highest information first)
Step 5: Transform original data into new components (PC1, PC2, ...)
```

---

### 📌 PPT diagram: High-dimensional → Compact representation

```
Original Data (multiple features)
       ↓
Find directions of maximum variation
       ↓
Project data onto new axes (Principal Components)
       ↓
Reduced and meaningful data representation
```

---

### Important PPT notes:

- PCA **must** be applied **after scaling**
    
- PCA is used when dataset has many correlated features
    
- PCA exchanged interpretability for performance
    

---

## ✅ Difference (as per PPT wording)

|Feature Selection|PCA (Feature Extraction)|
|---|---|
|Removes unnecessary features|Creates new transformed features|
|Keeps original meaning|Loses original meaning|
|LASSO, RFE|PCA|

---

**Short (2–4 marks):**

- Define feature engineering.
    
- Explain One-Hot Encoding with an example.
    
- What is PCA and why is it used?
    
- Differentiate numerical and categorical features.
    

**Long (10–12 marks):**

- Explain principal component analysis with steps and diagrams.
    
- How do we handle missing data? Explain types and techniques.
    
- Discuss Feature Engineering pipeline in detail.
    
- Explain feature scaling and feature selection with examples.
    

---



