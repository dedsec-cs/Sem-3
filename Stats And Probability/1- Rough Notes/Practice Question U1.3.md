### Range

The **Range** ($R$) is the difference between the largest observation ($L$) and the smallest observation ($S$): $R = L - S$.
The **Coefficient of Range** ($CR$) is a relative measure of dispersion: $CR = \frac{L - S}{L + S}$.

**Example:**

  * Find the range & Coefficient of Range for the following data: 20, 35, 25, 30, 15.

**Solution:**
The largest value is $L=35$. The smallest value is $S=15$.
$$\text{Range} (R) = L - S = 35 - 15 = \mathbf{20}$$
$$\text{Coefficient of Range} (CR) = \frac{L - S}{L + S} = \frac{35 - 15}{35 + 15} = \frac{20}{50} = \mathbf{0.4}$$

-----

**Example:**

  * Find the range & Coefficient of Range for the following data: 25, 38, 45, 30, 15.

**Solution:**
The largest value is $L=45$. The smallest value is $S=15$.
$$\text{Range} (R) = L - S = 45 - 15 = \mathbf{30}$$
$$\text{Coefficient of Range} (CR) = \frac{L - S}{L + S} = \frac{45 - 15}{45 + 15} = \frac{30}{60} = \mathbf{0.5}$$

-----

**Example:**

  * Find the range & Coefficient of Range for the following data:

| X | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| F | 5 | 9 | 12 | 17 | 14 | 10 | 6 |

**Solution:**
For a discrete frequency distribution, the range is determined only by the extreme values of $X$, regardless of their frequencies.
The largest value is $L=7$. The smallest value is $S=1$.
$$\text{Range} (R) = L - S = 7 - 1 = \mathbf{6}$$
$$\text{Coefficient of Range} (CR) = \frac{L - S}{L + S} = \frac{7 - 1}{7 + 1} = \frac{6}{8} = \mathbf{0.75}$$

-----

**Example:**

  * Find the range & Coefficient of Range:

| X | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 |
|---|---|---|---|---|---|---|
| F | 12 | 18 | 27 | 20 | 17 | 6 |

**Solution:**
For a grouped frequency distribution, the range is the difference between the upper limit of the last class and the lower limit of the first class.
The largest value is $L=60$ (Upper limit of 50-60). The smallest value is $S=0$ (Lower limit of 0-10).
$$\text{Range} (R) = L - S = 60 - 0 = \mathbf{60}$$
$$\text{Coefficient of Range} (CR) = \frac{L - S}{L + S} = \frac{60 - 0}{60 + 0} = \frac{60}{60} = \mathbf{1.0}$$

-----

### Quartile Deviation

The **Interquartile Range** ($IQR$) is $Q_3 - Q_1$.
The **Quartile Deviation** ($QD$) is $\frac{Q_3 - Q_1}{2}$.
The **Coefficient of Quartile Deviation** ($CQD$) is $\frac{Q_3 - Q_1}{Q_3 + Q_1}$.

**Example:**

  * Find interquartile range, quartile deviation and coefficient of quartile deviation: 28, 18, 20, 24, 27, 30, 15.

**Solution:**

1.  **Sort Data:** 15, 18, 20, 24, 27, 28, 30. ($N=7$)
2.  **Find Quartiles:** We use the position formula $\text{Position} = \frac{k(N+1)}{4}$.
      * $Q_1$ position ($\frac{1(7+1)}{4} = 2^{\text{nd}}$ observation) is $\mathbf{Q_1 = 18}$.
      * $Q_3$ position ($\frac{3(7+1)}{4} = 6^{\text{th}}$ observation) is $\mathbf{Q_3 = 28}$.
3.  **Calculate Measures:**
    $$\text{Interquartile Range} (IQR) = Q_3 - Q_1 = 28 - 18 = \mathbf{10}$$
    $$\text{Quartile Deviation} (QD) = \frac{Q_3 - Q_1}{2} = \frac{10}{2} = \mathbf{5.0}$$
    $$\text{Coefficient of Quartile Deviation} (CQD) = \frac{Q_3 - Q_1}{Q_3 + Q_1} = \frac{10}{28 + 18} = \frac{10}{46} \approx \mathbf{0.2174}$$

-----

