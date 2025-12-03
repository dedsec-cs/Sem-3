
# **1. Why Do We Need L1 Regularization?**

Imagine building a model that predicts house prices.  
You may have 50 features: area, bedrooms, distance to school, number of windows, paint color, and so on.

But reality check:

- Not all features matter.
    
- Some features add noise.
    
- Some features weaken the model.
    

If we use all features with full weight, the model becomes unnecessarily complex and may overfit.

We need a way to **control complexity** and **remove unimportant features** automatically.

L1 Regularization does exactly that.

---

# **2. What Is L1 Regularization? 

L1 Regularization is a technique that:

- Penalizes large weight values
    
- Forces some weight values to become exactly zero
    
- Automatically selects the most important features
    

This is also known as **Lasso Regression**  
LASSO stands for:

Least  
Absolute  
Shrinkage and  
Selection  
Operator

The name itself describes what L1 does:

- Least: It tries to minimize error
    
- Absolute: Uses absolute value of weights
    
- Shrinkage: Pushes some weights toward zero
    
- Selection: Eliminates irrelevant features by making their weights zero
    

---

# **3. The Mathematical Form of L1 Regularization**

For a simple linear regression model:

Prediction:  
y = w1 x1 + w2 x2 + ... + wn xn + b

Loss function without regularization:

Loss = Mean Squared Error (MSE)

Loss = (1/n) Σ (y_actual – y_predicted)^2

With L1 regularization:

Loss = (1/n) Σ (y_actual – y_predicted)^2 + λ Σ |wi|

Where:

- λ (lambda) is the regularization strength
    
- Σ |wi| is the sum of absolute values of the weights
    

Interpretation:

- The model tries to keep error low
    
- But is penalized for using too many or too large weights
    

This penalty term forces the model to become simpler.

---

# **4. Deep Intuition: Why Does L1 Make Weights Zero?**

Unlike L2 (which squares weights), L1 uses absolute values.

The absolute penalty forms a sharp "V" around zero.  
This sharp corner encourages the optimization process to push many weights directly to zero.

In contrast:

- L2 creates a smooth U-shaped penalty, so weights get smaller but rarely become exactly zero.
    
- L1 creates a corner at 0, so weights stick to zero.
    

Because of this unique behavior:

L1 → Feature Selection  
L2 → Weight Shrinkage

---

# **5. What Happens as λ Changes?**

### Small λ (λ ≈ 0)

- Weak regularization
    
- Model behaves like normal regression
    
- Many non-zero weights
    
- Higher risk of overfitting
    

### Moderate λ

- Significant simplification
    
- Some weights shrink
    
- Some become exactly zero
    
- Better generalization
    

### Large λ

- Strong penalty
    
- Many features removed
    
- Model becomes too simple
    
- Risk of underfitting
    

Choosing λ is crucial.  
Cross-validation is usually used to find the best value.

---

# **6. Why L1 Regularization Is Special**

### 1. It Performs Feature Selection

L1 removes unimportant features by making their coefficients exactly zero.  
This is extremely useful when:

- Dataset has many features
    
- Only a few features are important
    
- Some features are redundant or noisy
    

### 2. Works well with high-dimensional datasets

Examples:

- Text classification (thousands of words as features)
    
- Genetics (thousands of gene markers)
    
- Sensor data
    

### 3. Produces simpler and more interpretable models

Because L1 eliminates features, the final model often becomes compact and easy to explain.

### 4. Helps reduce overfitting

By removing irrelevant features, L1 prevents the model from fitting noise.

---

# **7. Numerical Example (Step-by-Step)**

Let’s take a simple dataset:

Predict y from x using linear regression.

Data:  
x: 1, 2, 3  
y: 2, 4, 6

True relationship: y = 2x

But assume we introduce two useless features f2 and f3:

f1 = x  
f2 = random noise  
f3 = random noise

Start with regression model:

y = w1 f1 + w2 f2 + w3 f3

Suppose after training (without regularization), weights are:

w1 = 2.01  
w2 = 0.7  
w3 = -0.5

Because of noise, the model is overfitting.

Now apply L1 Regularization with λ = 0.5

The loss becomes:

Loss = MSE + 0.5(|w1| + |w2| + |w3|)

During optimization:

- w2 and w3 move toward zero
    
- w1 stays strong because it is truly important
    

Final weights might become:

w1 = 2.00  
w2 = 0  
w3 = 0

Result:

- Noise features eliminated
    
- Final model becomes y = 2x
    
- Perfect generalization
    

