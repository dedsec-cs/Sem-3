Here are the step-by-step solutions for questions 1 to 7 from the provided practice sheet.

### 1. A die is tossed twice. A 'success' is getting an odd number on a random basis. Find the mean and variance of the number of successes.

Solution:

This is a problem involving the Binomial Distribution where $n$ is the number of trials and $p$ is the probability of success.

- **Number of trials ($n$):** 2 (since the die is tossed twice).
    
- Probability of success ($p$): A success is getting an odd number $\{1, 3, 5\}$.
    
    $$p = \frac{3}{6} = 0.5$$
    
- Probability of failure ($q$):
    
    $$q = 1 - p = 0.5$$
    

Mean ($E[X]$):

For a binomial distribution, Mean $= np$.

$$\text{Mean} = 2 \times 0.5 = 1$$

Variance ($Var(X)$):

For a binomial distribution, Variance $= npq$.

$$\text{Variance} = 2 \times 0.5 \times 0.5 = 0.5$$

**Answer:** Mean = 1, Variance = 0.5.

---

### **2. A pair of dice is thrown together. Find the expected value of the sum of the numbers of points drawn.**

Solution:

Let $X$ be the sum of the points on the two dice.

The expected value of the sum of random variables is the sum of their individual expected values: $E(X + Y) = E(X) + E(Y)$.

1. Expected value of a single die:
    
    Outcomes are $\{1, 2, 3, 4, 5, 6\}$, each with probability $1/6$.
    
    $$E(\text{Die}) = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5$$
    
2. Expected value of the sum:
    
    $$E(\text{Sum}) = E(\text{Die 1}) + E(\text{Die 2})$$
    
    $$E(\text{Sum}) = 3.5 + 3.5 = 7$$
    

**Answer:** The expected value is 7.

---

### **3. Let X be a continuous random variable with PDF:**

$$f(x) = \begin{cases} 2x, & 0 < x < 1 \\ 0, & \text{otherwise} \end{cases}$$

Find the expected value of X and also calculate variance, standard deviation.

**Solution:**

1. Expected Value ($E[X]$):

$$E[X] = \int_{-\infty}^{\infty} x f(x) dx = \int_{0}^{1} x(2x) dx = \int_{0}^{1} 2x^2 dx$$

$$= \left[ \frac{2x^3}{3} \right]_0^1 = \frac{2(1)^3}{3} - 0 = \frac{2}{3}$$

2. Variance ($Var(X)$):

First, find $E[X^2]$:

$$E[X^2] = \int_{0}^{1} x^2(2x) dx = \int_{0}^{1} 2x^3 dx$$

$$= \left[ \frac{2x^4}{4} \right]_0^1 = \left[ \frac{x^4}{2} \right]_0^1 = \frac{1}{2}$$

Now, use the variance formula: $Var(X) = E[X^2] - (E[X])^2$

$$Var(X) = \frac{1}{2} - \left(\frac{2}{3}\right)^2 = \frac{1}{2} - \frac{4}{9}$$

Taking common denominator (18):

$$Var(X) = \frac{9}{18} - \frac{8}{18} = \frac{1}{18}$$

3. Standard Deviation ($\sigma$):

$$\sigma = \sqrt{Var(X)} = \sqrt{\frac{1}{18}} = \frac{1}{3\sqrt{2}} \approx 0.2357$$

**Answer:** Mean = $2/3$, Variance = $1/18$, SD $\approx 0.236$.

---

### **4. Let x is random variable with p.m.f given below**

|**X**|**3**|**6**|**9**|
|---|---|---|---|
|**P(X)**|**1/6**|**1/2**|**1/3**|

**Calculate the value of $E(2x + 1)^2$**

Solution:

We need to find the expected value of the function $g(X) = (2X + 1)^2$.

Formula: $E[g(X)] = \sum g(x) P(x)$.

**Step 1: Calculate $(2x+1)^2$ for each x:**

- If $x = 3$: $(2(3)+1)^2 = 7^2 = 49$
    
- If $x = 6$: $(2(6)+1)^2 = 13^2 = 169$
    
- If $x = 9$: $(2(9)+1)^2 = 19^2 = 361$
    

Step 2: Multiply by probabilities and sum:

$$E = 49\left(\frac{1}{6}\right) + 169\left(\frac{1}{2}\right) + 361\left(\frac{1}{3}\right)$$

To add these, find a common denominator (6):

$$= \frac{49}{6} + \frac{169 \times 3}{6} + \frac{361 \times 2}{6}$$

$$= \frac{49 + 507 + 722}{6}$$

$$= \frac{1278}{6} = 213$$

**Answer:** $E(2x + 1)^2 = 213$.

---

### **5. The probability that a bomb dropped from a plane will strike the target is 1/5. If 6 bombs are dropped, find the probability that:**

a) Exactly two will strike the target

b) At least two will strike the target

Solution:

This is a Binomial distribution problem ($n=6, p=1/5=0.2, q=0.8$).

Formula: $P(X=x) = \binom{n}{x} p^x q^{n-x}$

a) Exactly two ($x=2$):

$$P(X=2) = \binom{6}{2} (0.2)^2 (0.8)^4$$

$$= 15 \times 0.04 \times 0.4096$$

$$= 0.6 \times 0.4096 = 0.24576$$

b) At least two ($x \ge 2$):

Using the complement rule: $P(X \ge 2) = 1 - [P(0) + P(1)]$

- $P(0) = \binom{6}{0} (0.2)^0 (0.8)^6 = 1 \times 1 \times 0.262144 = 0.262144$
    
- $P(1) = \binom{6}{1} (0.2)^1 (0.8)^5 = 6 \times 0.2 \times 0.32768 = 0.393216$
    

$$P(X \ge 2) = 1 - (0.262144 + 0.393216)$$

$$P(X \ge 2) = 1 - 0.65536 = 0.34464$$

**Answer:** a) $0.24576$, b) $0.34464$.

---

### **6. The lengths of pine needles are Normally distributed. 11.51% are shorter than 6.2 cm and 3.59% are longer than 9.5 cm. Find the mean and standard deviation.**

Solution:

Let $\mu$ be the mean and $\sigma$ be the standard deviation. We use the standard normal variable $Z = \frac{X - \mu}{\sigma}$.

1. First Condition ($X < 6.2$):

$P(X < 6.2) = 0.1151$.

Since the probability is less than 0.5, the Z-score is negative. The area to the left is 0.1151.

Looking at the Z-table, the area corresponding to $0.5 - 0.1151 = 0.3849$ (from mean to Z) corresponds to $Z = 1.2$.

Since it's on the left:

$$Z_1 = -1.2$$

$$-1.2 = \frac{6.2 - \mu}{\sigma} \implies \mu - 1.2\sigma = 6.2 \quad \dots(1)$$

2. Second Condition ($X > 9.5$):

$P(X > 9.5) = 0.0359$.

This means the area to the left is $1 - 0.0359 = 0.9641$.

Looking at the Z-table, the area corresponding to $0.9641 - 0.5 = 0.4641$ (from mean to Z) corresponds to $Z = 1.8$.

$$Z_2 = 1.8$$

$$1.8 = \frac{9.5 - \mu}{\sigma} \implies \mu + 1.8\sigma = 9.5 \quad \dots(2)$$

3. Solve Simultaneous Equations:

Subtract equation (1) from (2):

$$(\mu + 1.8\sigma) - (\mu - 1.2\sigma) = 9.5 - 6.2$$

$$3.0\sigma = 3.3$$

$$\sigma = 1.1 \text{ cm}$$

Substitute $\sigma$ back into (1):

$$\mu - 1.2(1.1) = 6.2$$

$$\mu - 1.32 = 6.2$$

$$\mu = 7.52 \text{ cm}$$

**Answer:** Mean = 7.52 cm, Standard Deviation = 1.1 cm.

---

### **7. During rush hour commuters arrive at a steady rate of 7 commuters every 30 seconds.**

Solution:

This follows a Poisson Distribution.

**a) Probability that in a random 30 second interval there will be more than 5 but no more than 11 commuters.**

- $\lambda = 7$ (per 30 sec).
    