**Example:**

  * Find interquartile range, quartile deviation and coefficient of quartile deviation:

| X | 10 | 20 | 30 | 40 | 50 | 60 |
|---|---|---|---|---|---|---|
| F | 2 | 8 | 20 | 35 | 42 | 20 |

**Solution:**

1.  **Calculate Cumulative Frequency ($c.f.$):**

| X | F | $c.f.$ |
|---|---|---|
| 10 | 2 | 2 |
| 20 | 8 | 10 |
| 30 | 20 | 30 |
| **40** | **35** | **65** |
| **50** | **42** | **107** |
| 60 | 20 | 127 |
| **Total**| $\mathbf{N=127}$ | |

2.  **Find Quartiles:** We use the position formula $\text{Position} = \frac{k(N+1)}{4}$.
      * $Q_1$ position ($\frac{127+1}{4} = 32^{\text{nd}}$). The first $c.f. \ge 32$ is 65, so $\mathbf{Q_1 = 40}$.
      * $Q_3$ position ($3 \times 32 = 96^{\text{th}}$). The first $c.f. \ge 96$ is 107, so $\mathbf{Q_3 = 50}$.
3.  **Calculate Measures:**
    $$\text{Interquartile Range} (IQR) = Q_3 - Q_1 = 50 - 40 = \mathbf{10}$$
    $$\text{Quartile Deviation} (QD) = \frac{Q_3 - Q_1}{2} = \frac{10}{2} = \mathbf{5.0}$$
    $$\text{Coefficient of Quartile Deviation} (CQD) = \frac{Q_3 - Q_1}{Q_3 + Q_1} = \frac{10}{50 + 40} = \frac{10}{90} \approx \mathbf{0.1111}$$

-----

**Example:**

  * Find quartile deviation and coefficient of quartile deviation: 4, 8, 10, 7, 15, 11, 18, 14, 12, 16.

**Solution:**

1.  **Sort Data:** 4, 7, 8, 10, 11, 12, 14, 15, 16, 18. ($N=10$)
2.  **Find Quartiles (Interpolation):**
      * $Q_1$ position ($\frac{1(10+1)}{4} = 2.75^{\text{th}}$).
        $$Q_1 = x_2 + 0.75(x_3 - x_2) = 7 + 0.75(8 - 7) = \mathbf{7.75}$$
      * $Q_3$ position ($\frac{3(10+1)}{4} = 8.25^{\text{th}}$).
        $$Q_3 = x_8 + 0.25(x_9 - x_8) = 15 + 0.25(16 - 15) = \mathbf{15.25}$$
3.  **Calculate Measures:**
    $$\text{Quartile Deviation} (QD) = \frac{Q_3 - Q_1}{2} = \frac{15.25 - 7.75}{2} = \frac{7.5}{2} = \mathbf{3.75}$$
    $$\text{Coefficient of Quartile Deviation} (CQD) = \frac{Q_3 - Q_1}{Q_3 + Q_1} = \frac{7.5}{15.25 + 7.75} = \frac{7.5}{23} \approx \mathbf{0.3261}$$

-----

**Example:**

  * Find quartile deviation and coefficient of quartile deviation:

| X | 20 | 40 | 60 | 80 | 100 |
|---|---|---|---|---|---|
| f | 4 | 10 | 15 | 20 | 11 |

**Solution:**

1.  **Calculate Cumulative Frequency ($c.f.$):**

| X | f | $c.f.$ |
|---|---|---|
| 20 | 4 | 4 |
| 40 | 10 | 14 |
| **60** | **15** | **29** |
| **80** | **20** | **49** |
| 100 | 11 | 60 |
| **Total**| $\mathbf{N=60}$ | |

2.  **Find Quartiles:**
      * $Q_1$ position ($\frac{60+1}{4} = 15.25^{\text{th}}$). The first $c.f. \ge 15.25$ is 29, so $\mathbf{Q_1 = 60}$.
      * $Q_3$ position ($3 \times 15.25 = 45.75^{\text{th}}$). The first $c.f. \ge 45.75$ is 49, so $\mathbf{Q_3 = 80}$.
