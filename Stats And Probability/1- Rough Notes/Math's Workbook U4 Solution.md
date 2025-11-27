
### 11. A Binomial random variable X satisfies the relation $9P(X=4)=P(X=2)$, where $n=6$. Find value of $P(X=3)$.

Step 1: Understand the Binomial Probability Formula

The probability mass function (PMF) for a Binomial distribution is given by:

$$P(X=r) = \binom{n}{r} p^r q^{n-r}$$

Where:

- $n = 6$
    
- $q = 1 - p$
    

Step 2: Set up the given equation

We are given $9P(X=4) = P(X=2)$.

$$9 \cdot \binom{6}{4} p^4 q^{6-4} = \binom{6}{2} p^2 q^{6-2}$$

Step 3: Solve for $p$

First, calculate the combinations:

$\binom{6}{4} = \frac{6 \times 5}{2 \times 1} = 15$

$\binom{6}{2} = \frac{6 \times 5}{2 \times 1} = 15$

Substitute these back into the equation:

$$9(15) p^4 q^2 = (15) p^2 q^4$$

Divide both sides by $15 p^2 q^2$ (assuming $p,q \neq 0$):

$$9 p^2 = q^2$$

Take the square root of both sides:

$$3p = q$$

Since $q = 1 - p$:

$$3p = 1 - p$$

$$4p = 1 \implies p = 0.25 \quad (\text{and } q = 0.75)$$

Step 4: Calculate $P(X=3)$

$$P(X=3) = \binom{6}{3} (0.25)^3 (0.75)^3$$

$$\binom{6}{3} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20$$

$$P(X=3) = 20 \cdot \left(\frac{1}{4}\right)^3 \cdot \left(\frac{3}{4}\right)^3$$

$$P(X=3) = 20 \cdot \frac{1}{64} \cdot \frac{27}{64}$$

$$P(X=3) = \frac{540}{4096} \approx \mathbf{0.1318}$$

---

### 12. If the Probability that an individual suffers a bad reaction from a certain medicine is 0.001, then what will be the Probability that exactly one will suffer of bad reaction out of 2000 individuals (where $e^{-2}=0.13533$)?

Step 1: Identify the Distribution

Since $n$ is large ($2000$) and $p$ is small ($0.001$), we approximate the Binomial distribution using the Poisson distribution.

Step 2: Calculate the mean ($\lambda$)

$$\lambda = n \times p$$

$$\lambda = 2000 \times 0.001 = 2$$

Step 3: Use the Poisson Formula

The formula is $P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$.

We need to find the probability for exactly one individual ($k=1$).

$$P(X=1) = \frac{e^{-2} \cdot 2^1}{1!}$$

$$P(X=1) = 2 \cdot e^{-2}$$

Step 4: Substitute the given value

Given $e^{-2} = 0.13533$:

$$P(X=1) = 2 \cdot 0.13533$$

$$P(X=1) = \mathbf{0.27066}$$

---

### 13. Find the value of $k$ such that the exponential distribution $f(x)=ke^{-x/7}$ for $0 \le x < \infty$.

Step 1: Use the property of PDF

For a function to be a valid Probability Density Function (PDF), the integral over its entire range must equal 1.

$$\int_{0}^{\infty} f(x) \, dx = 1$$

$$\int_{0}^{\infty} k e^{-x/7} \, dx = 1$$

Step 2: Integrate

$$k \left[ \frac{e^{-x/7}}{-1/7} \right]_{0}^{\infty} = 1$$

$$k \left[ -7e^{-x/7} \right]_{0}^{\infty} = 1$$

Evaluate the limits (note that $e^{-\infty} = 0$ and $e^{0} = 1$):

$$k \left[ (-7(0)) - (-7(1)) \right] = 1$$

$$k [7] = 1$$

Step 3: Solve for $k$

$$7k = 1$$

$$k = \frac{1}{7}$$

---

### 14. The time, T minutes, Jason takes to cycle to school is Normally distributed with a mean of 17 and a variance of 8. Find the probability that on a given day Jason will take over 22 minutes to cycle to school.

