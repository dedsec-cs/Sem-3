# Introduction to Curve Fitting

## What Is Curve Fitting?

**Curve Fitting** is a mathematical process of constructing a continuous function, or a "curve," that best represents the relationship between two or more variables in a given set of discrete data points.

* **Goal:** To find a simple, predictive mathematical model that summarizes the trend hidden within the scattered data.
* **Method:** We almost always use the **Method of Least Squares** to define what "best" means—it minimizes the total squared vertical distances (residuals) between the data points and the fitted curve.

---

# Question 1: Fitting a Straight Line

The task is to fit a straight line, which is an application of **Linear Regression**, to the data:

| X | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Y | 1 | 1.8 | 3.3 | 4.5 | 6.3 |

Here, the number of data points is $n=5$.

## Normal Equations for a Straight Line

**Normal Equations** are the system of simultaneous linear equations derived by applying the **Method of Least Squares** to a chosen model. They are crucial because solving them gives you the optimal values for the model's parameters (the coefficients) that **minimize the Sum of Squared Errors (SSE)**.

To derive them, we take the partial derivatives of the SSE with respect to each unknown coefficient and set them equal to zero (a technique from advanced calculus used to find minima).

### Normal Equations for $\hat{y} = a + bx$

The model is $\hat{y} = a + bx$. The parameters to solve for are **$a$** (intercept) and **$b$** (slope).

1.  $\sum y = na + b \sum x$
2.  $\sum xy = a \sum x + b \sum x^2$

### Normal Equations for $\hat{y} = ax + b$

This is the exact same straight line model, just with the parameters named differently: $\hat{y} = b + ax$. The role of $a$ and $b$ is swapped.

1.  $\sum y = n b + a \sum x$
2.  $\sum xy = b \sum x + a \sum x^2$

Since the two forms represent the same geometric line, the final equation will be identical, even though the parameter labels might change.

## Calculation Table

First, we need the summation terms:

| X             | Y               | XY               | $X^2$           |
| ------------- | --------------- | ---------------- | --------------- |
| 0             | 1.0             | 0.0              | 0               |
| 1             | 1.8             | 1.8              | 1               |
| 2             | 3.3             | 6.6              | 4               |
| 3             | 4.5             | 13.5             | 9               |
| 4             | 6.3             | 25.2             | 16              |
| $\sum x = 10$ | $\sum y = 16.9$ | $\sum xy = 47.1$ | $\sum x^2 = 30$ |

And $n=5$.

## Fitting the Equation $\hat{y} = a + bx$

Substitute the sums into the Normal Equations:

1.  $16.9 = 5a + 10b$
2.  $47.1 = 10a + 30b$