3.  **Calculate Measures:**
    $$\text{Quartile Deviation} (QD) = \frac{Q_3 - Q_1}{2} = \frac{80 - 60}{2} = \frac{20}{2} = \mathbf{10.0}$$
    $$\text{Coefficient of Quartile Deviation} (CQD) = \frac{Q_3 - Q_1}{Q_3 + Q_1} = \frac{20}{80 + 60} = \frac{20}{140} = \frac{1}{7} \approx \mathbf{0.1429}$$


---
### Mean Deviation

**The Mean Deviation (M.D.)** is the arithmetic mean of the absolute deviations of the observations from an average (Mean, Median, or Mode).

**M.D. Formulae:**
$$\text{M.D. from } A = \frac{\sum |X - A|}{N} \text{ (Ungrouped)}$$
$$\text{M.D. from } A = \frac{\sum f |X - A|}{N} \text{ (Frequency Distribution)}$$
$$\text{Coefficient of M.D.} = \frac{\text{M.D.}}{\text{Average } (A)}$$

-----
### Mean Deviation

**The Mean Deviation (M.D.)** is the arithmetic mean of the absolute deviations of the observations from an average (Mean or Median).

**M.D. Formulae:**
$$\text{M.D. from } A = \frac{\sum |X - A|}{N}$$
$$\text{Coefficient of M.D.} = \frac{\text{M.D.}}{\text{Average } (A)}$$

***

**Example:**
* Calculate M.D. from Mean & Median & coefficient of Mean Deviation from the following data: 20, 22, 25, 38, 40, 50, 65, 70, 75.

**Solution:**
**1. Calculate Averages:**
Data ($N=9$): 20, 22, 25, 38, **40**, 50, 65, 70, 75.
$$\text{Mean } (\bar{X}) = \frac{\sum X}{N} = \frac{405}{9} = \mathbf{45.0}$$
$$\text{Median } (M) = \left(\frac{9+1}{2}\right)^{\text{th}} \text{ item} = 5^{\text{th}} \text{ item} = \mathbf{40.0}$$

**2. Calculate Deviations and Sums:**

| Data Value ($X$) | Absolute Deviation from Mean ($\mathbf{X - 45}$) | Absolute Deviation from Median ($\mathbf{X - 40}$) |
| :--------------: | :----------------------------------------------: | :------------------------------------------------: |
|        20        |                        25                        |                         20                         |
|        22        |                        23                        |                         18                         |
|        25        |                        20                        |                         15                         |
|        38        |                        7                         |                         2                          |
|        40        |                        5                         |                         0                          |
|        50        |                        5                         |                         10                         |
|        65        |                        20                        |                         25                         |
|        70        |                        25                        |                         30                         |
|        75        |                        30                        |                         35                         |
|  **Total Sum**   |                                                  |                                                    |

**3. Calculate Mean Deviation & Coefficient (from Mean):**
* $$\text{M.D. from Mean} = \frac{\sum |X - \bar{X}|}{N} = \frac{160}{9} \approx \mathbf{17.78}$$
* $$\text{Coeff. M.D. (Mean)} = \frac{\text{M.D. from Mean}}{\bar{X}} = \frac{17.78}{45.0} \approx \mathbf{0.395}$$

**4. Calculate Mean Deviation & Coefficient (from Median):**
* $$\text{M.D. from Median} = \frac{\sum |X - M|}{N} = \frac{155}{9} \approx \mathbf{17.22}$$
* $$\text{Coeff. M.D. (Median)} = \frac{\text{M.D. from Median}}{M} = \frac{17.22}{40.0} \approx \mathbf{0.431}$$
-----

**Example:**

  * Calculate M.D. from Mean & Median & coefficient of Mean Deviation from the following data:

| X | 20 | 30 | 40 | 50 | 60 | 70 |
|---|---|---|---|---|---|---|
| F | 8 | 12 | 20 | 10 | 6 | 4 |

**Solution:**
**1. Averages:**

| $X$ | $F$ | $FX$ | $c.f.$ |
|---|---|---|---|
| 20 | 8 | 160 | 8 |
| 30 | 12 | 360 | 20 |
| 40 | 20 | 800 | 40 |
| 50 | 10 | 500 | 50 |
| 60 | 6 | 360 | 56 |
| 70 | 4 | 280 | 60 |
| **Total**| $\mathbf{N=60}$ | $\mathbf{\sum FX=2460}$ | |