This is the power of L1.

---

# **8. Geometric Intuition

Imagine the allowed region of weights drawn on a graph.

### L2 Regularization → Circular region

Smooth boundaries  
Weights rarely zero

### L1 Regularization → Diamond-shaped region

Sharp corners  
Corners lie on axes  
These corners represent zero values

Because the optimization process often hits a corner, weights become zero.

This is the geometric reason L1 performs feature selection.

---

# **9. When Should We Use L1 Regularization?**

Use L1 when:

- You suspect many features are irrelevant
    
- You want an interpretable model
    
- You want automatic feature selection
    
- The dataset is high-dimensional
    
- You want to prevent overfitting through feature elimination
    

---

# **10. Limitations of L1 Regularization**

Even though powerful, L1 has some drawbacks:

### 1. Unstable with highly correlated features

If two features are very similar, L1 may:

- Choose one
    
- Drop the other arbitrarily
    

This may confuse interpretations.

### 2. Can behave unpredictably in small datasets

If the dataset is tiny, forcing weights to zero may oversimplify.

### 3. Optimization can be harder

Because of the absolute value, the loss function has a non-differentiable point at zero.

---

# **11. Comparison: L1 vs L2 Regularization**

|Feature|L1 (Lasso)|L2 (Ridge)|
|---|---|---|
|Penalty|Sum of absolute weights|Sum of squares of weights|
|Effect|Shrinks weights to zero (feature selection)|Shrinks weights smoothly but never zero|
|Model|Sparse|Dense|
|Use Case|Many features, some irrelevant|All features important|
|Handles Multicollinearity|Poorly|Strongly|

---

# **12. Complete Summary**

1. L1 Regularization (Lasso) penalizes the sum of absolute weight values.
    
2. It drives some weights to zero, effectively eliminating features.
    
3. It simplifies the model and prevents overfitting.
    
4. It creates sparse, interpretable models.
    
5. Works best when many features exist but only a few truly matter.
    
6. Very useful in high-dimensional problems.
    
7. But can behave inconsistently with correlated features.
    

---

# **13. Final Conclusions**

L1 Regularization is one of the most powerful tools in machine learning because it combines:

- Simplicity
    
- Interpretability
    
- Automatic feature selection
    
- Reduced model complexity
    
- Better generalization
    

It turns complex models into clean, sharp, efficient prediction machines.

---
# **CHAPTER: L2 REGULARIZATION (RIDGE)**

---

# **1. Why Do We Need L2 Regularization?**

When we train a machine learning model, especially one with many features, the model may:

- Become too sensitive
    
- Learn noise
    
- Produce unstable predictions
    
- Show high variance
    
- Overfit the training data
    

L2 Regularization is a technique to **control this complexity** by discouraging the model from relying too heavily on any specific feature.

Think of it as gently reminding the model:

"Do not make any single weight too powerful."

---

# **2. What Is L2 Regularization?

L2 Regularization adds a penalty to the loss function equal to the **sum of the squares** of the model weights.

This shrinks the weights but does not force them to become exactly zero.

Because weights stay non-zero but small, L2 regularization:

- Reduces model complexity
    
- Prevents overfitting
    
- Improves generalization
    
- Makes predictions more stable
    

L2 Regularization is also known as **Ridge Regression**.

---

# **3. Mathematical Form of L2 Regularization**

Suppose a linear regression model predicts:

y = w1 x1 + w2 x2 + ... + wn xn + b

Without regularization, the loss function is:

Loss = (1/n) Σ (y_actual – y_predicted)^2

With L2 regularization:

Loss = (1/n) Σ (y_actual – y_predicted)^2 + λ Σ (wi²)

Where:

- λ is the regularization strength
    
- Σ (wi²) is the sum of squared weights
    

This penalty makes large weights costly.

---

# **4. Intuition: Why Squaring the Weights Works**

L2 squares the weights: wi²  
This makes large values grow even larger.

Example:  
1² = 1  
5² = 25  
10² = 100

Because of this rapid growth, the algorithm avoids large weight values.  
It prefers smaller, smoother weights.

But unlike L1, which uses absolute values, L2's penalty has a smooth, rounded shape.

This makes weights **shrink** but **rarely reach zero**.

In short:

L2 → Shrinks weights  
L1 → Eliminates weights

---

# **5. Effect of λ (Regularization Strength)**

### λ = 0

No regularization.  
Model behaves like standard regression.

### λ is small

Gentle shrinkage  
Model remains flexible  
Good for avoiding mild overfitting