We solve this system of equations.
Multiply equation (1) by 2:
$$2 \times (1): \quad 33.8 = 10a + 20b \quad \text{(1')}$$

Subtract (1') from (2):
$$\begin{aligned} 47.1 &= 10a + 30b \\ - (33.8 &= 10a + 20b) \\ \hline 13.3 &= 0 + 10b \end{aligned}$$
$$\mathbf{b} = \frac{13.3}{10} = \mathbf{1.33}$$

Substitute $b=1.33$ back into equation (1):
$$\begin{aligned} 16.9 &= 5a + 10(1.33) \\ 16.9 &= 5a + 13.3 \\ 5a &= 16.9 - 13.3 \\ 5a &= 3.6 \\ \mathbf{a} &= \frac{3.6}{5} = \mathbf{0.72} \end{aligned}$$

The fitted equation is:
$$\hat{y} = 0.72 + 1.33x$$

## Fitting the Equation $\hat{y} = ax + b$

In this form, $\mathbf{a}$ is the slope and $\mathbf{b}$ is the intercept. Since the geometric line is the same, we just rename the coefficients:

* Slope ($a$) $= 1.33$
* Intercept ($b$) $= 0.72$

The fitted equation is:
$$\hat{y} = 1.33x + 0.72$$

---

# Question 2: Fitting the Non-Linear Equation

The data is:

| X | Y |
|---|---|
| 0.1 | 21 |
| 0.2 | 11 |
| 0.4 | 7 |
| 0.5 | 6 |
| 1 | 5 |

The equation to fit is:
$$y = \frac{C_0}{x} + 4\sqrt{x}$$

This is a **Non-Linear Model**, but we can use an advanced technique: **Linearization by Substitution**.

### 1. Rearrange the Equation

We want the equation to look like the standard linear model, $\hat{Y} = A + BX$.

First, move the $\mathbf{4\sqrt{x}}$ term to the left side:
$$y - 4\sqrt{x} = \frac{C_0}{x}$$

Now, let's define new variables:
* Let the new dependent variable be $\mathbf{Y'} = y - 4\sqrt{x}$
* Let the new independent variable be $\mathbf{X'} = \frac{1}{x}$
* Let the unknown coefficient be $\mathbf{C'} = C_0$

The equation becomes the simple linear model:
$$\mathbf{Y'} = C' \mathbf{X'}$$
(This is a straight line passing through the origin, with intercept $A=0$.)

### 2. Calculate Transformed Data

We need to create the $\mathbf{X'}$ and $\mathbf{Y'}$ columns:

| X                         | Y                           | $\sqrt{x}$ | $4\sqrt{x}$ | $\mathbf{Y'} = y - 4\sqrt{x}$ | $\mathbf{X'} = 1/x$ | $\mathbf{X'Y'}$                | $(\mathbf{X'})^2$               |
| ------------------------- | --------------------------- | ---------- | ----------- | ----------------------------- | ------------------- | ------------------------------ | ------------------------------- |
| 0.1                       | 21                          | 0.316      | 1.265       | $\mathbf{19.735}$             | $\mathbf{10.0}$     | 197.35                         | 100                             |
| 0.2                       | 11                          | 0.447      | 1.789       | $\mathbf{9.211}$              | $\mathbf{5.0}$      | 46.055                         | 25                              |
| 0.4                       | 7                           | 0.632      | 2.530       | $\mathbf{4.470}$              | $\mathbf{2.5}$      | 11.175                         | 6.25                            |
| 0.5                       | 6                           | 0.707      | 2.828       | $\mathbf{3.172}$              | $\mathbf{2.0}$      | 6.344                          | 4                               |
| 1.0                       | 5                           | 1.000      | 4.000       | $\mathbf{1.000}$              | $\mathbf{1.0}$      | 1.000                          | 1                               |
| $\sum X' = \mathbf{20.5}$ | $\sum Y' = \mathbf{37.588}$ |            |             |                               |                     | $\sum X'Y' = \mathbf{261.924}$ | $\sum (X')^2 = \mathbf{136.25}$ |

$n=5$.

### 3. Apply Least Squares to $\mathbf{Y'} = C' \mathbf{X'}$

Since the model has **no intercept**, the Normal Equation simplifies to one equation:

$$\sum X'Y' = C' \sum (X')^2$$

Solve for $C'$:
$$C' = \frac{\sum X'Y'}{\sum (X')^2}$$

$$C' = \frac{261.924}{136.25} \approx 1.9223$$

### 4. Back-Substitute to the Original Equation

Since $C' = C_0$, the fitted parameter is $\mathbf{C_0 \approx 1.9223}$.

The final fitted equation is:

$$\hat{y} = \frac{1.9223}{x} + 4\sqrt{x}$$

---
## Note

- Fit A Straight Line
$y = ax + b$ 
$y = a + bx$

- Fit A Second Degree Parabola
$y = a + bx + cx^2$ 
$y = ax^2 + bx + c$

$\sum{y} = an + b\sum{x} + c\sum{x^2}$ 
$\sum{xy} = a\sum{x} + b \sum{x^2} + c\sum{x^3}$
$\sum{x^2 y} = a\sum{x^2} + b\sum{x^3} + c\sum{x^4}$

---
3. Fit $y = C_0x + \frac{C_1}{\sqrt{x}}$

| X   | Y   |
| --- | --- |
| 0.2 | 16  |
| 0.3 | 14  |
| 0.5 | 11  |
| 1   | 6   |
| 2   | 3   |

4. Fit a Curve $y = ab^x$

| X   | Y     |
| --- | ----- |
| 2   | 144   |
| 3   | 172.8 |
| 4   | 207.4 |
| 5   | 248.8 |
| 6   | 298.5 |

5. Fit $y = ax^b$

| X   | Y    |
| --- | ---- |
| 1   | 7.1  |
| 2   | 27.8 |
| 3   | 62.1 |
| 4   | 110  |
| 5   | 161  |

6. Fit $PV^r = C$ to the following data

| P   | V    |
| --- | ---- |
| 0.5 | 1620 |
| 1   | 1000 |
| 1.5 | 750  |
| 2   | 620  |
| 2.5 | 520  |
| 3   | 460  |

7. Fit $PV^r = C$ to the following data

| V   | P    |
| --- | ---- |
| 50  | 64.7 |
| 60  | 51.3 |
| 70  | 40.5 |
| 90  | 25.9 |
| 100 | 78   |

8. Fit $y = ae^{bx}$

| X   | Y      |
| --- | ------ |
| 2   | 4.077  |
| 4   | 11.084 |
| 6   | 30.128 |
| 8   | 81.897 |
| 10  | 222.62 |

9. Fit $f(t) = ae^{-3t} + be^{-2t}$

| t   | f(t) |
| --- | ---- |
| 0.1 | 0.76 |
| 0.2 | 0.58 |
| 0.3 | 0.44 |
| 0.4 | 0.35 |
 