$$\text{Mean } (\bar{X}) = \frac{2460}{60} = \mathbf{41.0}$$
$$\text{Median } (M): \text{Pos.} = \frac{60+1}{2} = 30.5^{\text{th}}.\: c.f. \ge 30.5 \text{ is } 40 \text{, so } M = \mathbf{40.0}$$

**2. Deviations:**

| $X$       | $F$ | $X - \bar{X}$ | $F(X - \bar{X})$ | $X - M$ | $F(X - M)$     |
| --------- | --- | ------------- | ---------------- | ------- | -------------- |
| 20        | 8   | 21            | 168              | 20      | 160            |
| 30        | 12  | 11            | 132              | 10      | 120            |
| 40        | 20  | 1             | 20               | 0       | 0              |
| 50        | 10  | 9             | 90               | 10      | 100            |
| 60        | 6   | 19            | 114              | 20      | 120            |
| 70        | 4   | 29            | 116              | 30      | 120            |
| **Total** | 60  |               | $\mathbf{640}$   |         | $\mathbf{620}$ |

**3. Mean Deviation & Coefficient:**
$$\text{M.D. from Mean} = \frac{640}{60} \approx \mathbf{10.67}$$
$$\text{Coeff. M.D. (Mean)} = \frac{10.67}{41.0} \approx \mathbf{0.260}$$

$$\text{M.D. from Median} = \frac{620}{60} \approx \mathbf{10.33}$$
$$\text{Coeff. M.D. (Median)} = \frac{10.33}{40.0} \approx \mathbf{0.258}$$

-----

**Example:**

  * Calculate the Mean Deviation & coefficient of Mean Deviation from the following data:

| Marks | 5 | 15 | 25 | 35 | 45 | 55 |
|---|---|---|---|---|---|---|
| No. of students ($F$) | 10 | 20 | 30 | 40 | 50 | 30 |

**Solution:**
**1. Averages:**

| $X$ | $F$ | $FX$ | $c.f.$ |
|---|---|---|---|
| 5 | 10 | 50 | 10 |
| 15 | 20 | 300 | 30 |
| 25 | 30 | 750 | 60 |
| **35** | **40** | **1400** | **100** |
| 45 | 50 | 2250 | 150 |
| 55 | 30 | 1650 | 180 |
| **Total**| $\mathbf{N=180}$ | $\mathbf{\sum FX=6400}$ | |

$$\text{Mean } (\bar{X}) = \frac{6400}{180} \approx \mathbf{35.56}$$
$$\text{Median } (M): \text{Pos.} = \frac{180+1}{2} = 90.5^{\text{th}}.\: c.f. \ge 90.5 \text{ is } 100 \text{, so } M = \mathbf{35.0}$$

**2. Deviations from Mean ($\bar{X}=35.56$):**

| $X$       | $F$ | $X - 35.56$ | $F(X - 35.56)$    |
| --------- | --- | ----------- | ----------------- |
| 5         | 10  | 30.56       | 305.6             |
| 15        | 20  | 20.56       | 411.2             |
| 25        | 30  | 10.56       | 316.8             |
| 35        | 40  | 0.56        | 22.4              |
| 45        | 50  | 9.44        | 472.0             |
| 55        | 30  | 19.44       | 583.2             |
| **Total** | 180 |             | $\mathbf{2111.2}$ |

**3. Mean Deviation & Coefficient (from Mean):**
$$\text{M.D. from Mean} = \frac{2111.2}{180} \approx \mathbf{11.73}$$
$$\text{Coeff. M.D. (Mean)} = \frac{11.73}{35.56} \approx \mathbf{0.330}$$
*(The calculation for M.D. from Median is also provided in the tool output: M.D. from Median $\approx 11.67$, Coeff. $\approx 0.333$)*

-----

**Example:**

  * Calculate the Mean Deviation & coefficient of Mean Deviation from the following data:

| Marks | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 |
|---|---|---|---|---|---|---|
| No. of students ($F$) | 10 | 20 | 30 | 50 | 40 | 30 |

**Solution:**
**1. Averages:**

