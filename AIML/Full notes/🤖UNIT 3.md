---

---
---
## 🧠 Regression & Classification: Core Supervised Learning

### 1. Regression: Modelling Continuous Outputs

**•Regression** is a statistical method used to find the relationship between variables and **predict a continuous output variable** (dependent variable, $Y$) based on one or more predictor variables (independent variables, $X$)
•It predicts continuous/real values such as temperature, age, salary, price, etc.
•It is mainly used for prediction, forecasting, time series modeling, and determining the causal-effect relationship between variables.
![[Pasted image 20251111092736.png]]
•"Regression shows a line or curve that passes through all the datapoints on target-predictor graph in such a way that the vertical distance between the datapoints and the regression line is minimum.

---

A. Key Terminologies 2

- **Dependent Variable (Y)**: The main factor we are trying to **predict** or explain (also called the target variable).
    
- **Independent Variable (X)**: The factors used to **predict** or explain the changes in the dependent variable (also called the predictor variable).
    
- **Regression Line / Line of Best Fit**: A line or curve that passes through the data points in such a way that the vertical distance (error) between the actual data points and the line is minimized5.
- **Outliers:** Outlier is an observation which contains either very low value or very high value in comparison to other observed values. An outlier may hamper the result, so it should be avoided.
- **Multicollinearity:** If the independent variables are highly correlated with each other than other variables, then such condition is called Multicollinearity. It should not be present in the dataset, because it creates problem while ranking the most affecting variable.
- **Underfitting and Overfitting:** If our algorithm works well with the training dataset but not well with test dataset, then such problem is called Overfitting. And if our algorithm does not perform well even with training dataset, then such problem is called underfitting.

	

---
![[Pasted image 20251111093040.png]]

---
## 🔹 Types of Regression 

### 1. **Univariate Regression**

> Relationship between **one independent variable(predictor) (X)** and **one dependent variable (Outcome)(Y)**.The goal is to model how changes in the independent variable affect the dependent variable.

#### ✅ **Simple Linear Regression**

- Fits a straight line:  
    `Y = a + bX + ε`
    
- Use case (from PPT):  
    Predict sales based on advertising spend
    

#### ✅ **Polynomial Regression**

- Fits a curve instead of a straight line  
    `Y = a + b₁X + b₂X² + ... + bₙXⁿ + ε`
    
- Use when data shows **non-linear growth patterns**
    

#### ✅ **Logarithmic Regression**

- `Y = a + b log(X) + ε`
    
- Used when growth rate decreases with time  
    Example: relation between income & consumption
    

#### ✅ **Exponential Regression**

- `Y = a ⋅ e^(bX)`
    
- Used in **growth/decay** scenarios: population, radioactive decay
    

---

### 2. **Multivariate Regression**

> Used when there are **multiple predictors (X₁, X₂, ..., Xₙ)** affecting a **single dependent variable**.

#### ✅ **Multiple Linear Regression**

- `Y = a + b₁X₁ + b₂X₂ + ... + bₙXₙ + ε`
    
- Use case (from PPT):  
    Predicting a person’s **weight** based on height, age, exercise frequency
    

---

### 🔒 Regularized Regression (to prevent overfitting)

> When models become complex, they may “memorize” noise in training data = **overfitting**.

#### ✅ **Ridge Regression (L2 Regularization)**

- Adds penalty = square of coefficients
    
- Works well when predictors are many but **none should be eliminated**
    
- Shrinks coefficients smoothly (no feature becomes 0)
    

#### ✅ **Lasso Regression (L1 Regularization)**

- Adds penalty = absolute value of coefficients
    
- Can shrink some coefficients to **zero**
    
- Used for **feature selection** (selects most important features)
    

#### ✅ **Elastic Net Regression**

- Combo of L1 (Lasso) + L2 (Ridge)
    
- Best when predictors are **highly correlated**
    

---

## 🚨 Regression vs Logistic Regression (Clarification)

- **Regression → predicts continuous values**
    
- **Logistic Regression → classification** (0/1, Yes/No)
    

> Logistic Regression is still covered under “Regression” in syllabus but used for classification (binary/multi-class) .

---

## 🧪 Metrics used in Regression (from PPT)

### ✅ Mean Squared Error (MSE)

