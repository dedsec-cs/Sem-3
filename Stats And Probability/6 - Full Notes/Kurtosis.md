# Moment Coefficient of Skewness

## Definition

This is the most common method for measuring skewness, developed by Karl Pearson. It uses the second and third central moments ($\mu_2$ and $\mu_3$) to create a pure, dimensionless number that quantifies the degree and direction of asymmetry.

* The **second central moment ($\mu_2$)** measures the **variance** (spread).
* The **third central moment ($\mu_3$)** measures the **skewness** (asymmetry).

By comparing the skewness to the spread, we get a standardized measure.

## Formula

There are two main coefficients based on moments:

### 1. Beta 1 ($\beta_1$)

This coefficient measures the *degree* of skewness but, because it squares $\mu_3$, it will always be positive. Therefore, it doesn't tell you the *direction* (left or right) of the skew.

$$\beta_1 = \frac{\mu_3^2}{\mu_2^3}$$

* **If $\beta_1 = 0$**, the distribution is symmetrical.
* **If $\beta_1 > 0$**, the distribution is skewed.

### 2. Underroot of Beta 1 ($\gamma_1$ or $\sqrt{\beta_1}$)

This is the more widely used **moment coefficient of skewness** because it preserves the sign (positive or negative) of $\mu_3$, which tells us the *direction* of the skew.

$$\gamma_1 = \sqrt{\beta_1} = \frac{\mu_3}{\mu_2^{3/2}}$$

*(Note: $\mu_2^{3/2}$ is the same as $\sqrt{\mu_2^3}$ or $(\sqrt{\mu_2})^3$. Since $\sqrt{\mu_2}$ is the standard deviation $\sigma$, this formula is often written as $\frac{\mu_3}{\sigma^3}$.)*

**Interpretation:**
* **If $\gamma_1 = 0$:** The distribution is symmetrical.
* **If $\gamma_1 > 0$ (Positive):** The distribution is **positively skewed** (tail to the right).
* **If $\gamma_1 < 0$ (Negative):** The distribution is **negatively skewed** (tail to the left).

---

## Problem Solving On Moment Coefficient Of Skewness

**Question:** The second and third central moments of a distribution are $\mu_2 = 16$ and $\mu_3 = -40$. Calculate the moment coefficient of skewness ($\gamma_1$) and interpret the result.

**Solution:**
We are given:
* $\mu_2 = 16$ (Variance)
* $\mu_3 = -40$

We will use the formula for $\gamma_1$:
$$\gamma_1 = \frac{\mu_3}{\mu_2^{3/2}}$$

**Step 1: Calculate the denominator ($\mu_2^{3/2}$).**
* This is $(\sqrt{16})^3$.
* $\sqrt{16} = 4$
* $4^3 = 4 \times 4 \times 4 = 64$
* So, $\mu_2^{3/2} = 64$.

**Step 2: Calculate $\gamma_1$.**
* $$\gamma_1 = \frac{-40}{64}$$
* $$\gamma_1 = -0.625$$

**Answer:** The moment coefficient of skewness is **-0.625**.
**Interpretation:** Since the coefficient is negative, the distribution is **negatively skewed**.

---

# Kurtosis

## Definition

Kurtosis is a measure of the "peakedness" or "tailedness" of a distribution. It describes how sharp the central peak is and how heavy the tails are, relative to a **Normal Distribution** (which is the benchmark).

* A high kurtosis distribution has a **sharp peak and heavy tails** (meaning more data in the tails, or more outliers).
* A low kurtosis distribution has a **flat peak and light tails** (meaning less data in the tails).

## Types Of Kurtosis

We compare the shape of a distribution to the **Mesokurtic** (Normal) curve.



1.  **Leptokurtic**
    * **Shape:** More peaked and has heavier tails than a normal distribution.
    * **Data:** More of the data is clustered in the center *and* in the tails.
    * This means there is a higher probability of extreme values (outliers).

2.  **Mesokurtic**
    * **Shape:** This is the normal distribution itself. It is the "gold standard" that kurtosis is measured against.
    * Its peakedness and tail weight are considered "normal."

3.  **Platykurtic**
    * **Shape:** Flatter and has lighter tails than a normal distribution.
    * **Data:** The data is more spread out and uniform, with fewer values clustered in the center and fewer extreme values in the tails.

## Formula For Kurtosis

The coefficient of kurtosis is denoted by **Beta 2 ($\beta_2$)**. It is calculated using the fourth and second central moments.

$$\beta_2 = \frac{\mu_4}{\mu_2^2}$$

* $\mu_4$ = The fourth central moment
* $\mu_2$ = The second central moment (Variance)

## Measure Of Kurtosis

We use the value of $\beta_2$ to determine the type of kurtosis.

* **For a Mesokurtic (Normal) distribution, $\beta_2 = 3$.** This is our baseline.

* **If $\beta_2 > 3$:** The distribution is **Leptokurtic** (sharp peak, heavy tails).
* **If $\beta_2 = 3$:** The distribution is **Mesokurtic** (normal).
* **If $\beta_2 < 3$:** The distribution is **Platykurtic** (flat peak, light tails).

### Excess Kurtosis ($\gamma_2$)

Because 3 is the baseline, many statisticians prefer to use the **"excess kurtosis"** coefficient, $\gamma_2$. This formula normalizes the measure so that 0 is the baseline.

**Formula:**
$$\gamma_2 = \beta_2 - 3$$

**Interpretation:**
* **$\gamma_2 > 0$:** Leptokurtic
* **$\gamma_2 = 0$:** Mesokurtic
* **$\gamma_2 < 0$:** Platykurtic