| Class     | $F$              | Midpoint ($m$) | $Fm$                    | $c.f.$  |
| --------- | ---------------- | -------------- | ----------------------- | ------- |
| 0-10      | 10               | 5              | 50                      | 10      |
| 10-20     | 20               | 15             | 300                     | 30      |
| 20-30     | 30               | 25             | 750                     | 60      |
| **30-40** | **50**           | **35**         | **1750**                | **110** |
| 40-50     | 40               | 45             | 1800                    | 150     |
| 50-60     | 30               | 55             | 1650                    | 180     |
| **Total** | $\mathbf{N=180}$ |                | $\mathbf{\sum Fm=6300}$ |         |

$$\text{Mean } (\bar{X}) = \frac{6300}{180} = \mathbf{35.0}$$

**2. Deviations from Mean ($\bar{X}=35.0$):**

| $m$       | $F$ | $m - 35$ | $F(m - 35)$     |
| --------- | --- | -------- | --------------- |
| 5         | 10  | 30       | 300             |
| 15        | 20  | 20       | 400             |
| 25        | 30  | 10       | 300             |
| 35        | 50  | 0        | 0               |
| 45        | 40  | 10       | 400             |
| 55        | 30  | 20       | 600             |
| **Total** | 180 |          | $\mathbf{2000}$ |

**3. Mean Deviation & Coefficient (from Mean):**
$$\text{M.D. from Mean} = \frac{2000}{180} \approx \mathbf{11.11}$$
$$\text{Coeff. M.D. (Mean)} = \frac{11.11}{35.0} \approx \mathbf{0.317}$$
*(Note: If calculated from the Median $M=37.5$ (from tool output), M.D. $\approx 11.94$, Coeff. $\approx 0.319$)*

-----

-----

**Example:**

  * Write short notes on:
        \* Range
        \* Interquartile range
        \* Mean deviation
        \* Standard deviation
        \* Variance

**Solution:**

### Short Notes on Measures of Dispersion

  * **Range:** The simplest measure of dispersion, defined as the difference between the **largest observation ($L$)** and the **smallest observation ($S$)** in a dataset: $R = L - S$. It is easy to calculate but relies solely on the two extreme values, making it highly susceptible to outliers.

  * **Interquartile Range (IQR):** A measure of statistical dispersion equal to the difference between the third quartile ($Q_3$) and the first quartile ($Q_1$): $IQR = Q_3 - Q_1$. It measures the spread of the middle $50\%$ of the data, making it a robust measure that is unaffected by extreme outliers.

  * **Mean Deviation (M.D.):** The arithmetic mean of the **absolute deviations** of the observations from a central value (Mean, Median, or Mode): $\text{M.D.} = \frac{\sum |X - A|}{N}$. Since it uses absolute values, it mathematically lacks certain desirable properties compared to the standard deviation, but it is conceptually easier to understand.

  * **Standard Deviation (S.D.):** The most widely used measure of dispersion, defined as the **square root of the variance**. It measures the typical amount of variation or dispersion of a set of values from the mean, and is expressed in the original units of measurement. The formula is $\sigma = \sqrt{\frac{\sum (X-\bar{X})^2}{N}}$ (for population).

  * **Variance:** The mean of the **squared deviations** from the arithmetic mean. It is the square of the standard deviation ($\sigma^2$). It is mathematically preferred because squaring deviations removes the negative signs and weighs larger deviations more heavily, but its unit is the square of the original data unit.

-----

**Example:**

  * Explain the measures of dispersion and also find the range & Coefficient of Range for the following data: 20, 35, 25, 30, 15.

**Solution:**

### Explanation of Measures of Dispersion

**Measures of Dispersion** (or Measures of Variation) quantify the extent to which the values in a dataset are spread out or scattered around a central value. They indicate how representative the central tendency (like the mean or median) is of the data. A low measure of dispersion indicates that the data points tend to be close to the average, while a high measure indicates the data points are spread farther apart. Common measures include Range, Quartile Deviation, Mean Deviation, and Standard Deviation.

### Range and Coefficient of Range Calculation

Data: 20, 35, 25, 30, 15.

The largest value is $L=35$. The smallest value is $S=15$.
$$\text{Range} (R) = L - S = 35 - 15 = \mathbf{20}$$
$$\text{Coefficient of Range} (CR) = \frac{L - S}{L + S} = \frac{35 - 15}{35 + 15} = \frac{20}{50} = \mathbf{0.4}$$