- Mean Squared Error (MSE) is a common metric used to evaluate the performance of regression models. Average squared difference between predicted and actual values.
- Formula:     $$\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2$$Where:

- $n$ is the number of observations13.    
- $y_i$ is the actual value14.
- $\hat{y}_i$ is the predicted value15.
- ![[Pasted image 20251111221459.png]]
 •The Mean Squared Error (MSE) for this dataset is 0.6875. This value gives us an indication of how well the predicted values match the actual values, with a lower MSE representing better model performance.

## Importance of MSE:
- **Model Evaluation**: MSE provides a **quantitative measure** of model performance, where a **lower value** indicates a better fit and greater predictive accuracy on the data.
    
- **Optimization Objective**: It serves as the primary **loss function** (or cost function) in many training algorithms (like gradient descent), which work to **minimize the MSE** to find the optimal model parameters.
    
- **Sensitivity to Outliers**: Because MSE **squares the errors**, it amplifies the impact of large deviations, making the metric highly **sensitive to outliers**.
    
- **Comparative Analysis**: MSE allows for straightforward **comparison** between different regression models or algorithms, facilitating the selection of the best-performing model for a given task.

##### 2. R-squared ($R^2$) Error (Coefficient of Determination)

- **Definition**: $R^2$ is a statistical measure that indicates the **proportion of the variance** in the dependent variable ($Y$) that is predictable from the independent variables ($X$)24. It indicates the **goodness of fit** of the model25.
    
- **Range**: $R^2$ values range from **0 to 1**26.
    
    - **$R^2 = 1$**: The model explains **all** the variability (perfect fit)27.
        
    - **$R^2 = 0$**: The model explains **none** of the variability (the mean of $Y$ is the best predictor)28.
        
- **Interpretation**: An $R^2$ value of 0.70 suggests that 70% of the variability in $Y$ can be explained by the model's independent variables29.
    
- Formula:
    
    $$R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} \text{ }$$
    
    - $\text{SS}_{\text{res}} = \sum (y_i - \hat{y}_i)^2$ (Residual Sum of Squares, the unexplained variation)30.
        
    - $\text{SS}_{\text{tot}} = \sum (y_i - \bar{y})^2$ (Total Sum of Squares, the total variation in $Y$)31.
        

---

## 🔁 When to Use What (Quick Summary)

|Type|Use When|Example|
|---|---|---|
|Simple Linear|Single predictor, linear relation|Salary vs experience|
|Polynomial|Clearly curved relationship|Growth curve, trend data|
|Logarithmic|Growth slows over time|Income vs spending|
|Exponential|Constant % growth/decay|Population growth|
|Multiple Linear|Multiple predictors|Predict price of house|
|Ridge|Many predictors, prevent overfitting|High-dimensional datasets|
|Lasso|Want feature selection|Removing irrelevant features|
|Elastic Net|Predictors are correlated|Real-world ML problems|

---

### 2. Logistic Regression: The Classification Tool

**Logistic Regression** is a supervised learning algorithm primarily used to solve **classification problems**. It is a type of regression but is functionally different from linear regression.

#### A. Core Principles

- **Output**: It works with **categorical/discrete variables** such as 0 or 1, Yes or No, or True or False.
    
- **Probability**: It works on the concept of **probability**. It models the probability that an instance belongs to a certain class.
    
- **Sigmoid Function**: It uses the **Sigmoid function** (or logistic function) to map the continuous output of a linear model into a probability value between 0 and 1.
    
    - **Sigmoid Formula**: $\text{sig}(x) = \frac{1}{1 + e^{-x}}$ 
    - ![[Pasted image 20251111223008.png]]
        

#### B. Types of Logistic Regression
![[Pasted image 20251111223030.png]]

1. **Binary Logistic Regression**: Used when the dependent variable has **exactly two** possible outcomes (e.g., success/failure, 0/1).
    
2. **Multinomial Logistic Regression**: Used when the categorical dependent variable has **two or more discrete outcomes** that are **not ordered** (e.g., predicting the type of food consumed by pets: wet food, dry food, or junk food).
    
3. **Ordinal Logistic Regression**: Used when the dependent variable is in an **ordered state** or has an inherent rank (e.g., predicting shirt size: XS/S/M/L/XL; or survey answers: Agree/Disagree/Unsure).

