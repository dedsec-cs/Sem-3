## 1. What is Regression?

Regression is a **supervised learning technique** in machine learning where the goal is to **predict a continuous numerical output** based on one or more input features. It tries to mathematically model the relationship between **dependent variable (Y)** and **independent variable(s) (X)**.

It does this by fitting the **best possible curve or line** through the training data such that the difference between the predicted values and the actual values is as small as possible.

### Why do we need Regression?

Regression helps us to:

1. Determine **how strongly** variables are related
    
2. Predict **future outcomes**
    
3. Understand and **quantify** trends and behaviors in data
    
4. Support **decision-making and planning** operations in businesses
    

Examples where Regression is used:  
• Forecasting stock market prices  
• Predicting house prices using area, location, etc.  
• Predicting sales vs advertisement spending  
• Medical predictions such as risk score

In simple words:  
Regression = Predicting **how much**.

---
### Key Terminologies in Regression & ML

1. **Dependent Variable**
    
    - The main factor we want to **predict or understand**.
        
    - Also called the **target variable**.
        
    - Example: Predicting house prices → House price is the dependent variable.
        
2. **Independent Variable**
    
    - Factors that **affect the dependent variable** or are used to **predict it**.
        
    - Also called **predictors**.
        
    - Example: Size of the house, location, number of rooms → Independent variables for house price.
        
3. **Outliers**
    
    - Observations with **extremely high or low values** compared to others.
        
    - Can **distort results** and should often be removed or treated.
        
    - Example: A house priced 10x higher than others in the dataset.
        
4. **Multicollinearity**
    
    - Occurs when **independent variables are highly correlated** with each other.
        
    - Problematic because it makes it **hard to rank which variable affects the dependent variable most**.
        
    - Example: Using both weight in kg and weight in pounds as predictors.
        
5. **Underfitting and Overfitting**
    
    - **Underfitting**: Model performs **poorly even on training data** → too simple.
        
    - **Overfitting**: Model performs **well on training data but poorly on test data** → too complex.
        
    - Example: Overfitting → model memorizes training data; Underfitting → model fails to capture patterns.
        

---
## 2. Types of Regression

Regression types are mainly classified into two categories:

### A) Based on Number of Input Variables

1. **Univariate Regression** → Only one input feature X
    
2. **Multivariate Regression** → Multiple input features X₁, X₂, …
    

### B) Based on Shape of Relationship

1. Linear Regression
    
2. Polynomial Regression
    
3. Logarithmic Regression
    
4. Exponential Regression  
    (Linear + Polynomial required as per syllabus)
    

---

## 3. Univariate Regression

### 3.1 Simple Linear Regression (SLR)

This is the simplest form of regression. It assumes that the relationship between X and Y is **straight-line** in nature.

Mathematical Model:  
Y = a + bX

Where:  
• a = Intercept → Value of Y when X is 0  
• b = Slope → Amount by which Y changes when X increases by 1 unit

How does the model learn?  
It tries to **find the best-fit line** by minimizing the errors (residuals) using **Least Squares Method**.

Graph Interpretation:  
• Data is scattered as points  
• A line is drawn in such a way that the sum of squared vertical distances between actual and predicted points is minimal

Applications:  
• Study time vs Marks  
• Age vs Height (early age)  
• Temperature vs Electricity consumption

Advantages:  
• Simple, fast, easy to interpret

Limitations:  
• Works only when data is linearly related  
• Cannot capture curves & complex patterns

---

## 4. Polynomial Regression

Real-world data is often not straight line — it may bend or take different shapes.  
Polynomial Regression handles such **curved relationships**.

General form:  
Y = a + b₁X + b₂X² + b₃X³ + … + bnXⁿ

Where degree n ≥ 2 makes curve fit better.

Practical Uses:  
• Growth patterns  
• Biological relationships  
• Climate or population data

Why it is powerful:  
It can model **non-linear patterns** while still being linear in coefficients.

Drawback:  
Higher polynomial degree → memorizing noise → **overfitting**

When to use:  
When the data does not appear straight but has **smooth curve**.

---

## 5. Multivariate Regression

When there are **multiple** independent variables affecting the dependent variable.

Example:  
House price = f(area, number of rooms, age, location)

General Equation:  
Y = a + b₁X₁ + b₂X₂ + … + bnXn

It represents a **plane** in multi-dimensional space.

Advantages:  
• Very realistic for industrial datasets  
• Can capture influence of many features

Challenges:  
• Multicollinearity can weaken predictions  
• Requires more data to train reliably

---

### Summary Comparison

|Type|Inputs|Pattern|Application|
|---|---|---|---|
|Simple Linear|1|Straight Line|Basic prediction tasks|
|Polynomial|1|Curvy Trend|Dynamic trend shifts|
|Multivariate|Many|Linear in Higher Dimension|Industry predictions|

---

## 6. Model Evaluation Metrics

Regression models must be evaluated to know how accurate they are.

### 6.1 Mean Squared Error (MSE)

MSE = (1/n) Σ (Yi − Ŷi)²

It measures the **average squared difference** between actual and predicted values.

