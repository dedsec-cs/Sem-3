Here's the updated cheat sheet with Median and Mode included\!

-----

# Statistics Cheat Sheet: Statistical Techniques I

## 1\. Measures of Central Tendency

### Arithmetic Mean ($\bar{X}$)

  * **Summary:** The simple average. Sum of all values divided by the number of values.
  * **Individual Series (Ungrouped)**
      * **Direct:** $\bar{X} = \frac{\sum X}{N}$
      * **Shortcut:** $\bar{X} = A + \frac{\sum d}{N}$ (where $A$ = Assumed Mean, $d = X - A$)
  * **Discrete/Continuous Series (Grouped)**
      * **Note:** For Continuous, $X$ becomes the Mid-point ($m$).
      * **Direct:** $\bar{X} = \frac{\sum fX}{N}$ (where $N = \sum f$)
      * **Shortcut:** $\bar{X} = A + \frac{\sum fd}{N}$ (where $d = X - A$)
      * **Step Deviation:** $\bar{X} = A + \left( \frac{\sum fd'}{N} \right) \times i$ (where $d' = \frac{d}{i}$ and $i$ = common factor/class width)

### Median (M)

  * **Summary:** The middle value that divides an *ordered* dataset into two equal halves.
  * **Individual Series:** Value of the $\left(\frac{N+1}{2}\right)^{th}$ item.
  * **Discrete Series:** Find cumulative frequency ($cf$), then find the value corresponding to the $\left(\frac{N+1}{2}\right)^{th}$ item.
  * **Continuous Series:**
      * First find Median Class using $\frac{N}{2}$.
      * **Formula:** $M = L_1 + \left( \frac{\frac{N}{2} - cf}{f} \right) \times i$
          * $L_1$: Lower limit of the median class.
          * $cf$: Cumulative frequency of the class *before* the median class.
          * $f$: Frequency of the median class.
          * $i$: Class width.

### Mode (Z)

  * **Summary:** The most frequently occurring value in the dataset.
  * **Individual/Discrete Series:** The value ($X$) with the highest frequency ($f$).
  * **Continuous Series:**
      * First find Modal Class (class with highest $f$).
      * **Formula:** $Z = L_1 + \left( \frac{f_1 - f_0}{2f_1 - f_0 - f_2} \right) \times i$
          * $L_1$: Lower limit of the modal class.
          * $f_1$: Frequency of the modal class.
          * $f_0$: Frequency of the class *before* the modal class.
          * $f_2$: Frequency of the class *after* the modal class.
          * $i$: Class width.
  * **Empirical Relation (for moderate skew):** Mode $\approx$ 3(Median) - 2(Mean)

### Properties of Mean

  * **Sum of Deviations:** The sum of deviations from the true mean is always zero.
      * $\sum (X - \bar{X}) = 0$
  * **Combined Mean:** The overall mean of two or more groups.
      * $\bar{X}_{12} = \frac{(N_1 \bar{X}_1) + (N_2 \bar{X}_2)}{N_1 + N_2}$

### Weighted Mean ($\bar{X}_w$)

  * **Summary:** An average where values ($X$) are given different "importance" or weights ($W$).
  * **Formula:** $\bar{X}_w = \frac{\sum WX}{\sum W}$

### Geometric Mean (GM)

  * **Summary:** Used to average rates of change or growth (e.g., investment returns).
  * **Formula:** $GM = \sqrt[N]{X_1 \times X_2 \times \dots \times X_N}$

### Harmonic Mean (HM)

  * **Summary:** Used to average rates like speed (km/h) over a fixed distance.
  * **Formula:** $HM = \frac{N}{\sum \left( \frac{1}{X} \right)}$

-----

## 2\. Moments

### Moments about Origin (Raw Moments, $\mu_r'$)

  * **Summary:** Moments calculated around the value '0'.
  * **Formula:** $\mu_r' = \frac{\sum X^r}{N}$ or $\frac{\sum fX^r}{N}$
  * **Key:** $\mu_1' = \bar{X}$ (The Arithmetic Mean)

### Moments about Mean (Central Moments, $\mu_r$)

  * **Summary:** Moments calculated around the mean ($\bar{X}$). Used to describe the shape of the distribution.
  * **Formula:** $\mu_r = \frac{\sum (X - \bar{X})^r}{N}$ or $\frac{\sum f(X - \bar{X})^r}{N}$
  * **Key:**
      * $\mu_1 = 0$ (Always)
      * $\mu_2 = \sigma^2$ (The Variance)
      * $\mu_3$ (Measures Skewness)
      * $\mu_4$ (Measures Kurtosis)

### Relation Between Moments

  * **Summary:** How to find central moments ($\mu_r$) if you have raw moments ($\mu_r'$).
  * **Formulas:**
      * $\mu_2 = \mu_2' - (\mu_1')^2$
      * $\mu_3 = \mu_3' - 3(\mu_2')(\mu_1') + 2(\mu_1')^3$
      * $\mu_4 = \mu_4' - 4(\mu_3')(\mu_1') + 6(\mu_2')(\mu_1')^2 - 3(\mu_1')^4$
  * **Note:** The same formulas work for provisional moments (moments about $A$), just replace $\mu_r'$ with $\mu_r'(A)$.