![[Pasted image 20251111223150.png]]


---
### 🛡️ Regularization: Controlling Model Complexity

**Regularization** is a set of techniques used in machine learning and statistics to **prevent overfitting** and improve a model's **generalization** and performance on unseen data. It achieves this by adding a **penalty term** to the model's loss function, thereby discouraging excessively complex models and large coefficients.

---

### 1. Bias and Variance: The Reducible Errors

All errors in a Machine Learning Model (MLM) can be classified into reducible errors (Bias and Variance) and irreducible errors.

#### A. Bias

- **Definition**: Bias refers to the errors due to **overly simplistic assumptions** made by the learning algorithm6. It represents the difference between the prediction values made by the model and the actual expected values7.
    
- **Impact**: Bias always deals with errors on the **training data**.
    
    - **High Bias**: Occurs when the model is too simple. The model fails to capture the important features or underlying patterns of the dataset, leading to **poor performance** on both training and testing sets. This condition is called **Underfitting**.
    - •Low Bias: A low bias model will make fewer assumptions about the form of the target function.
        
- **Reducing High Bias**: Increase model complexity, increase the input features, or **decrease the regularization term**.
- •Some examples of machine learning algorithms with low bias are Decision Trees, k-Nearest Neighbours and Support Vector Machines.
- •At the same time, an algorithm with high bias is Linear Regression, Linear Discriminant Analysis and Logistic Regression.
    

#### B. Variance

- **Definition**: Variance specifies the amount of variation in the prediction if a different training dataset were used. It measures how sensitive the model is to small fluctuations in the training data.
    
- **Impact**:
    
    - **High Variance**: Occurs when the model is too complex. The model learns the noise in the training data, leading to a large variation in prediction with changes in the training set. This causes **overfitting**.

 •A model with high variance has the below problems:

	•A high variance model leads to overfitting.
	
	•Increase model complexities.

- **Reducing High Variance**: Reduce input features, use a less complex model, increase the training data, or **increase the regularization term**.


### Different Combinations of Bias-Variance

•Low-Bias, Low-Variance:

	The combination of low bias and low variance shows an ideal machine
	learning model. However, it is not possible practically.

•Low-Bias, High-Variance:

	 With low bias and high variance, model predictions are inconsistent and
	 accurate on average. This case occurs when the model learns with a large
	 number of parameters and hence leads to an overfitting

•High-Bias, Low-Variance:

	•With High bias and low variance, predictions are consistent but
	inaccurate on average. This case occurs when a model does not learn well
	with the training dataset or uses few numbers of the parameter. It leads to
	underfitting problems in the model.

•High-Bias, High-Variance:

	With high bias and high variance, predictions are inconsistent and also
	inaccurate on average.

![[Pasted image 20251111224218.png]]

---

### 2. Overfitting and Underfitting

Overfitting and Underfitting are manifestations of a model's poor generalization due to high variance or high bias, respectively.

#### A. Overfitting

- **Definition**: An undesirable behavior where the model makes accurate predictions for the **training data** but performs poorly on new, unseen data18. The model learns the noise/irrelevant details in the training set19.
    
- **Bias-Variance**: Characterized by **Low Bias** and **High Variance**.
    
- **Symptoms**: Low training error but **high validation/test error**.
    
- **Causes**: The model complexity is too high, the training data size is too small, or the training data contains large amounts of noise.
    
- **Solutions**: Use **regularization** (L1 or L2), employ cross-validation, or reduce model complexity2323.

- •High variance and low bias.

#### B. Underfitting

- **Definition**: Occurs when a model is **too simple** to capture the necessary complexities and patterns in the data24.
    
- **Bias-Variance**: Characterized by **High Bias** and **Low Variance**.
    
- **Symptoms**: **High training error** and **high validation/test error**. The model fails to fit the training data well27.
    
- **Causes**: The model is too simple, insufficient features are used, or excessive regularization is applied.
    
- **Solutions**: **Increase model complexity**, perform feature engineering (add features), or remove noise from the data29.
- •The underfitting model has High bias and low variance.
-

![[Pasted image 20251111224407.png]]

---
### Regularization: L1 (Lasso)

•LASSO (Least Absolute Shrinkage and Selection Operator) is a regression analysis method
that incorporates L1 regularization.