**Step 1: Identify Parameters**

- Mean ($\mu$) = 17
    
- Variance ($\sigma^2$) = 8
    
- Standard Deviation ($\sigma$) = $\sqrt{8} \approx 2.828$
    

Step 2: Calculate the Z-score

We want to find $P(X > 22)$. First, standardize the value 22.

$$Z = \frac{X - \mu}{\sigma}$$

$$Z = \frac{22 - 17}{\sqrt{8}} = \frac{5}{2.828} \approx 1.768$$

Step 3: Find the Probability

We need $P(Z > 1.77)$ (rounding to 2 decimals for standard tables).

Using standard normal distribution tables:

$$P(Z < 1.77) \approx 0.9616$$

Since we want the area greater than 22 (the right tail):

$$P(X > 22) = 1 - P(Z < 1.77)$$

$$P(X > 22) = 1 - 0.9616 = \mathbf{0.0384}$$

---

### 15. A discrete random variable X has Poisson distribution with mean $\lambda$. Given that $P(X=8)=P(X=9)$, determine the value of $P(4X \le 1)$.

Step 1: Use the given condition to find $\lambda$

Poisson PMF: $P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$

Given $P(X=8) = P(X=9)$:

$$\frac{e^{-\lambda}\lambda^8}{8!} = \frac{e^{-\lambda}\lambda^9}{9!}$$

Divide both sides by $e^{-\lambda}\lambda^8$:

$$\frac{1}{8!} = \frac{\lambda}{9!}$$

Rearrange to solve for $\lambda$:

$$\lambda = \frac{9!}{8!} = \frac{9 \times 8!}{8!} = 9$$

So, the mean $\lambda = 9$.

Step 2: Interpret the Target Probability

We need to find $P(4X \le 1)$.

$$4X \le 1 \implies X \le \frac{1}{4}$$

$$X \le 0.25$$

Since Poisson is a discrete distribution dealing with counts ($0, 1, 2, \dots$), the only integer value satisfying $X \le 0.25$ is $X = 0$.

Step 3: Calculate $P(X=0)$

$$P(X=0) = \frac{e^{-9} \cdot 9^0}{0!}$$

$$P(X=0) = e^{-9}$$

---

### 16. A random variable X has an exponential distribution with probability distribution function given by $f(x)=5e^{-5x}$ for $x>0$. Find the probability that X is not less than 2.

Step 1: Identify the goal

"Not less than 2" means $P(X \ge 2)$.

Step 2: Set up the Integral

We integrate the PDF from 2 to infinity.

$$P(X \ge 2) = \int_{2}^{\infty} 5e^{-5x} \, dx$$

Step 3: Solve the Integral

$$= \left[ \frac{5e^{-5x}}{-5} \right]_{2}^{\infty}$$

$$= \left[ -e^{-5x} \right]_{2}^{\infty}$$

Evaluate limits:

$$= (-e^{-\infty}) - (-e^{-5(2)})$$

$$= 0 - (-e^{-10})$$

$$= e^{-10}$$

---
### 17. If $x$ is a random variable for which $E(x)=10$ and $Var(x)=25$. Find the values of $a$ and $b$ such that $y=ax-b$ has expectation and variance equal to 1.

**Step 1: Use the properties of Expectation and Variance**

- **Expectation Property:** $E(ax - b) = aE(x) - b$
- **Variance Property:** $Var(ax - b) = a^2 Var(x)$

Step 2: Set up the equations

We are given $E(y) = 1$ and $Var(y) = 1$.

1. $E(ax - b) = 1 \implies a(10) - b = 1$
2. $Var(ax - b) = 1 \implies a^2(25) = 1$

Step 3: Solve for $a$

From equation (2):

$$25a^2 = 1$$

$$a^2 = \frac{1}{25}$$

$$a = \pm \frac{1}{5} = \pm 0.2$$

**Step 4: Solve for $b$**

- Case 1 (taking $a = 0.2$):
    
    $$10(0.2) - b = 1$$
    
    $$2 - b = 1 \implies b = 1$$
    