Why square errors?  
• To give more penalty to large errors  
• To avoid negative-positive cancellation

Interpretation:  
Lower the MSE → More accurate model

Limitation:  
Unit becomes squared → Hard to interpret directly

---

### 6.2 R-Square (R²) – Coefficient of Determination

R² tells us **how much variance in Y** is explained by the model.

R² = 1 − (SSres / SStot)

Value Range:  
• 1 → Perfect model  
• 0 → No explanatory power at all  
• < 0 → Worse than predicting mean value

Interpretation:  
Higher R² = Better goodness of fit

R² answers:  
“How good is the model at explaining the story behind the data?”

---

────────────────────────────────────────

# PART – 2 : CLASSIFICATION

## 1. What is Classification?

Classification is a **supervised learning technique** where the goal is to **categorize** a given input into one of several predefined classes or categories.

Instead of predicting _how much_ (like regression), it predicts:  
**Which class/category does the data belong to?**

Examples:  
• Spam mail vs Real mail  
• Diabetes → Yes or No  
• Fraud vs Genuine transaction  
• Identifying emotion from text

Output type:  
Discrete values (Labels)

Classification answers:  
“Yes or No?”, “A or B?”, “Which group?”

---

## 2. Logistic Regression (Classification Model)

Despite its name, Logistic Regression is **not a regression technique**.  
It is used for **binary classification problems**, where the output has only **two possible classes**.

Examples:  
• Pass vs Fail  
• Tumor → Benign or Malignant  
• Customer → Will Buy or Will Not Buy

Why not Linear Regression?  
Because Linear Regression can predict values outside 0 and 1 range.  
But classification requires **probabilities between 0 and 1**.

Solution:  
Logistic Regression uses **Sigmoid Function** (S-shaped curve)

Sigmoid Function:  
Probability = 1 / (1 + e⁻(a + bX))

Outputs:  
If Probability ≥ 0.5 → Class 1  
If Probability < 0.5 → Class 0

Decision Boundary:  
A classification rule that separates classes based on probability threshold.

Advantages:  
• Works well for binary problems  
• Probabilistic interpretation  
• Efficient, fast

Limitation:  
• Only linear separation of classes  
• Bad for highly complex datasets

---

## 3. Types of Logistic Regression

Logistic regression is used when the target variable is **categorical** (class labels). Based on how many classes (categories) exist in the output and how multiple labels behave, logistic regression is classified into the following types:

---

#### 1. **Binary Logistic Regression**

This is the most common type.

- Used when the outcome has **only two possible classes**
    
- Example outcomes:
    
    - Yes / No
        
    - Spam / Not Spam
        
    - Has Disease / No Disease
        
    - Pass / Fail
        

Here, **one class is assumed as positive (1)** and the other as **negative (0)**.

The model estimates:

```
P(y = 1 | x)   → Probability of being in Class 1
```

Decision rule:

```
If probability ≥ 0.5 → Class 1 (Positive)
Else → Class 0 (Negative)
```

---

#### 2. **Multinomial Logistic Regression**

Used when there are **three or more classes** and **they are not ordered**.

Examples:

- Types of fruits: Apple, Banana, Orange
    
- Transport mode: Car, Bus, Train, Airplane
    
- Occupation category: Student, Engineer, Teacher, Doctor
    

Key Points:

- Uses **Softmax function** (instead of Sigmoid)
    
- Calculates probability for **each class**
    
- Assigns the class with the highest probability
    

Here:

```
P(Class 1 | x) + P(Class 2 | x) + ... + P(Class k | x) = 1
```

---

#### 3. **Ordinal Logistic Regression**

Used when the output classes are **ordered or ranked**.

Examples:

- Rating levels: Poor < Average < Good < Excellent
    
- Education levels: High School < Bachelor’s < Master’s < PhD
    
- Satisfaction: Low < Medium < High
    

Important characteristics:

- Classes have a **meaningful order**
    
- But differences between classes may **not be equal**  
    (The gap between "Good" and "Excellent" may not equal the gap between "Poor" and "Average")
    

This model considers that higher classes should have a **greater probability** as certain input features increase.

---

### Summary Table

|Type of Logistic Regression|Output Classes|Order of Classes|Examples|
|---|---|---|---|
|Binary Logistic Regression|2|No|Spam / Non-spam, Yes / No|
|Multinomial Logistic Regression|3 or more|No|Fruits, Transport modes|
|Ordinal Logistic Regression|3 or more|Yes|Ratings, Satisfaction levels|

---

### Why Different Types?

Because different real-world scenarios have:

- Different number of categories
    
- Different relationships between categories
    

Choosing the correct type ensures:

- Better model behavior
    
- More accurate probability predictions
    
- Correct interpretation of results
    

---

## Final Summary Table

|Method|Output Type|Model Line Shape|Common Use|
|---|---|---|---|
|Linear Regression|Numerical|Straight Line|Price forecasting|
|Polynomial Regression|Numerical|Curve|Growth trends|
|Multivariate Regression|Numerical|Plane|Real-world predictions|
|Logistic Regression|Category|Sigmoid curve|Binary classification|

---