•It's particularly useful for models that can benefit from feature selection and addressing
multicollinearity.
### 3. L1 and L2 Regularization (Regularized Linear Regression)

Regularization works by adding a penalty term to the minimization objective function (often the Mean Squared Error, MSE).

The general objective function becomes:

$$\text{Minimize: } \text{Loss Function} + \lambda \times \text{Penalty Term}$$

Where $\lambda$ (lambda) is the regularization parameter controlling the strength of the penalty30.

#### A. L2 Regularization (Ridge Regression)

- **Definition**: A machine learning technique that uses the L2 regularization method to avoid overfitting.
    
- **Penalty Term**: Adds a penalty proportional to the **sum of the squares** (squared magnitude) of the coefficients ($\beta_j^2$).
- •It is a machine learning technique that avoids overfitting by introducing a penalty term into the model's loss function based on the squares of the model's parameters.
- The goal of L2 regularization is to keep the model's parameter sizes short and prevent oversizing.
- In order to achieve L2 regularization, a term that is proportionate to the squares of the model's parameters is added to the loss function.
- This word works as a limiter on the parameters' size, preventing them from growing out of control.
- A hyperparameter called lambda that controls the regularization's intensity also controls the size of the penalty term.
- The parameters will be smaller and the regularization will be stronger the greater the lambda.
    
- Objective Function:
    
    $$\text{Minimize: } \|Y - X\beta\|^2 + \lambda \|\beta\|^2 \quad \text{or} \quad \text{CF}_{\text{L2}} = \sum (y_i - \hat{y}_i)^2 + \lambda \sum \beta_j^2$$
    
- **Effect**: It shrinks the coefficients **evenly** towards zero 33, keeping their sizes small and preventing any single feature from dominating the prediction34. It is particularly effective for managing **multicollinearity**.
    

#### B. L1 Regularization (Lasso Regression)

- **Definition**: LASSO (Least Absolute Shrinkage and Selection Operator) is a regression method that incorporates L1 regularization35.
    
- **Penalty Term**: Adds a penalty proportional to the **sum of the absolute values** of the coefficients ($|\beta_j|$).
    
- Objective Function:
    
    $$\text{Minimize: } \|Y - X\beta\|^2 + \lambda \|\beta\|_1 \quad \text{or} \quad \text{CF}_{\text{L1}} = \sum (y_i - \hat{y}_i)^2 + \lambda \sum |\beta_j|$$
    
- **Key Effect (Feature Selection)**: L1 regularization can shrink the coefficients of unimportant features to **exactly zero**. This effectively removes irrelevant features from the model, leading to a **sparse** and highly interpretable model38.
 
- Bias-Variance Tradeoff: By introducing the penalty, LASSO can help reduce overfitting, making the model more generalizable to unseen data. However, this can introduce some bias.
- Tuning Parameter (λ): The choice of λ is crucial. A smaller λ leads to a model closer to ordinary least squares (OLS), while a larger λ increases the amount of shrinkage and feature selection. Techniques like cross-validation are commonly used to find an optimal λ.
- Applications: LASSO is widely used in scenarios with many predictors, especially when some of them might be irrelevant or redundant. It's popular in fields like genetics, finance, and machine learning.

#### C. Elastic Net

- **Definition**: Combines both L1 and L2 regularization, adding both absolute and squared norms of coefficients. It includes a hyperparameter α that controls the ratio between L1 and L2 regularization.
    
- Objective Function:
    
    $$\text{Minimize: } \|Y - X\beta\|^2 + \lambda_1 \|\beta\|_1 + \lambda_2 \|\beta\|^2 \text{}$$
    
- **Effect**: Allows for both the robustness of L2 (managing correlated predictors) and the feature selection of L140.


## Benefits of Regularization

1.Prevents Overfitting: Regularization helps models focus on underlying patterns instead of memorizing noise in the training data.

2.Improves Interpretability: L1 (Lasso) regularization simplifies models by reducing less important feature coefficients to zero.

3.Enhances Performance: Prevents excessive weighting of outliers or irrelevant features helps in improving overall model accuracy.

4.Stabilizes Models: Reduces sensitivity to minor data changes which ensures consistency across different data subsets.