- Case 2 (taking $a = -0.2$):
    
    $$10(-0.2) - b = 1$$
    
    $$-2 - b = 1 \implies b = -3$$
    

**Answer:** $a = 0.2, b = 1$ or  $a = -0.2, b = -3$

---

### 18. Find the moment generating function of a random variable whose moments about origin are $v_{r}=(r+1)!2^{r}$.

Step 1: Write the definition of MGF

The Moment Generating Function $M_X(t)$ is defined as the exponential generating function of the moments $v_r$:

$$M_X(t) = \sum_{r=0}^{\infty} \frac{t^r}{r!} v_r$$

Step 2: Substitute the given moments

$$M_X(t) = \sum_{r=0}^{\infty} \frac{t^r}{r!} (r+1)! 2^r$$

Step 3: Simplify the terms

Recall that $(r+1)! = (r+1) \times r!$.

$$M_X(t) = \sum_{r=0}^{\infty} \frac{t^r 2^r}{r!} (r+1) r!$$

$$M_X(t) = \sum_{r=0}^{\infty} (2t)^r (r+1)$$

Step 4: Identify the series

Expand the summation:

$$r=0 \implies (2t)^0(1) = 1$$

$$r=1 \implies (2t)^1(2) = 2(2t)$$

$$r=2 \implies (2t)^2(3) = 3(2t)^2$$

Series: $1 + 2(2t) + 3(2t)^2 + \dots$

This is the Binomial expansion for $(1-x)^{-2}$, where $x = 2t$.

$$(1-x)^{-2} = 1 + 2x + 3x^2 + \dots$$

**Answer:** $M_X(t) = (1 - 2t)^{-2}$ (valid for $|2t| < 1$)

---

### 19. Fit a binomial distribution to the data given in the following data:

|**x**|**0**|**1**|**2**|**3**|**4**|
|---|---|---|---|---|---|
|f|24|41|28|5|2|

Step 1: Calculate the Mean of the observed data

Total Frequency ($N$) = $24 + 41 + 28 + 5 + 2 = 100$

$\sum fx = 0(24) + 1(41) + 2(28) + 3(5) + 4(2)$

$\sum fx = 0 + 41 + 56 + 15 + 8 = 120$

Mean ($\bar{x}$) = $\frac{\sum fx}{N} = \frac{120}{100} = 1.2$

Step 2: Find Binomial Parameters $n$ and $p$

Since the data goes from $x=0$ to $x=4$, we take $n = 4$.

For a binomial distribution, Mean $= np$.

$$1.2 = 4p \implies p = 0.3$$

$$q = 1 - p = 0.7$$

Step 3: Calculate Theoretical Frequencies

Formula: $T(x) = N \times P(X=x) = 100 \times \binom{4}{x} (0.3)^x (0.7)^{4-x}$

- **x = 0:** $100 \times 1 \times 1 \times (0.7)^4 = 100 \times 0.2401 = \mathbf{24.01}$
    
- **x = 1:** $100 \times 4 \times (0.3)^1 \times (0.7)^3 = 100 \times 1.2 \times 0.343 = \mathbf{41.16}$
    
- **x = 2:** $100 \times 6 \times (0.3)^2 \times (0.7)^2 = 100 \times 0.54 \times 0.49 = \mathbf{26.46}$
    
- **x = 3:** $100 \times 4 \times (0.3)^3 \times (0.7)^1 = 100 \times 0.108 \times 0.7 = \mathbf{7.56}$
    
- **x = 4:** $100 \times 1 \times (0.3)^4 \times 1 = 100 \times 0.0081 = \mathbf{0.81}$
    

**Answer:** The fitted distribution is roughly: $24, 41, 26, 8, 1$.

---

### 20. It is given that 2% of the electric bulbs manufactured by a company are defective. Using Poisson distribution find the probability that a sample of 200 bulbs will contain:

I. No defective bulb

II. Two defective bulbs

III. At most three defective bulbs.

**Step 1: Identify Parameters**

