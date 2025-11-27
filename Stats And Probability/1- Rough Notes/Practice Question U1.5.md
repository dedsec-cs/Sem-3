### Skewness

**Skewness** measures the asymmetry of a distribution.

-----

**Example:**

  * Karl Pearson coefficient of skewness of a distribution is 0.32, its standard deviation is 6.5 and mean is 29.6. find the mode of the distribution.

**Solution:**
We use Karl Pearson's first coefficient of skewness formula:
$$S_k = \frac{\bar{X} - Z}{\sigma}$$
Where $S_k$ is the coefficient of skewness, $\bar{X}$ is the mean, $Z$ is the mode, and $\sigma$ is the standard deviation.

Given: $S_k = 0.32$, $\bar{X} = 29.6$, $\sigma = 6.5$.
Rearranging the formula to solve for the Mode ($Z$):
$$Z = \bar{X} - S_k \cdot \sigma$$
$$Z = 29.6 - (0.32 \cdot 6.5)$$
$$Z = 29.6 - 2.08$$
$$Z = \mathbf{27.52}$$

-----

**Example:**

  * Calculate Karl Pearson’s Coefficient of skewness from the table given below:

| X | 14.5 | 15.5 | 16.5 | 17.5 | 18.5 | 19.5 | 20.5 | 21.5 |
|---|---|---|---|---|---|---|---|---|
| f | 35 | 40 | 48 | 100 | 125 | 87 | 43 | 22 |

**Solution:**
We need to calculate $\bar{X}$, the Mode ($Z$), and the Standard Deviation ($\sigma$).
$N = \sum f = 500$.

1.  **Mode ($Z$):** The value of $X$ with the highest frequency ($f=125$) is $\mathbf{Z = 18.5}$.
2.  **Mean ($\bar{X}$):** $\sum FX = 9033$.
    $$\bar{X} = \frac{9033}{500} = \mathbf{18.066}$$
3.  **Standard Deviation ($\sigma$):** $\sum F(X-\bar{X})^2 \approx 1572.752$.
    $$\sigma = \sqrt{\frac{1572.752}{500}} \approx \mathbf{1.775}$$
4.  **Skewness ($S_k$):**
    $$S_k = \frac{\bar{X} - Z}{\sigma} = \frac{18.066 - 18.5}{1.775} = \frac{-0.434}{1.775} \approx \mathbf{-0.245}$$


-----

### Kurtosis

**Kurtosis** measures the relative peakedness or flatness of a distribution compared to a normal distribution.

-----

**Example:**

  * For a distribution, the mean is 10, variance is 16, $\gamma_1$ is +1 and $\beta_2$ is 4. Comment about the nature of distribution. Also find third central moment.

**Solution:**
Given: $\text{Variance } (\mu_2) = 16$, $\sigma = \sqrt{16} = 4$, $\gamma_1 = 1$, $\beta_2 = 4$.

1.  **Third Central Moment ($\mu_3$):**
    The skewness coefficient $\gamma_1$ is defined as $\gamma_1 = \frac{\mu_3}{\sigma^3}$.
    $$\mu_3 = \gamma_1 \cdot \sigma^3 = 1 \cdot (4)^3 = \mathbf{64.0}$$

2.  **Comment on Nature of Distribution:**

      * **Skewness:** Since $\gamma_1 = +1$ (a positive value), the distribution is **Positively Skewed** (skewed to the right).
      * **Kurtosis:** The Kurtosis coefficient is $\beta_2 = 4$.
          * Since $\beta_2 > 3$, the distribution is **Leptokurtic**. It is more peaked than a normal curve, with heavier tails.

-----

**Example:**

  * The first four moment about the working mean 28.5 of a distribution are 0.294, 7.144, 42.409 and 454.98. Calculate the first four moment about mean. Also evaluate $\beta_1$ and $\beta_2$ and comment upon the skewness and kurtosis of the distribution.

**Solution:**
Given: $A=28.5$. Raw moments ($\mu'_r$): $\mu'_1=0.294, \mu'_2=7.144, \mu'_3=42.409, \mu'_4=454.98$.

**1. First Four Central Moments ($\mu_r$):**

  * $\mathbf{\mu_1} = \mathbf{0}$
  * $\mathbf{\mu_2} = \mu'_2 - (\mu'_1)^2 = 7.144 - (0.294)^2 \approx \mathbf{7.058}$
  * $\mathbf{\mu_3} = \mu'_3 - 3\mu'_2 \mu'_1 + 2(\mu'_1)^3 \approx 42.409 - 3(7.144)(0.294) + 2(0.294)^3 \approx \mathbf{36.159}$
  * $\mathbf{\mu_4} = \mu'_4 - 4\mu'_3 \mu'_1 + 6\mu'_2 (\mu'_1)^2 - 3(\mu'_1)^4 \approx \mathbf{408.790}$