- We need $P(5 < X \le 11)$, which is $P(X=6) + \dots + P(X=11)$.
    
    Formula: $P(x) = \frac{e^{-7} 7^x}{x!}$
    
    Using cumulative Poisson tables or calculation:
    
    $P(X \le 11) - P(X \le 5) \approx 0.9467 - 0.3007 = 0.6460$.
    

**b) Show that the probability that more than 81 commuters will arrive in a 5-minute interval is approx 0.085.**

- New Rate for 5 minutes: $\lambda = 7 \times (\frac{5 \text{ min}}{30 \text{ sec}}) = 7 \times 10 = 70$.
    
- Since $\lambda = 70$ is large, use Normal Approximation to Poisson.
    
    Mean $\mu = 70$, Variance $\sigma^2 = 70$, SD $\sigma = \sqrt{70} \approx 8.367$.
    
- We need $P(X > 81)$. Using continuity correction, we look for $X > 81.5$.
    
    $$Z = \frac{81.5 - 70}{8.367} = \frac{11.5}{8.367} \approx 1.374$$
    
- Using Z-table, $P(Z > 1.374) = 1 - P(Z < 1.374) = 1 - 0.9153 = 0.0847$.
    
    This is approximately 0.085.
    

**c) Determine the probability that more than 81 commuters will arrive in 2 of these intervals of 5 minutes.**

- We treat this as a Binomial problem.
    
- Trial: A 5-minute interval.
    
- Total trials ($n$) = 4 (Since 20 mins is divided into 4 intervals).
    
- Probability of success ($p$) = 0.085 (from part b).
    
- We want exactly 2 successes ($x=2$).
    

$$P(X=2) = \binom{4}{2} (0.085)^2 (1 - 0.085)^{4-2}$$

$$= 6 \times (0.085)^2 \times (0.915)^2$$

$$= 6 \times 0.007225 \times 0.837225$$

$$= 0.03629$$---
### **Solution 8**

**a. Battery Life (Normal Distribution)**

Given:

- Mean ($\mu$) = 12 hours
    
- Standard Deviation ($\sigma$) = 3 hours
    
- Sample size ($N$) = 100
    
- $Z = \frac{X - \mu}{\sigma}$
    

I. Probability of life more than 15 hours ($P(X > 15)$)

Calculate the Z-score for $X = 15$:

$$Z = \frac{15 - 12}{3} = \frac{3}{3} = 1$$

We need to find the area to the right of $Z = 1$.

- Given area for $Z=1$ (from mean to Z) is $0.3413$.
    
- $P(Z > 1) = 0.5 - 0.3413 = 0.1587$
    

**Percentage:** $0.1587 \times 100 = \mathbf{15.87\%}$

---

II. Probability of life less than 6 hours ($P(X < 6)$)

Calculate the Z-score for $X = 6$:

$$Z = \frac{6 - 12}{3} = \frac{-6}{3} = -2$$

We need to find the area to the left of $Z = -2$. By symmetry, this is equal to the area to the right of $Z = 2$.

- _Note: The question paper lists "area for z=2 is 0.0028". This appears to be a typo for the standard tail probability $0.0228$ or a misprint of the mean-to-Z area $0.4772$. We will use the standard calculation._
    
- Standard area from mean for $Z=2$ is $0.4772$.
    
- $P(Z < -2) = 0.5 - 0.4772 = 0.0228$
    

**Percentage:** $0.0228 \times 100 = \mathbf{2.28\%}$

---

III. Probability of life between 10 and 14 hours ($P(10 < X < 14)$)

Calculate Z-scores for $X = 10$ and $X = 14$:

$$Z_1 = \frac{10 - 12}{3} = -0.67$$

$$Z_2 = \frac{14 - 12}{3} = 0.67$$

We need the area between $Z = -0.67$ and $Z = 0.67$.

- Given area for $Z=0.67$ (from mean to Z) is $0.2487$.
    
- Total Area = Area(left) + Area(right) = $0.2487 + 0.2487 = 0.4974$
    

**Percentage:** $0.4974 \times 100 = \mathbf{49.74\%}$

---

**b. Brass Plugs (Normal Distribution)**

Given:

- Mean ($\mu$) = 0.7515 cm
    
- Standard Deviation ($\sigma$) = 0.002 cm
    
- Total plugs ($N$) = 1000
    