-----

## 3\. Skewness (Asymmetry)

### Distribution Shapes

  * **Symmetrical:** No skew.

[Image of a symmetrical distribution curve]

```
* **Mean = Median = Mode**
```

  * **Positively Skewed:** Long tail to the right.

[Image of a positively skewed distribution curve]

```
* **Mean > Median > Mode**
```

  * **Negatively Skewed:** Long tail to the left.
      * **Mean \< Median \< Mode**

### Karl Pearson's Coefficient ($Sk_p$)

  * **Summary:** Measures skew using the mean, mode/median, and standard deviation.
  * **Formulas:**
      * $\text{Sk}_p = \frac{\text{Mean} - \text{Mode}}{\text{Standard Deviation}} = \frac{\bar{X} - Z}{\sigma}$
      * $\text{Sk}_p = \frac{3 (\text{Mean} - \text{Median})}{\text{Standard Deviation}} = \frac{3 (\bar{X} - M)}{\sigma}$
  * **Interpretation:**
      * $Sk_p = 0$: Symmetrical
      * $Sk_p > 0$: Positively Skewed
      * $Sk_p < 0$: Negatively Skewed

### Moment Coefficient of Skewness ($\gamma_1$)

  * **Summary:** Measures skew using the 2nd and 3rd central moments.
  * **Formulas:**
      * $\beta_1 = \frac{\mu_3^2}{\mu_2^3}$
      * $\gamma_1 = \sqrt{\beta_1} = \frac{\mu_3}{\mu_2^{3/2}}$ (or $\frac{\mu_3}{\sigma^3}$)
  * **Interpretation:**
      * $\gamma_1 = 0$: Symmetrical
      * $\gamma_1 > 0$: Positively Skewed
      * $\gamma_1 < 0$: Negatively Skewed

-----

## 4\. Kurtosis (Peakedness)

  * **Summary:** Measures the peakedness and tail weight of a distribution.
  * **Types:**
      * **Leptokurtic:** Sharp peak, heavy tails (more outliers).
      * **Mesokurtic:** Normal curve, the benchmark.
      * **Platykurtic:** Flat peak, light tails (fewer outliers).
  * **Measure ($\beta_2$)**
      * **Formula:** $\beta_2 = \frac{\mu_4}{\mu_2^2}$
      * **Interpretation:**
          * $\beta_2 > 3$: Leptokurtic
          * $\beta_2 = 3$: Mesokurtic
          * $\beta_2 < 3$: Platykurtic
  * **Excess Kurtosis ($\gamma_2$)**
      * **Formula:** $\gamma_2 = \beta_2 - 3$
      * **Interpretation:** ($\gamma_2 > 0$ is Lepto, $\gamma_2 = 0$ is Meso, $\gamma_2 < 0$ is Platy)