5.Prevents Complexity: Keeps model from becoming too complex which is important for limited or noisy data.

6.Handles Multicollinearity: Reduces the magnitudes of correlated coefficients helps in improving model stability.

7.Allows Fine-Tuning: Hyperparameters like alpha and lambda control regularization strength helps in balancing bias and variance.

8.Promotes Consistency: Ensures reliable performance across different datasets which reduces the risk of large performance shifts.

---

## Confusion Matrix

The **Confusion Matrix** is a vital tool used to evaluate the performance of a **classification model**1. It provides a visual representation of the model's performance by comparing its predicted classifications against the actual, known outcomes2.
![[Pasted image 20251111231925.png]]

## 📊 Confusion Matrix Structure

The matrix is a $2 \times 2$ table (for binary classification) that contains four fundamental outcomes:

| **Component**           | **Definition**                                                                                                                                              | **Interpretation**                                                                                                                                         | **Error Type**     |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **True Positive (TP)**  | Number of correct predictions where an instance is predicted as positive, and it is actually positive.                                                      | **Correctly** identified the positive class.                                                                                                               | Correct Prediction |
| **True Negative (TN)**  | Number of correct predictions that an instance is negative.                                                                                                 | **Correctly** identified the negative class.                                                                                                               | Correct Prediction |
| **False Positive (FP)** | Number of incorrect predictions where an instance is predicted as positive, but it is actually negative.                                                    | **Incorrectly** raised an alarm (False Alarm).                                                                                                             | **Type I Error**   |
| **False Negative (FN)** | Number of incorrect predictions where an instance is predicted as negative, but it is actually positive.                                                    | **Incorrectly** missed a positive case.                                                                                                                    | **Type II Error**  |
|                         | **Predicted Negative**                                                                                                                                      | **Predicted Positive**                                                                                                                                     |                    |
| **Actual Negative**     | **True Negative (TN)**: The number of correct predictions that an instance is negative. 3                                                                   | **False Positive (FP)**: The number of incorrect predictions where an instance is predicted as positive, but it is actually negative (**Type I error**). 4 |                    |
| **Actual Positive**     | **False Negative (FN)**: The number of incorrect predictions where an instance is predicted as negative, but it is actually positive (**Type II error**). 5 | **True Positive (TP)**: The number of correct predictions that an instance is positive. 6                                                                  |                    |

---

## 🔑 Significance of the Four Outcomes

1. **True Positive (TP)**: The model correctly identified a positive case. (Desired outcome)
    
2. **True Negative (TN)**: The model correctly identified a negative case. (Desired outcome)
    
3. **False Positive (FP)** (Type I Error): The model incorrectly flagged a negative case as positive.
    
4. **False Negative (FN)** (Type II Error): The model incorrectly missed a positive case, classifying it as negative. This error is often the **most critical** in real-world applications (e.g., missing a disease diagnosis).
![[Pasted image 20251111232040.png]]

---

## 🔬 Key Metrics Derived from the Matrix

The Confusion Matrix is fundamental for calculating performance metrics, especially when dealing with imbalanced datasets where simple accuracy is misleading.

- Accuracy: Measures overall correctness.
    
    $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
    
- Precision: Of all the cases the model predicted positive, how many were actually positive? (Focuses on the quality of positive predictions).
    
    $$\text{Precision} = \frac{TP}{TP + FP}$$
    