- Approved limits: $0.752 \pm 0.004$ cm
    
    - Lower Limit (LL) = $0.748$ cm
        
    - Upper Limit (UL) = $0.756$ cm
        

Plugs are **rejected** if they are outside these limits (i.e., $X < 0.748$ or $X > 0.756$).

1. Calculate Z-scores for limits:

$$Z_{lower} = \frac{0.748 - 0.7515}{0.002} = \frac{-0.0035}{0.002} = -1.75$$

$$Z_{upper} = \frac{0.756 - 0.7515}{0.002} = \frac{0.0045}{0.002} = 2.25$$

2. Calculate Probability of Rejection:

We need the sum of the tail areas.

- Lower Tail ($Z < -1.75$):
    
    Given area for $Z=1.75$ is $0.4599$.
    
    $P(Z < -1.75) = 0.5 - 0.4599 = 0.0401$
    
- Upper Tail ($Z > 2.25$):
    
    Given area for $Z=2.25$ is $0.4878$.
    
    $P(Z > 2.25) = 0.5 - 0.4878 = 0.0122$
    
- Total Probability of Rejection:
    
    $P(\text{Reject}) = 0.0401 + 0.0122 = 0.0523$
    

3. Number of Rejected Plugs:

$$1000 \times 0.0523 = 52.3$$

**Answer:** Approximately **52 plugs** are likely to be rejected.

---

### **Solution 9**

**Car Showroom Salesman (Poisson Distribution)**

Given:

- Average rate = 1 call per 15 minutes.
    
- Hourly rate ($\lambda_{hour}$) = 4 calls per hour.
    
- Poisson Formula: $P(X=x) = \frac{e^{-\lambda} \cdot \lambda^x}{x!}$
    

**a) Probability of exactly 6 calls between 9 a.m. and 11 a.m.**

- Time duration ($t$) = 2 hours.
    
- Parameter $\lambda = 4 \times 2 = 8$.
    
- $x = 6$.
    

$$P(X=6) = \frac{e^{-8} \cdot 8^6}{6!}$$

$$P(X=6) = \frac{0.0003355 \cdot 262144}{720}$$

$$P(X=6) \approx \mathbf{0.1221}$$

**b) Probability of exactly 6 calls between 9 a.m. and 10 a.m.**

- Time duration ($t$) = 1 hour.
    
- Parameter $\lambda = 4 \times 1 = 4$.
    
- $x = 6$.
    

$$P(X=6) = \frac{e^{-4} \cdot 4^6}{6!}$$

$$P(X=6) = \frac{0.0183156 \cdot 4096}{720}$$

$$P(X=6) \approx \mathbf{0.1042}$$

---

### **Solution 10**

**Moment Generating Functions (MGF)**

1. Binomial Distribution

Given: $P(X=r) = {}^nC_r \cdot p^r \cdot q^{n-r}$

The MGF, $M_X(t) = E[e^{tX}]$, is defined as:

$$M_X(t) = \sum_{r=0}^{n} e^{tr} \cdot {}^nC_r \cdot p^r \cdot q^{n-r}$$

$$M_X(t) = \sum_{r=0}^{n} {}^nC_r \cdot (pe^t)^r \cdot q^{n-r}$$

Using the Binomial Theorem $(a+b)^n = \sum {}^nC_r a^r b^{n-r}$, let $a = pe^t$ and $b = q$.

$$M_X(t) = (q + pe^t)^n$$

2. Poisson Distribution

Given: $P(X=r) = \frac{e^{-\lambda} \cdot \lambda^r}{r!}$

The MGF, $M_X(t) = E[e^{tX}]$, is defined as:

$$M_X(t) = \sum_{r=0}^{\infty} e^{tr} \cdot \frac{e^{-\lambda} \cdot \lambda^r}{r!}$$

$$M_X(t) = e^{-\lambda} \sum_{r=0}^{\infty} \frac{(\lambda e^t)^r}{r!}$$

Recall the expansion of $e^x = \sum \frac{x^r}{r!}$. Here, our "$x$" is $\lambda e^t$.

$$M_X(t) = e^{-\lambda} \cdot e^{\lambda e^t}$$

$$M_X(t) = e^{\lambda(e^t - 1)}$$
---