- $n = 200$
    
- $p = 0.02$
    
- Mean $\lambda = np = 200 \times 0.02 = 4$
    

**Step 2: Solve using $P(X=x) = \frac{e^{-\lambda} \lambda^x}{x!}$**

I. No defective bulb ($x=0$)

$$P(X=0) = \frac{e^{-4} 4^0}{0!} = e^{-4} \approx \mathbf{0.0183}$$

II. Two defective bulbs ($x=2$)

$$P(X=2) = \frac{e^{-4} 4^2}{2!} = \frac{0.0183 \times 16}{2} \approx \mathbf{0.1465}$$

III. At most three defective bulbs ($X \le 3$)

$$P(X \le 3) = P(0) + P(1) + P(2) + P(3)$$

- $P(0) \approx 0.0183$
    
- $P(1) = \frac{e^{-4} 4^1}{1!} \approx 0.0732$
    
- $P(2) \approx 0.1465$
    
- $P(3) = \frac{e^{-4} 4^3}{3!} = \frac{0.0183 \times 64}{6} \approx 0.1952$
    

Sum $= 0.0183 + 0.0732 + 0.1465 + 0.1952 = \mathbf{0.4332}$

---

### 21. In a test on 2000 electric bulbs... average life of 2040 hours and S.D. of 60 hours, estimate the number of bulbs likely to burn for More than 2150 hours.

Step 1: Calculate Z-score

$$Z = \frac{X - \mu}{\sigma} = \frac{2150 - 2040}{60} = \frac{110}{60} \approx 1.83$$

Step 2: Find Probability

From Z-table, Area to the left of $Z=1.83$ is $0.9664$.

Area to the right (More than 2150) $= 1 - 0.9664 = 0.0336$.

Step 3: Estimate Number of Bulbs

$$N = \text{Total Bulbs} \times \text{Probability}$$

$$N = 2000 \times 0.0336 = 67.2$$

**Answer:** Approximately **67 bulbs**.

---

### 22. The length of Telephone conversation is an exponential variate with mean 7 minutes. Find the Probability that call:

i. End in less than 7 minutes.

ii. Tabs between 7 to 10 minutes.

Step 1: Identify Parameter

Mean $= 1/\lambda = 7 \implies \lambda = 1/7$.

CDF Formula: $P(X < x) = 1 - e^{-\lambda x}$.

i. Less than 7 minutes ($X < 7$)

$$P(X < 7) = 1 - e^{-(1/7) \times 7} = 1 - e^{-1}$$

$$= 1 - 0.3679 = \mathbf{0.6321}$$

ii. Between 7 and 10 minutes ($7 < X < 10$)

$$P(7 < X < 10) = P(X < 10) - P(X < 7)$$

$$= (1 - e^{-10/7}) - (1 - e^{-1})$$

$$= e^{-1} - e^{-10/7}$$

$$= 0.3679 - 0.2396 = \mathbf{0.1283}$$

---

### 23. The weights of newly born kittens are Normally distributed. 4.95% of newly b
orn kittens are heavier than 122 grams and 10.56% are lighter than 93 grams. Find the mean and the standard deviation...

Step 1: Set up Z-score equations

Let Mean $= \mu$ and S.D $= \sigma$.

1. Heavier than 122g (Right tail area = 0.0495):
    
    Left area $= 1 - 0.0495 = 0.9505$.
    
    Looking at Z-table, $Z \approx 1.65$ corresponds to area $0.9505$.
    
    Equation 1: $122 = \mu + 1.65\sigma$
    
2. Lighter than 93g (Left tail area = 0.1056):
    
    Looking at Z-table for area $0.1056$ (or negative Z for $1-0.1056=0.8944$).
    
    $Z \approx -1.25$ corresponds to this area.
    
    Equation 2: $93 = \mu - 1.25\sigma$
    

Step 2: Solve the simultaneous equations

Subtract Eq(2) from Eq(1):

$$(122 - 93) = (\mu - \mu) + (1.65\sigma - (-1.25\sigma))$$