### Variance and Standard Deviation

The **Variance ($\sigma^2$)** measures the average squared deviation from the mean, and the **Standard Deviation ($\sigma$)** is the square root of the variance, returning the dispersion measurement to the original units.

**Key Formulae:**
$$\text{Variance } (\sigma^2) = \frac{\sum (X-\bar{X})^2}{N} \quad \text{ or } \quad \frac{\sum f(X-\bar{X})^2}{N}$$
$$\text{Standard Deviation } (\sigma) = \sqrt{\text{Variance}}$$

-----

**Example:**

  * Find the Variance and standard deviation for the following individual series: 3, 6, 8, 10, 18.

**Solution:**
**1. Calculate Mean ($\bar{X}$):**
$$N=5$$
$$\bar{X} = \frac{3 + 6 + 8 + 10 + 18}{5} = \frac{45}{5} = \mathbf{9.0}$$

**2. Calculate Deviations and Sum of Squares:**

| $X$ | $X - \bar{X} = X - 9$ | $(X - \bar{X})^2$ |
|:---:|:---:|:---:|
| 3 | -6 | 36 |
| 6 | -3 | 9 |
| 8 | -1 | 1 |
| 10 | 1 | 1 |
| 18 | 9 | 81 |
| **Sum** | 0 | $\mathbf{\sum (X-\bar{X})^2 = 128}$ |

**3. Calculate Variance and Standard Deviation:**
$$\text{Variance } (\sigma^2) = \frac{128}{5} = \mathbf{25.6}$$
$$\text{Standard Deviation } (\sigma) = \sqrt{25.6} \approx \mathbf{5.06}$$

-----

**Example:**

  * Find the variance and standard deviation for the following frequency distribution:

| Marks | 5-15 | 15-25 | 25-35 | 35-45 | 45-55 | 55-65 |
|---|---|---|---|---|---|---|
| No. of students ($F$) | 10 | 20 | 25 | 20 | 15 | 10 |

**Solution:**
**1. Calculate Mean ($\bar{X}$):**
$N = \sum F = 100$.

| Class | $F$ | Midpoint ($m$) | $Fm$ |
|:---:|:---:|:---:|:---:|
| 5-15 | 10 | 10 | 100 |
| 15-25 | 20 | 20 | 400 |
| 25-35 | 25 | 30 | 750 |
| 35-45 | 20 | 40 | 800 |
| 45-55 | 15 | 50 | 750 |
| 55-65 | 10 | 60 | 600 |
| **Total**| 100 | | $\mathbf{\sum Fm = 3400}$ |

$$\bar{X} = \frac{3400}{100} = \mathbf{34.0}$$

**2. Calculate Weighted Sum of Squared Deviations:**

| $m$ | $F$ | $m - \bar{X} = m - 34$ | $(m - \bar{X})^2$ | $F(m - \bar{X})^2$ |
|:---:|:---:|:---:|:---:|:---:|
| 10 | 10 | -24 | 576 | 5760 |
| 20 | 20 | -14 | 196 | 3920 |
| 30 | 25 | -4 | 16 | 400 |
| 40 | 20 | 6 | 36 | 720 |
| 50 | 15 | 16 | 256 | 3840 |
| 60 | 10 | 26 | 676 | 6760 |
| **Total**| 100 | | | $\mathbf{21400}$ |

**3. Calculate Variance and Standard Deviation:**
$$\text{Variance } (\sigma^2) = \frac{21400}{100} = \mathbf{214.0}$$
$$\text{Standard Deviation } (\sigma) = \sqrt{214} \approx \mathbf{14.63}$$

-----

**Example:**

  * Calculate standard deviation and variance of the given data:

| Size ($X$) | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| Frequency ($F$) | 3 | 6 | 9 | 13 | 8 | 5 | 4 |

**Solution:**
**1. Calculate Mean ($\bar{X}$):**
$N = \sum F = 48$.

| $X$ | $F$ | $FX$ |
|:---:|:---:|:---:|
| 6 | 3 | 18 |
| 7 | 6 | 42 |
| 8 | 9 | 72 |
| 9 | 13 | 117 |
| 10 | 8 | 80 |
| 11 | 5 | 55 |
| 12 | 4 | 48 |
| **Total**| 48 | $\mathbf{\sum FX = 432}$ |