- Recall (Sensitivity): Of all the cases that were actually positive, how many did the model correctly find? (Focuses on the model's ability to find all positive samples).
    
    $$\text{Recall} = \frac{TP}{TP + FN}$$
    
- **F1-Score**: The harmonic mean of Precision and Recall, providing a balanced measure.
    $$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

Alternatively, expanding the terms:

$$\text{F1-Score} = \frac{2 \times TP}{2 \times TP + FP + FN}$$

###### Specificity (True Negative Rate)

Specificity measures the proportion of **actual negative cases** that were **correctly identified as negative** (True Negatives)3.

**Specificity Formula:**

$$\text{Specificity} = \frac{TN}{TN + FP}$$


---

## 🔄 K-folds Cross-Validation: In Detail

K-fold cross-validation is a crucial technique used to assess a machine learning model's performance and ensure it **generalizes well to unseen data**2.
![[Pasted image 20251111232534.png]]

---

### 1. Mechanism and Process

The process systematically divides the dataset to ensure every data point contributes to both training and validation:

1. **Data Partitioning**: The entire dataset is randomly divided into **$k$ equal-sized subsets** or **"folds"**.
    
    - The value of $k$ is chosen based on the dataset size and available computational resources; common choices are $k=5$ or $k=10$.
        
2. **Model Training and Validation**: The model is trained and validated for **$k$ iterations.
    
    - In each iteration, **one fold** is designated as the **validation/test set**.
        
    - The **remaining $k-1$ folds** are combined to form the **training set**.
        
    - This ensures that **every instance** in the dataset is used for both training and validation at least once8.
        
3. **Performance Estimation**: After all $k$ iterations are complete, the performance metrics (e.g., accuracy, precision, recall) obtained from each fold are **averaged**. This average provides a comprehensive and reliable estimate of the model's performance.

•Stratification Option: In cases of imbalanced datasets, stratified k-fold cross-validation can be employed to ensure that each fold has a similar distribution of classes, which helps maintain the representativeness of each fold.

---

### 2. Advantages and Disadvantages

#### ✅ Advantages

- **Mitigation of Overfitting**: By testing the model across multiple different splits, it helps **reduce the risk of overfitting**, ensuring the model generalizes well rather than just memorizing the training set.
    
- **Better Generalization**: It provides a more **robust and better estimate** of how the model will perform on new, independent data compared to a single train-test split.
    
- **Efficient Data Use**: Since every instance is used for both training and validation, it **maximizes the utilization of available data**, which is especially important for smaller datasets13.
    
- **Variance Reduction**: Averaging the results across $k$ folds helps **smooth out the variability** that can occur from random sampling in a single split14.
    

#### ❌ Disadvantages

- **Computational Cost**: K-fold cross-validation is **computationally intensive** because the model must be trained and evaluated **$k$ times**15. This is a major factor for large datasets or complex models.
    
- **Choice of K**: Selecting the appropriate value for $k$ is crucial16. A very small $k$ can lead to high variance, while a very large $k$ increases the computational expense17.
    
- **Stratification**: In cases of imbalanced datasets, **stratified k-fold cross-validation** can be used to ensure each fold has a similar distribution of classes, maintaining the representativeness of each fold18.


## 🔄 How K-Folds Cross-Validation Works

K-folds cross-validation is a technique designed to estimate the true performance of a model on unseen data by cycling through multiple train-test splits222.

---

### 1. Data Splitting (Partitioning)

- The **entire dataset** is randomly divided into **$k$ subsets** or "folds" of approximately equal size3.
    
- Common values chosen for the hyperparameter $k$ are 5 or 10, but the value can be adjusted based on the size of the dataset4.
    

### 2. Model Training and Validation Loop

The model is trained and validated for **$k$ iterations** (runs)5. The process is repeated $k$ times to ensure every data point is used for both training and validation6:

|**Iteration**|**Validation/Test Set**|**Training Set**|
|---|---|---|
|**Run 1**|Fold 1|Folds 2, 3, 4, $\dots$, $k$|
|**Run 2**|Fold 2|Folds 1, 3, 4, $\dots$, $k$|
|**$\dots$**|$\dots$|$\dots$|
|**Run k**|Fold $k$|Folds 1, 2, 3, $\dots$, $k-1$|

- In each iteration, **one fold** is temporarily set aside as the **validation set**7.
    
- The **remaining $k-1$ folds** are combined to form the **training set**, which is used to fit the model8.
    

### 3. Performance Measurement (Averaging)

- After completing all $k$ iterations, the performance metrics (such as accuracy, precision, recall, F1 score, etc.) obtained from the validation step in each run are collected9.
    
- These $k$ individual performance scores are then **averaged**10.
    
- This average provides a **more comprehensive and reliable view** of the model's performance on unseen data than a single train-test split11.
    

The technique helps reduce the risk of overfitting by testing the model's generalization capability across different subsets of the data.

---
•Regularization: Bias and Variance, Overfitting and Underfitting, L1 and L2 Regularization, Regularized Linear Regression, Decision Trees (ID3, C4.5, CART), Confusion matrix, k-folds cross-validation, K Nearest Neighbour, Support vector machine.