$$29 = 2.9\sigma$$

$$\sigma = 10$$

Step 3: Find Mean

Substitute $\sigma = 10$ into Eq(1):

$$122 = \mu + 1.65(10)$$

$$122 = \mu + 16.5$$

$$\mu = 105.5$$

**Answer:** Mean = **105.5 grams**, Standard Deviation = **10 grams**

---
**24. Obtained the moment generating function of the random variable having probability distribution**

$$f(x) = \begin{cases} x, & 0 < x < 1 \\ 2 - x, & 1 \le x < 2 \\ 0, & \text{else where} \end{cases}$$

**Also determine mean and variance of the distribution.**

**Solution:**

1. Moment Generating Function (MGF)

The definition of MGF is $M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty} e^{tx} f(x) dx$.

Splitting the integral over the defined ranges:

$$M_X(t) = \int_{0}^{1} e^{tx}(x) dx + \int_{1}^{2} e^{tx}(2-x) dx$$

Using Integration by Parts $\int u v' dx = uv - \int u' v dx$:

For the first part: $\int x e^{tx} dx = \left[ \frac{xe^{tx}}{t} - \frac{e^{tx}}{t^2} \right]_0^1$

$$= \left( \frac{e^t}{t} - \frac{e^t}{t^2} \right) - \left( 0 - \frac{1}{t^2} \right) = \frac{e^t}{t} - \frac{e^t - 1}{t^2}$$

For the second part: $\int (2-x) e^{tx} dx$. Let $u = 2-x, v' = e^{tx}$. Then $u' = -1, v = \frac{e^{tx}}{t}$.

$$= \left[ \frac{(2-x)e^{tx}}{t} \right]_1^2 - \int_1^2 -1 \cdot \frac{e^{tx}}{t} dx$$

$$= \left[ 0 - \frac{e^t}{t} \right] + \frac{1}{t} \left[ \frac{e^{tx}}{t} \right]_1^2$$

$$= -\frac{e^t}{t} + \frac{1}{t^2} (e^{2t} - e^t)$$

Adding both parts:

$$M_X(t) = \left( \frac{e^t}{t} - \frac{e^t}{t^2} + \frac{1}{t^2} \right) + \left( -\frac{e^t}{t} + \frac{e^{2t}}{t^2} - \frac{e^t}{t^2} \right)$$

$$M_X(t) = \frac{1}{t^2} (e^{2t} - 2e^t + 1) = \frac{(e^t - 1)^2}{t^2} = \left( \frac{e^t - 1}{t} \right)^2$$

2. Mean ($E(X)$)

Due to the symmetry of the triangular distribution from 0 to 2, the Mean is at the center.

$$E(X) = \int_0^1 x(x) dx + \int_1^2 x(2-x) dx$$

$$= \left[ \frac{x^3}{3} \right]_0^1 + \left[ x^2 - \frac{x^3}{3} \right]_1^2$$

$$= \frac{1}{3} + \left( (4 - \frac{8}{3}) - (1 - \frac{1}{3}) \right)$$

$$= \frac{1}{3} + \frac{4}{3} - \frac{2}{3} = \mathbf{1}$$

3. Variance ($Var(X)$)

First, find $E(X^2) = \int_0^1 x^2(x) dx + \int_1^2 x^2(2-x) dx$.

$$= \int_0^1 x^3 dx + \int_1^2 (2x^2 - x^3) dx$$

$$= \left[ \frac{x^4}{4} \right]_0^1 + \left[ \frac{2x^3}{3} - \frac{x^4}{4} \right]_1^2$$

$$= \frac{1}{4} + \left[ (\frac{16}{3} - 4) - (\frac{2}{3} - \frac{1}{4}) \right]$$

$$= \frac{1}{4} + \frac{16}{3} - 4 - \frac{2}{3} + \frac{1}{4}$$

$$= \frac{2}{4} + \frac{14}{3} - 4 = 0.5 + 4.666 - 4 = 1.166 \text{ or } \frac{7}{6}$$

$$Var(X) = E(X^2) - [E(X)]^2$$