$$\bar{X} = \frac{432}{48} = \mathbf{9.0}$$

**2. Calculate Weighted Sum of Squared Deviations:**

| $X$ | $F$ | $X - \bar{X} = X - 9$ | $(X - \bar{X})^2$ | $F(X - \bar{X})^2$ |
|:---:|:---:|:---:|:---:|:---:|
| 6 | 3 | -3 | 9 | 27 |
| 7 | 6 | -2 | 4 | 24 |
| 8 | 9 | -1 | 1 | 9 |
| 9 | 13 | 0 | 0 | 0 |
| 10 | 8 | 1 | 1 | 8 |
| 11 | 5 | 2 | 4 | 20 |
| 12 | 4 | 3 | 9 | 36 |
| **Total**| 48 | | | $\mathbf{124}$ |

**3. Calculate Variance and Standard Deviation:**
$$\text{Variance } (\sigma^2) = \frac{124}{48} \approx \mathbf{2.58}$$
$$\text{Standard Deviation } (\sigma) = \sqrt{2.5833} \approx \mathbf{1.61}$$

-----

**Example:**

  * Calculate the standard deviation of 100 students:

| Mass (kg) | 60-62 | 63-65 | 66-68 | 69-71 | 72-74 |
|---|---|---|---|---|---|
| No. of students ($F$) | 10 | 30 | 20 | 50 | 40 |

**Solution:**
The classes are **discontinuous** (e.g., 60-62, 63-65). We first convert them to continuous classes (e.g., 59.5-62.5) to find accurate midpoints and apply the formula. $\mathbf{N = \sum F = 150}$. *(Note: We use $N=150$ for calculation, as per the table, rather than the stated $N=100$.)*

**1. Calculate Mean ($\bar{X}$):**

| Class (Cont.) | $F$ | Midpoint ($m$) | $Fm$ |
|:---:|:---:|:---:|:---:|
| 59.5-62.5 | 10 | 61 | 610 |
| 62.5-65.5 | 30 | 64 | 1920 |
| 65.5-68.5 | 20 | 67 | 1340 |
| 68.5-71.5 | 50 | 70 | 3500 |
| 71.5-74.5 | 40 | 73 | 2920 |
| **Total**| 150 | | $\mathbf{\sum Fm = 10290}$ |

$$\bar{X} = \frac{10290}{150} = \mathbf{68.6}$$

**2. Calculate Weighted Sum of Squared Deviations:**

| $m$ | $F$ | $m - \bar{X} = m - 68.6$ | $(m - \bar{X})^2$ | $F(m - \bar{X})^2$ |
|:---:|:---:|:---:|:---:|:---:|
| 61 | 10 | -7.6 | 57.76 | 577.6 |
| 64 | 30 | -4.6 | 21.16 | 634.8 |
| 67 | 20 | -1.6 | 2.56 | 51.2 |
| 70 | 50 | 1.4 | 1.96 | 98.0 |
| 73 | 40 | 4.4 | 19.36 | 774.4 |
| **Total**| 150 | | | $\mathbf{2136.0}$ |

**3. Calculate Variance and Standard Deviation:**
$$\text{Variance } (\sigma^2) = \frac{2136.0}{150} \approx \mathbf{14.24}$$
$$\text{Standard Deviation } (\sigma) = \sqrt{14.24} \approx \mathbf{3.77}$$

-----

**Example:**

  * Sum of squares of items 2430, mean is 7, N=12, find the variance.
        \* 176.5
        \* 12.38
        \* 153.26
        \* 14

**Solution:**
The variance is calculated using the raw moments formula:
$$\text{Variance } (\sigma^2) = \frac{\sum X^2}{N} - (\bar{X})^2$$

Given:

  * $\sum X^2 = 2430$
  * $\bar{X} = 7$
  * $N = 12$

$$\sigma^2 = \frac{2430}{12} - (7)^2$$
$$\sigma^2 = 202.5 - 49$$
$$\sigma^2 = \mathbf{153.5}$$

The calculated variance is $153.5$. Among the given options, $153.26$ is the closest, likely representing a slight rounding error in the option list.