**2. Skewness ($\beta_1$):**
$$\beta_1 = \frac{\mu_3^2}{\mu_2^3} = \frac{36.159^2}{7.058^3} \approx \mathbf{3.719}$$

  * **Comment on Skewness:** Since $\beta_1 > 0$, the distribution is **Positively Skewed**.

**3. Kurtosis ($\beta_2$):**
$$\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{408.790}{7.058^2} \approx \mathbf{8.207}$$

  * **Comment on Kurtosis:** Since $\beta_2 > 3$, the distribution is **Leptokurtic**.

-----

**Example:**

  * The first four central moments of a distribution are 0, 2.3, 0.9, and 15.65. Test the skewness and kurtosis of the distribution. Also discuss the nature of the curve.

**Solution:**
Given: $\mu_1=0, \mu_2=2.3, \mu_3=0.9, \mu_4=15.65$.

**1. Skewness Test ($\beta_1, \gamma_1$):**
$$\beta_1 = \frac{\mu_3^2}{\mu_2^3} = \frac{0.9^2}{2.3^3} \approx \mathbf{0.0666}$$
$$\gamma_1 = \frac{\mu_3}{\sqrt{\mu_2^3}} = \frac{0.9}{\sqrt{2.3^3}} \approx \mathbf{0.258}$$

  * **Nature:** Since $\gamma_1 > 0$, the distribution is **Positively Skewed**.

**2. Kurtosis Test ($\beta_2, \gamma_2$):**
$$\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{15.65}{2.3^2} \approx \mathbf{2.958}$$
$$\gamma_2 = \beta_2 - 3 \approx 2.958 - 3 \approx \mathbf{-0.042}$$

  * **Nature:** Since $\beta_2 < 3$ (or $\gamma_2 < 0$), the distribution is **Platykurtic**.

**3. Discussion of the Curve's Nature:**
The distribution is slightly **Positively Skewed** and is **Platykurtic** (flatter and has lighter tails than a normal distribution).

-----

**Example:**

  * If a distribution has a high kurtosis, it is called:
        \* Leptokurtic
        \* Platykurtic
        \* Mesokurtic
        \* Skewed

**Solution:**
If a distribution has a high kurtosis ($\beta_2 > 3$), it is called:
$$\mathbf{\text{Leptokurtic}}$$

***
### Mixed/General Questions

**Example:**

  * Compute for the following data:

| Wages (Rs.) | 0-25 | 25-50 | 50-75 | 75-100 | 100-125 | 125-above |
|---|---|---|---|---|---|---|
| No. of persons | 10 | 30 | 40 | 20 | 25 | 15 |

**Solution:**
Since no specific measure is requested, we compute the Mean, Median, and Mode. We assume the last class is **125-150** ($h=25$). $N=140$.

**1. Mean ($\bar{X}$):**
Midpoints ($m$): 12.5, 37.5, 62.5, 87.5, 112.5, 137.5. $\sum Fm = 10375$.
$$\bar{X} = \frac{\sum Fm}{N} = \frac{10375}{140} \approx \mathbf{74.11}$$

**2. Median ($M$):**
$N/2 = 70$. Median Class is **50-75** ($L=50, f_M=40, c.f._{p}=40, h=25$).
$$M = 50 + \left(\frac{70 - 40}{40}\right) \times 25 = 50 + (0.75 \times 25) = 50 + 18.75 = \mathbf{68.75}$$

**3. Mode ($Z$):**
Modal Class is **50-75** ($L=50, f_1=40, f_0=30, f_2=20, h=25$).
$$Z = 50 + \left(\frac{40 - 30}{2(40) - 30 - 20}\right) \times 25 = 50 + \left(\frac{10}{30}\right) \times 25 \approx 50 + 8.33 = \mathbf{58.33}$$

-----

**Example:**

  * An incomplete distribution is given below. Given that median value is 46 and N=229.

| x | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 |
|---|---|---|---|---|---|---|---|
| f | 12 | 30 | X | 65 | Y | 25 | 18 |

**Solution:**
Let $X$ and $Y$ be the missing frequencies.

**1. Total Frequency Equation:**
$$12 + 30 + X + 65 + Y + 25 + 18 = 229$$
$$150 + X + Y = 229 \implies \mathbf{X + Y = 79}$$

**2. Median Equation:**
Given $M=46$. The Median Class is **40-50** ($L=40, h=10, f_M=65$).
$N/2 = 229/2 = 114.5$.
$c.f._{p}$ (c.f. of preceding class, 30-40) $= 12 + 30 + X = 42 + X$.
$$M = L + \left(\frac{N/2 - c.f._{p}}{f_M}\right) \times h$$
$$46 = 40 + \left(\frac{114.5 - (42 + X)}{65}\right) \times 10$$
$$6 = \left(\frac{72.5 - X}{65}\right) \times 10 \implies 39 = 72.5 - X$$
$$X = 72.5 - 39 = \mathbf{33.5}$$

**3. Find Y:**
$$Y = 79 - X = 79 - 33.5 = \mathbf{45.5}$$