### λ is moderate

Sharper weight control  
Weights become smaller  
Model simplifies  
Better generalization

### λ is large

Weights shrink heavily  
Model becomes too simple  
Underfitting may occur

Choosing the right λ is crucial.  
Typically done using cross-validation.

---

# **6. Why L2 Is Useful**

### 1. Reduces overfitting

By shrinking weights, the model becomes smoother and less sensitive to noise.

### 2. Controls variance

L2 is very effective in reducing variance without increasing bias too much.

### 3. Handles multicollinearity

When features are highly correlated, standard regression fails because weights explode.

L2 stabilizes the weights.

### 4. Produces stable, predictable models

Small weights lead to better-behaved models.

### 5. Works well when all features matter

Unlike L1, which discards features, L2 keeps them all but reduces their influence.

---

# **7. Geometric Intuition

Imagine the set of allowed weight values.

### For L2 regularization:

The allowed region is a **circle (or sphere)**.

Smooth boundaries.

Smooth boundaries → gradients are continuous → weights smoothly shrink.

### For L1 regularization:

The allowed region is a **diamond** with sharp corners.

Corners touch axes → weights become zero → feature selection.

Because L2 has no corners:

- Weights rarely go to zero
    
- Model remains dense
    
- All features remain active
    

---

# **8. Numerical Example (Simple, Intuitive)**

Suppose we want to fit:

y = w1 x1 + w2 x2

Training data:  
x1, x2 → y

(1, 0) → 5  
(2, 1) → 9  
(3, 1) → 12

Assume standard regression gives:

w1 = 3  
w2 = 2

Now apply L2 regularization with λ = 1.

New loss = MSE + λ(w1² + w2²)

Penalty term = 1*(3² + 2²) = 1*(9 + 4) = 13

To reduce penalty, optimization shrinks weights.

New weights after L2 optimization might become:

w1 = 2.4  
w2 = 1.7

Notice:

- Weights still non-zero
    
- Shrunk smoothly
    
- Model becomes more stable
    
- No feature eliminated
    

This is classic L2 behavior.

---

# **9. Gradient Descent Understanding**

In gradient descent, the update rule becomes:

wi(new) = wi(old) – α(∂Loss/∂wi + 2λwi)

This means:

Every iteration pushes the weight slightly toward zero, but not all the way.

This repeated shrinkage is why L2 stabilizes weights.

---

# **10. When Should We Use L2 Regularization?**

Use L2 when:

1. All features are important
    
2. Data has many correlated features
    
3. You want smooth, stable models
    
4. You want to reduce overfitting without eliminating features
    
5. You want reliable predictions for continuous data
    

L2 is the recommended first choice in many regression problems.

---

# **11. Advantages of L2 Regularization**

1. Prevents overfitting effectively
    
2. Shrinks weights smoothly
    
3. Handles multicollinearity
    
4. Produces stable models
    
5. Works well with gradient descent
    
6. Keeps all features (unlike L1)
    
7. Easy to compute and widely supported
    

---

# **12. Limitations of L2 Regularization**

1. Does not perform feature selection  
    All features remain in the final model.
    
2. Less interpretable than L1  
    Because no feature is removed.
    
3. Not ideal when features are mostly irrelevant  
    L1 or Elastic Net would be better.
    

---

# **13. L1 vs L2 (Quick Crisp Comparison)**

|Feature|L1 Regularization|L2 Regularization|
|---|---|---|
|Penalty|Sum of absolute weights|Sum of squares of weights|
|Effect|Makes weights zero|Shrinks weights but not zero|
|Model Type|Sparse|Dense|
|Feature Selection|Yes|No|
|Handles Multicollinearity|Poorly|Very well|
|Behavior|Can be unstable|Very stable|
|Use Case|Many irrelevant features|Many correlated features|

---

# **14. Summary of L2 Regularization**

1. L2 Regularization penalizes the sum of squared weights.
    
2. It shrinks weights but does not remove them.
    
3. It reduces overfitting and improves generalization.
    
4. Works especially well with correlated features.
    
5. Produces stable and smooth models.
    
6. Effect controlled by λ.
    
7. Does not perform feature selection, unlike L1.
    

---

# **15. Final Conclusion**

L2 Regularization, or Ridge Regression, is a powerful tool for controlling model complexity.  
It ensures that no feature dominates too heavily and keeps the model smooth and stable.  
It is one of the most widely used regularization techniques because it provides:

- Better generalization
    
- Reduced variance
    
- Improved model stability
    

without removing features.

---