$$Var(X) = \frac{7}{6} - (1)^2 = \frac{1}{6}$$

**Answer:** $M_X(t) = (\frac{e^t-1}{t})^2$, Mean $= 1$, Variance $= \frac{1}{6}$.

---

25. The discrete random variables X and Y are independent from one another and X and Y are defined as $X \sim B(4, 0.5)$ and $Y \sim B(6, 0.4)$.

a) Find the value of $Var(XY)$.

b) Determine $P(XY = 0)$.

**Solution:**

Parameters:

For X ($n=4, p=0.5$):

- $E(X) = np = 2$
    
- $Var(X) = npq = 4(0.5)(0.5) = 1$
    
- $E(X^2) = Var(X) + [E(X)]^2 = 1 + 2^2 = 5$
    

For Y ($n=6, p=0.4$):

- $E(Y) = np = 2.4$
    
- $Var(Y) = npq = 6(0.4)(0.6) = 1.44$
    
- $E(Y^2) = Var(Y) + [E(Y)]^2 = 1.44 + (2.4)^2 = 1.44 + 5.76 = 7.2$
    

a) Find $Var(XY)$

Formula: $Var(XY) = E(X^2 Y^2) - [E(XY)]^2$

Since X and Y are independent:

$$E(XY) = E(X)E(Y) = 2 \times 2.4 = 4.8$$

$$E(X^2 Y^2) = E(X^2)E(Y^2) = 5 \times 7.2 = 36$$

$$Var(XY) = 36 - (4.8)^2$$

$$Var(XY) = 36 - 23.04 = \mathbf{12.96}$$

b) Determine $P(XY = 0)$

$XY = 0$ if $X = 0$ OR $Y = 0$.

Using the complement rule: $P(XY=0) = 1 - P(XY \neq 0)$.

Since X and Y are independent: $P(XY \neq 0) = P(X \neq 0) \times P(Y \neq 0)$.

$P(X=0) = {^4}C_0 (0.5)^0 (0.5)^4 = 0.0625$

$\implies P(X \neq 0) = 1 - 0.0625 = 0.9375$

$P(Y=0) = {^6}C_0 (0.4)^0 (0.6)^6 = 0.046656$

$\implies P(Y \neq 0) = 1 - 0.046656 = 0.953344$

$P(XY \neq 0) = 0.9375 \times 0.953344 \approx 0.89376$

$P(XY = 0) = 1 - 0.89376 = \mathbf{0.10624}$

---

26. The number of monthly breakdowns of a computer is a RV having a Poisson distribution with mean equal to 1.8. Find the probability that this computer will function for a month:

(i) Without a breakdown

(ii) With only one breakdown

(iii) With at most one breakdown

(iv) With at least one breakdown

Solution:

Given: $\lambda = 1.8$.

Formula: $P(X=x) = \frac{e^{-1.8}(1.8)^x}{x!}$

(Note: $e^{-1.8} \approx 0.1653$)

(i) Without a breakdown ($x=0$)

$$P(0) = e^{-1.8} = \mathbf{0.1653}$$

(ii) With only one breakdown ($x=1$)

$$P(1) = \frac{e^{-1.8}(1.8)^1}{1!} = 0.1653 \times 1.8 = \mathbf{0.2975}$$

(iii) With at most one breakdown ($x \le 1$)

$$P(X \le 1) = P(0) + P(1)$$

$$= 0.1653 + 0.2975 = \mathbf{0.4628}$$

(iv) With at least one breakdown ($x \ge 1$)

$$P(X \ge 1) = 1 - P(0)$$

$$= 1 - 0.1653 = \mathbf{0.8347}$$

---

**27. In a distribution exactly Normal, 31% of the items are under 45 and 8% are over 64. What are the mean and Standard deviation of this Distribution? It is given that $f(0.5) = 0.19$, $f(1.4)=0.42$.**

**Solution:**

Let mean be $\mu$ and standard deviation be $\sigma$.

We convert X to Z-scores using $Z = \frac{X - \mu}{\sigma}$.