Since frequencies must be integers, the closest integer solution is $\mathbf{X=34}$ and $\mathbf{Y=45}$ (or $X=33, Y=46$), but the mathematically calculated values are $\mathbf{X=33.5}$ and $\mathbf{Y=45.5}$.

-----

**Example:**

  * The mean of the range, mode and median of the data: 5, 10, 3, 6, 4, 8, 9, 3, 15, 2, 9, 4, 19, 11, 4.

**Solution:**
Data ($N=15$): 2, 3, 3, 4, 4, 4, 5, **6**, 8, 9, 9, 10, 11, 15, 19.

1.  **Range ($R$):** $L - S = 19 - 2 = \mathbf{17}$.
2.  **Mode ($Z$):** Most frequent value (4 occurs 3 times) is $\mathbf{4}$.
3.  **Median ($M$):** $\left(\frac{15+1}{2}\right)^{\text{th}} = 8^{\text{th}}$ term is $\mathbf{6}$.

**Mean of (Range, Mode, Median):**
$$\bar{X}_{R, Z, M} = \frac{R + Z + M}{3} = \frac{17 + 4 + 6}{3} = \frac{27}{3} = \mathbf{9}$$
The correct option is **9**.

-----

**Example:**

  * The values of quartile and quartile deviation of the data: 17, 2, 7, 27, 15, 5, 14, 8.

**Solution:**
Data ($N=8$): 2, 5, 7, 8, 14, 15, 17, 27.

1.  **First Quartile ($Q_1$):** Position $= \frac{1(8+1)}{4} = 2.25^{\text{th}}$.
    $$Q_1 = x_2 + 0.25(x_3 - x_2) = 5 + 0.25(7 - 5) = \mathbf{5.5}$$
2.  **Third Quartile ($Q_3$):** Position $= \frac{3(8+1)}{4} = 6.75^{\text{th}}$.
    $$Q_3 = x_6 + 0.75(x_7 - x_6) = 15 + 0.75(17 - 15) = \mathbf{16.5}$$
3.  **Quartile Deviation ($QD$):**
    $$QD = \frac{Q_3 - Q_1}{2} = \frac{16.5 - 5.5}{2} = \frac{11}{2} = \mathbf{5.5}$$
    The correct value is **5.5**.

-----

**Example:**

  * An incomplete distribution of families according to their expenditure per week is given below. The median and mode for the distribution are Rs 25 and Rs 24 respectively. Calculate the missing frequencies.

| Expenditure | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 |
|---|---|---|---|---|---|
| No. of families ($F$) | 14 | $X$ | 27 | $Y$ | 15 |

**Solution:**
Let $X = f_{10-20}$ and $Y = f_{30-40}$. $h=10$.
Given $M=25$ and $Z=24$. Both fall in the **20-30** class ($L=20$).

**1. Setup Total Frequency:** $N = 14 + X + 27 + Y + 15 = 56 + X + Y$.

**2. Median Equation (M=25):**
$L=20, f_M=27, c.f._{p} = 14 + X$.
$$25 = 20 + \left(\frac{(56 + X + Y)/2 - (14 + X)}{27}\right) \times 10$$
$$5 \times 27 = 10 \times \left(\frac{56 + X + Y - 28 - 2X}{2}\right)$$
$$135 = 5 \times (28 - X + Y) \implies 27 = 28 - X + Y \implies \mathbf{X - Y = 1 \quad (Eq. A)}$$

**3. Mode Equation (Z=24):**
$L=20, f_1=27, f_0=X, f_2=Y$.
$$24 = 20 + \left(\frac{27 - X}{2(27) - X - Y}\right) \times 10$$
$$4(54 - X - Y) = 10(27 - X)$$
$$216 - 4X - 4Y = 270 - 10X \implies 6X - 4Y = 54 \implies \mathbf{3X - 2Y = 27 \quad (Eq. B)}$$

**4. Solve Simultaneous Equations:**
From (A): $X = 1 + Y$. Substitute into (B):
$$3(1 + Y) - 2Y = 27$$
$$3 + 3Y - 2Y = 27 \implies Y = 27 - 3 = \mathbf{24}$$
$$X = 1 + 24 = \mathbf{25}$$
The missing frequencies are $\mathbf{X=25}$ and $\mathbf{Y=24}$.

-----

**Example:**

  * Calculate the mean and standard deviation for the following data:

| Size of item ($X$) | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| Frequency ($F$) | 4 | 5 | 8 | 13 | 9 | 6 | 3 |

**Solution:**
$N = \sum F = 48$. $\sum FX = 432$.

**1. Mean ($\bar{X}$):**
$$\bar{X} = \frac{\sum FX}{N} = \frac{432}{48} = \mathbf{9.0}$$

**2. Standard Deviation ($\sigma$):**
$\sum F(X - \bar{X})^2 = 124$ (calculated in a previous problem).
$$\sigma = \sqrt{\frac{\sum F(X - \bar{X})^2}{N}} = \sqrt{\frac{124}{48}} \approx \sqrt{2.5833} \approx \mathbf{1.61}$$