Case 1: 31% are under 45

$P(X < 45) = 0.31$.

Since this probability is less than 0.5, the Z-score is negative.

Area to the left of mean is 0.5. We need the Z value where the area from Mean (0) to Z is $0.5 - 0.31 = 0.19$.

Given $f(0.5) = 0.19$, this corresponds to $Z = -0.5$ (negative because it's below mean).

$$\frac{45 - \mu}{\sigma} = -0.5 \implies 45 - \mu = -0.5\sigma \quad \dots(1)$$

Case 2: 8% are over 64

$P(X > 64) = 0.08$.

This implies $P(X < 64) = 1 - 0.08 = 0.92$.

The area from Mean (0) to Z is $0.92 - 0.5 = 0.42$.

Given $f(1.4) = 0.42$, this corresponds to $Z = 1.4$.

$$\frac{64 - \mu}{\sigma} = 1.4 \implies 64 - \mu = 1.4\sigma \quad \dots(2)$$

Solving the system:

From (1): $\mu = 45 + 0.5\sigma$

Substitute into (2):

$$64 - (45 + 0.5\sigma) = 1.4\sigma$$

$$19 - 0.5\sigma = 1.4\sigma$$

$$19 = 1.9\sigma$$

$$\sigma = 10$$

Substitute $\sigma=10$ back to find $\mu$:

$$\mu = 45 + 0.5(10) = 50$$

**Answer:** Mean ($\mu$) = 50, Standard Deviation ($\sigma$) = 10.

---

**28. Find the moment generating function of the distribution $f(x)=\frac{1}{b}e^{-\frac{x}{b}}; b>0, 0\le x\le \infty$. Hence find its mean and first two moments about origin and standard deviation.**

**Solution:**

1. Moment Generating Function (MGF)

$$M_X(t) = \int_0^\infty e^{tx} \frac{1}{b} e^{-x/b} dx$$

$$= \frac{1}{b} \int_0^\infty e^{-x(\frac{1}{b} - t)} dx$$

For the integral to converge, we assume $t < 1/b$.

$$= \frac{1}{b} \left[ \frac{e^{-x(\frac{1}{b} - t)}}{-(\frac{1}{b} - t)} \right]_0^\infty$$

$$= \frac{1}{b} \left( 0 - \frac{1}{-(\frac{1}{b} - t)} \right) = \frac{1}{b} \cdot \frac{1}{\frac{1 - bt}{b}} = \frac{1}{1 - bt} = (1 - bt)^{-1}$$

2. Moments about Origin

Expand $(1 - bt)^{-1}$ as a series: $1 + bt + (bt)^2 + \dots$

$$M_X(t) = 1 + b t + b^2 t^2 + b^3 t^3 \dots$$

Comparing with $M_X(t) = 1 + \mu_1' t + \mu_2' \frac{t^2}{2!} + \dots$

- First Moment ($\mu_1'$ or Mean): The coefficient of $t$ is $b$.
    
    $$E(X) = b$$
    
- Second Moment ($\mu_2'$): The coefficient of $\frac{t^2}{2!}$ is $2b^2$ (since term is $b^2 t^2 = 2b^2 \frac{t^2}{2}$).
    
    $$E(X^2) = 2b^2$$
    

3. Standard Deviation

$$Variance = E(X^2) - [E(X)]^2$$

$$Var(X) = 2b^2 - (b)^2 = b^2$$

$$S.D.(X) = \sqrt{b^2} = b$$

**Answer:** MGF = $(1-bt)^{-1}$, Mean = $b$, $\mu_2' = 2b^2$, S.D. = $b$.

---

29. In a sample of 1000 cases, the mean of a certain test is 14 and standard deviation is 2.5. Assuming distribution to be normal find:

I. How many students score between 12 and 15?

II. How many score above 18?

III. How many score below 8?

IV. How many score 16?

Solution:

Given: $N=1000, \mu=14, \sigma=2.5$.

$Z = \frac{X - 14}{2.5}$

I. Between 12 and 15

$X=12 \to Z = \frac{12-14}{2.5} = -0.8$

$X=15 \to Z = \frac{15-14}{2.5} = 0.4$

Area($-0.8 < Z < 0.4$) = Area(0 to 0.8) + Area(0 to 0.4)

From Z-table: $0.2881 + 0.1554 = 0.4435$

Students = $1000 \times 0.4435 = \mathbf{443.5} \approx 444$

II. Above 18

$X=18 \to Z = \frac{18-14}{2.5} = 1.6$

Area($Z > 1.6$) = $0.5 - \text{Area}(0 \text{ to } 1.6)$

From Z-table: $0.5 - 0.4452 = 0.0548$

Students = $1000 \times 0.0548 = \mathbf{54.8} \approx 55$

III. Below 8

$X=8 \to Z = \frac{8-14}{2.5} = -2.4$

Area($Z < -2.4$) = $0.5 - \text{Area}(0 \text{ to } 2.4)$

From Z-table: $0.5 - 0.4918 = 0.0082$

Students = $1000 \times 0.0082 = \mathbf{8.2} \approx 8$

IV. Score 16

Since "score 16" refers to a discrete integer in a test, we apply continuity correction ($15.5$ to $16.5$).

$Z_1 = \frac{15.5-14}{2.5} = 0.6$

$Z_2 = \frac{16.5-14}{2.5} = 1.0$

Area = Area(0 to 1.0) - Area(0 to 0.6)

$= 0.3413 - 0.2257 = 0.1156$

Students = $1000 \times 0.1156 = \mathbf{115.6} \approx 116$

---

**30. Seven coins are tossed and no. of heads noted. The experiment is repeated 128 times and the following distribution is obtained:**

|**No. of heads**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**Total**|
|---|---|---|---|---|---|---|---|---|---|
|**Frequencies**|7|6|19|35|30|23|7|1|128|

Solution:

(To solve this, we fit a Binomial Distribution to the data)

1. Calculate the Observed Mean

Mean $\bar{x} = \frac{\sum fx}{\sum f}$

$\sum fx = (0\times7) + (1\times6) + (2\times19) + (3\times35) + (4\times30) + (5\times23) + (6\times7) + (7\times1)$

$= 0 + 6 + 38 + 105 + 120 + 115 + 42 + 7 = 433$

$$\bar{x} = \frac{433}{128} \approx 3.3828$$

2. Determine Parameters

Since 7 coins are tossed, $n = 7$.

For Binomial distribution, Mean $= np$.

$$7p = 3.3828 \implies p = \frac{3.3828}{7} \approx 0.483$$

$$q = 1 - p \approx 0.517$$

(Note: Since coins are usually unbiased, we can also test against ideal $p=0.5$. If $p=0.5$, Mean=3.5. Our observed mean 3.38 is close. Standard fitting uses the calculated $p$).

3. Calculate Expected Frequencies

Formula: $N \times P(x) = 128 \times {^7}C_x (0.483)^x (0.517)^{7-x}$

- **x=0:** $128(0.517)^7 = 1.25$
    
- **x=1:** $128 \times 7 \times (0.483)(0.517)^6 = 8.7$
    
- **x=2:** $128 \times 21 \times (0.483)^2 (0.517)^5 = 26.2$
    
- **x=3:** $128 \times 35 \times (0.483)^3 (0.517)^4 = 43.6$
    
- **x=4:** $128 \times 35 \times (0.483)^4 (0.517)^3 = 43.5$
    
- **x=5:** $128 \times 21 \times (0.483)^5 (0.517)^2 = 26.0$
    
- **x=6:** $128 \times 7 \times (0.483)^6 (0.517)^1 = 8.6$
    
- **x=7:** $128 \times (0.483)^7 = 1.2$
    

**Comparison Table:**

|**Heads (x)**|**Observed Freq**|**Expected Freq (Fitted)**|
|---|---|---|
|0|7|1|
|1|6|9|
|2|19|26|
|3|35|44|
|4|30|44|
|5|23|26|
|6|7|9|
|7|1|1|