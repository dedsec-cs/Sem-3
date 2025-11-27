## Random Variable (R.V.)

A **Random Variable ($X$)** is a mathematical concept that links the results of a random experiment to numerical values. It is a **function** that maps every outcome in the **sample space ($S$)** to a unique real number.

* **Domain:** The **Sample Space ($S$)** (The set of all possible outcomes of the experiment).
* **Range:** A **subset of Real Numbers ($\mathbb{R}$)** (The possible numerical values the random variable can take).

---

### Example 1: Tossing Two Coins

**Experiment:** Tossing two coins.
**Random Variable ($X$):** "Number of Heads".

1.  **Determine the Sample Space ($S$):**
    The possible outcomes when tossing two coins are:
    $$S = \{HH, HT, TH, TT\}$$

2.  **Determine the Values of the Random Variable ($X$):**
    The function $X$ assigns a numerical value (the count of Heads) to each sample point:
    * For the outcome $HH$: $X(HH) = \mathbf{2}$ (two Heads)
    * For the outcome $HT$: $X(HT) = \mathbf{1}$ (one Head)
    * For the outcome $TH$: $X(TH) = \mathbf{1}$ (one Head)
    * For the outcome $TT$: $X(TT) = \mathbf{0}$ (zero Heads)

The values that the Random Variable $X$ can take are **$\{0, 1, 2\}$**.

---

### Example 2: Tossing Three Coins

**Experiment:** Tossing three coins.
**Random Variable ($X$):** "Number of Heads".

1.  **Determine the Sample Space ($S$):**
    The possible outcomes when tossing three coins are (Total $2^3 = 8$ outcomes):
    $$S = \{HHH, HHT, HTH, THH, HTT, THT, TTH, TTT\}$$

2.  **Determine the Sample Points and Corresponding Values for $X$:**
    The function $X$ assigns the count of Heads to each sample point:

| Sample Point ($\omega$) | Description | Value of R.V. ($X(\omega)$) |
| :--- | :--- | :--- |
| HHH | Three Heads | $\mathbf{3}$ |
| HHT | Two Heads, One Tail | $\mathbf{2}$ |
| HTH | Two Heads, One Tail | $\mathbf{2}$ |
| THH | Two Heads, One Tail | $\mathbf{2}$ |
| HTT | One Head, Two Tails | $\mathbf{1}$ |
| THT | One Head, Two Tails | $\mathbf{1}$ |
| TTH | One Head, Two Tails | $\mathbf{1}$ |
| TTT | Zero Heads | $\mathbf{0}$ |

The values that the Random Variable $X$ can take are **$\{0, 1, 2, 3\}$**.

---

## 2. Types of Random Variables

A Random Variable (R.V.) is classified based on the nature of the numerical values it can assume.

* **Discrete Random Variable:** This is a variable whose possible values are countable. The values are typically integers and have gaps between them (isolated values).
    * *Examples:* The number of defective items in a batch, the number of emails received per hour, or the number of heads in coin tosses (as in our examples).
* **Continuous Random Variable:** This is a variable that can take on any value within a given range or interval. The number of possible values is uncountable.
    * *Examples:* The height of a person, the temperature of a room, or the time taken to complete a task.

---

## 3. Discrete Random Variable Tools

The behavior of a Discrete Random Variable ($X$) is fully described by its probability distribution, which is managed using the following tools:

### Probability Mass Function (PMF)

The **Probability Mass Function ($P(X=x)$ or $p(x)$)** is a function that provides the probability for each specific value $x$ that the discrete random variable $X$ can take.

* **Conditions for a function to be a PMF:**
    1.  **Non-Negativity:** The probability for any given value $x_i$ must be non-negative:
        $$P(x_i) \ge 0 \quad \text{for all } i$$
    2.  **Total Probability:** The sum of the probabilities over all possible values of the random variable must equal $1$:
        $$\sum P(x_i) = 1$$

### Probability Distribution

The **Probability Distribution** is a table or list that systematically pairs every possible value of the random variable ($x_i$) with its corresponding probability ($p_i = P(X=x_i)$).

### Mean (Expected Value)

The **Mean ($\mu$)**, or **Expected Value ($E(X)$)**, represents the long-run average value of the random variable if the experiment were repeated many times. It is the center of the probability distribution.

$$\mu = E(X) = \sum x_i p_i$$

### Variance

The **Variance ($\sigma^2$)** measures the spread or dispersion of the probability distribution around its mean. A higher variance means the values are more spread out from the expected value.

$$\sigma^2 = \sum p_i (x_i - \mu)^2$$

The **Standard Deviation** ($\sigma$) is the square root of the variance and is often preferred because it is in the same units as the random variable $X$.

---

## Application: Two Coin Tossed Example

Let's use the experiment of tossing two coins to illustrate these tools.
**Random Variable ($X$):** The number of Heads.

### 1. Identify Values and Calculate PMF

* **Sample Space:** $S = \{HH, HT, TH, TT\}$, so $n(S) = 4$.
* **Possible Values for $X$ ($x_i$):** $\{0, 1, 2\}$.

We calculate the probability $P(X=x)$ for each value:

| Value of $X$ ($x_i$) | Outcome(s) | Probability $P(X=x_i) = p_i$ |
| :--- | :--- | :--- |
| $\mathbf{0}$ | $TT$ | $P(X=0) = \frac{1}{4}$ |
| $\mathbf{1}$ | $HT, TH$ | $P(X=1) = \frac{2}{4} = \frac{1}{2}$ |
| $\mathbf{2}$ | $HH$ | $P(X=2) = \frac{1}{4}$ |

### 2. Construct the Probability Distribution

The table above is the **Probability Distribution** for the random variable $X$.

**Verification of PMF Conditions:**
1.  **Non-Negativity:** $1/4, 1/2, 1/4$ are all $\ge 0$. **(Condition 1 satisfied)**
2.  **Total Probability:** $\sum P(x_i) = \frac{1}{4} + \frac{2}{4} + \frac{1}{4} = \frac{4}{4} = 1$. **(Condition 2 satisfied)**

### 3. Calculate the Mean (Expected Value)

$$\mu = E(X) = \sum x_i p_i$$

| $x_i$ | $p_i$ | $x_i p_i$ |
| :--- | :--- | :--- |
| $0$ | $1/4$ | $0 \times 1/4 = 0$ |
| $1$ | $2/4$ | $1 \times 2/4 = 2/4$ |
| $2$ | $1/4$ | $2 \times 1/4 = 2/4$ |
| **Sum** | $1$ | $\sum x_i p_i = 4/4 = \mathbf{1}$ |

The **Mean** or **Expected Value** is $\mu = 1$. (We expect $1$ Head on average over many trials).

### 4. Calculate the Variance

$$\sigma^2 = \sum p_i (x_i - \mu)^2$$

| $x_i$ | $p_i$ | $(x_i - \mu)$ | $(x_i - \mu)^2$ | $p_i (x_i - \mu)^2$ |
| :--- | :--- | :--- | :--- | :--- |
| $0$ | $1/4$ | $0 - 1 = -1$ | $(-1)^2 = 1$ | $1/4 \times 1 = 1/4$ |
| $1$ | $2/4$ | $1 - 1 = 0$ | $(0)^2 = 0$ | $2/4 \times 0 = 0$ |
| $2$ | $1/4$ | $2 - 1 = 1$ | $(1)^2 = 1$ | $1/4 \times 1 = 1/4$ |
| **Sum** | $1$ | | | $\sum p_i (x_i - \mu)^2 = 2/4 = \mathbf{0.5}$ |

The **Variance** is $\sigma^2 = 0.5$.

---
## Mean And Variance Of Discrete Random Variables

The **Mean** and **Variance** are descriptive measures that summarize the central tendency and spread of a random variable's probability distribution.

### Definition

* **Mean ($\mu$ or Expected Value, $E(X)$):** The average value of the random variable over a very large number of trials. It represents the central location of the distribution.
* **Variance ($\sigma^2$ or $V(X)$):** The average squared deviation of the random variable's values from its mean. It measures the dispersion or spread of the distribution.

### Formula for a Discrete Random Variable ($X$)

| Measure | Formula |
| :--- | :--- |
| **Mean (Expected Value)** | $$\mu = E(X) = \sum x_i P(X=x_i)$$ |
| **Variance** | $$\sigma^2 = V(X) = \sum (x_i - \mu)^2 P(X=x_i)$$ |
| **Alternate Variance Formula** | $$\sigma^2 = E(X^2) - [E(X)]^2$$ |
| **where** | $E(X^2) = \sum x_i^2 P(X=x_i)$ |

### Explanation with Example: Rolling a Fair Die

**Experiment:** Rolling a single fair six-sided die.
**Random Variable ($X$):** The number appearing on the die.

| $x_i$ (Value) | $P(X=x_i) = p_i$ | $x_i p_i$ | $x_i^2$ | $x_i^2 p_i$ |
| :--- | :--- | :--- | :--- | :--- |
| **1** | $1/6$ | $1/6$ | 1 | $1/6$ |
| **2** | $1/6$ | $2/6$ | 4 | $4/6$ |
| **3** | $1/6$ | $3/6$ | 9 | $9/6$ |
| **4** | $1/6$ | $4/6$ | 16 | $16/6$ |
| **5** | $1/6$ | $5/6$ | 25 | $25/6$ |
| **6** | $1/6$ | $6/6$ | 36 | $36/6$ |
| **Sum** | $6/6 = 1$ | **$21/6$** | | **$91/6$** |

* **1. Calculate the Mean ($E(X)$):**
    $$E(X) = \sum x_i p_i = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = \mathbf{3.5}$$
    The expected number when rolling a fair die is $3.5$.

* **2. Calculate the Variance ($\sigma^2$):** We use the alternate formula, $\sigma^2 = E(X^2) - [E(X)]^2$.
    * First, calculate $E(X^2)$:
        $$E(X^2) = \sum x_i^2 p_i = \frac{1+4+9+16+25+36}{6} = \frac{91}{6}$$
    * Now, calculate the Variance:
        $$\sigma^2 = \frac{91}{6} - \left(\frac{21}{6}\right)^2$$
        $$\sigma^2 = \frac{91}{6} - \frac{441}{36} = \frac{91 \times 6}{36} - \frac{441}{36} = \frac{546 - 441}{36} = \frac{105}{36}$$
        $$\sigma^2 = \frac{35}{12} \approx \mathbf{2.9167}$$

---

## Example 3: Finding Constant in PMF

**Problem:** A random variable $X$ takes values $r = 1, 2, 3, \dots$ with a PMF $P(X=r) = \frac{\lambda^r}{r!}$. Given that the sum of probabilities is valid, find the value of $\lambda$.

**Key Principle (PMF Condition):** The sum of all probabilities must equal $1$.

$$\sum_{r=1}^{\infty} P(X=r) = 1$$

1.  **Set up the sum:**
    $$\sum_{r=1}^{\infty} \frac{\lambda^r}{r!} = 1$$
    This series is closely related to the Taylor series expansion of the exponential function, $e^x$:
    $$e^x = \sum_{r=0}^{\infty} \frac{x^r}{r!} = \frac{x^0}{0!} + \frac{x^1}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$$

2.  **Compare the PMF sum to the exponential series:**
    The sum $\sum_{r=1}^{\infty} \frac{\lambda^r}{r!}$ is the exponential series $e^\lambda$ **minus** the first term (where $r=0$):
    $$e^\lambda = \sum_{r=0}^{\infty} \frac{\lambda^r}{r!} = \frac{\lambda^0}{0!} + \sum_{r=1}^{\infty} \frac{\lambda^r}{r!} = 1 + \sum_{r=1}^{\infty} \frac{\lambda^r}{r!}$$

3.  **Substitute the PMF sum and solve for $\lambda$:**
    Since $\sum_{r=1}^{\infty} \frac{\lambda^r}{r!} = 1$, we substitute this back into the exponential equation:
    $$e^\lambda = 1 + 1$$
    $$e^\lambda = 2$$

4.  **Solve for $\lambda$ using the natural logarithm:**
    $$\lambda = \ln(2)$$

The value of the constant $\lambda$ is $\mathbf{\ln(2)}$. (Note: This type of PMF, $\frac{e^{-\lambda} \lambda^r}{r!}$, is the structure of the **Poisson Distribution**, and here the constant $e^{-\lambda}$ was implied in the problem statement by assuming the full PMF sum equals 1.)

**Example 4: Discrete Probability Distribution 

 A random variable $X$ has the following probability function values:

   * $P(X=0) = 0$
   * $P(X=1) = k$
   * $P(X=2) = 2k$
   * $P(X=3) = 2k$
   * $P(X=4) = 3k$
   * $P(X=5) = k^2$
   * $P(X=6) = 2k^2$
   * $P(X=7) = 7k^2 + k$

 **Find:**

 1.  The value of $k$.
 2.  $P(X < 6)$
 3.  $P(X \ge 6)$
 4.  $P(3 < X \le 6)$ (Note: The transcript solves for a specific range similar to this).


This problem requires using the fundamental properties of a **Discrete Probability Mass Function (PMF)** to first solve for the unknown constant $k$ and then calculate various probabilities.

---

## 1. Find the Value of $k$

The primary condition for any PMF is that the **sum of all probabilities must equal $1$** ($\sum P(X=x_i) = 1$).

1.  **Set up the equation using the PMF condition:**
    $$P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4) + P(X=5) + P(X=6) + P(X=7) = 1$$

2.  **Substitute the given expressions for the probabilities:**
    $$(0) + (k) + (2k) + (2k) + (3k) + (k^2) + (2k^2) + (7k^2 + k) = 1$$

3.  **Combine like terms (terms with $k$ and terms with $k^2$):**
    * $k$-terms: $k + 2k + 2k + 3k + k = 9k$
    * $k^2$-terms: $k^2 + 2k^2 + 7k^2 = 10k^2$

4.  **Form the quadratic equation:**
    $$10k^2 + 9k = 1$$
    $$10k^2 + 9k - 1 = 0$$

5.  **Solve the quadratic equation using factoring:**
    We look for factors of $10 \times (-1) = -10$ that sum to $9$ (which are $10$ and $-1$).
    $$10k^2 + 10k - k - 1 = 0$$
    $$10k(k + 1) - 1(k + 1) = 0$$
    $$(10k - 1)(k + 1) = 0$$

6.  **Determine possible values for $k$:**
    $$10k - 1 = 0 \implies k = \frac{1}{10}$$
    $$k + 1 = 0 \implies k = -1$$

7.  **Select the valid value for $k$:**
    Since all probabilities in a PMF must be non-negative ($P(X=x_i) \ge 0$), we must check the values:
    * If $k = -1$, then $P(X=1) = k = -1$. Since probability cannot be negative, $\mathbf{k \neq -1}$.
    * If $k = 1/10$, all probabilities are non-negative.

    The valid value of $k$ is $\mathbf{\frac{1}{10}}$ or $\mathbf{0.1}$.

---

## 2. Calculate $P(X < 6)$

The probability $P(X < 6)$ is the sum of probabilities for all values of $X$ strictly less than 6: $X=0, 1, 2, 3, 4, 5$.

$$P(X < 6) = P(0) + P(1) + P(2) + P(3) + P(4) + P(5)$$

Using the simplified sum from Step 3 of finding $k$: $9k - (P(6) + P(7))$.
Alternatively, using the expressions:
$$P(X < 6) = 0 + k + 2k + 2k + 3k + k^2 = 8k + k^2$$

Substitute $k = 1/10$:
$$P(X < 6) = 8\left(\frac{1}{10}\right) + \left(\frac{1}{10}\right)^2 = \frac{8}{10} + \frac{1}{100} = \frac{80}{100} + \frac{1}{100} = \mathbf{\frac{81}{100}}$$

---

## 3. Calculate $P(X \ge 6)$

The probability $P(X \ge 6)$ is the sum of probabilities for $X=6$ and $X=7$.

$$P(X \ge 6) = P(6) + P(7)$$
$$P(X \ge 6) = (2k^2) + (7k^2 + k) = 9k^2 + k$$

Alternatively, we can use the complement rule: $P(X \ge 6) = 1 - P(X < 6)$.
$$P(X \ge 6) = 1 - \frac{81}{100} = \mathbf{\frac{19}{100}}$$

*Verification (using $9k^2 + k$):*
$$9\left(\frac{1}{10}\right)^2 + \frac{1}{10} = \frac{9}{100} + \frac{10}{100} = \mathbf{\frac{19}{100}}$$

---

## 4. Calculate $P(3 < X \le 6)$

The probability $P(3 < X \le 6)$ includes values of $X$ strictly greater than 3 and less than or equal to 6: $X=4, 5, 6$.

$$P(3 < X \le 6) = P(4) + P(5) + P(6)$$
$$P(3 < X \le 6) = (3k) + (k^2) + (2k^2) = 3k + 3k^2$$

Substitute $k = 1/10$:
$$P(3 < X \le 6) = 3\left(\frac{1}{10}\right) + 3\left(\frac{1}{10}\right)^2$$
$$P(3 < X \le 6) = \frac{3}{10} + \frac{3}{100}$$
$$P(3 < X \le 6) = \frac{30}{100} + \frac{3}{100} = \mathbf{\frac{33}{100}}$$



**Example 5: Defective Bulbs 

 5 defective bulbs are accidentally mixed with 20 good ones. It is not possible to just look at a bulb and tell whether or not it is defective. Find the **probability distribution** of the number of defective bulbs if 4 bulbs are drawn at random from this lot.

This is a problem involving **combinations** to determine the probabilities, as the order in which the bulbs are drawn does not matter, and the problem fits the structure of a **Hypergeometric Distribution**.

Here is the step-by-step solution to find the probability distribution.

---

## 1. Define the Random Variable and Parameters

* **Total Bulbs ($N$):** $5 \text{ (defective)} + 20 \text{ (good)} = 25$ bulbs.
* **Total Defective Bulbs ($K$):** $5$.
* **Sample Size Drawn ($n$):** $4$ bulbs.
* **Random Variable ($X$):** The number of defective bulbs drawn in the sample of $4$.

The possible values for the random variable $X$ are the integers from **0 to 4** (since you can draw a minimum of 0 defective bulbs and a maximum of 4 defective bulbs, as you only draw 4 total).
$$X \in \{0, 1, 2, 3, 4\}$$

---

## 2. Calculate the Total Possible Cases ($n(S)$)

The total number of ways to draw 4 bulbs from 25 is given by the combination formula $N C_n$:

$$n(S) = \binom{25}{4} = \frac{25!}{4! (25-4)!} = \frac{25 \times 24 \times 23 \times 22}{4 \times 3 \times 2 \times 1}$$
$$n(S) = 25 \times 23 \times 22 = \mathbf{12,650}$$

---

## 3. Calculate the Probability Mass Function (PMF)

The probability of drawing $x$ defective bulbs (from the 5 defective ones) and $(4-x)$ good bulbs (from the 20 good ones) is calculated using the formula:
$$P(X=x) = \frac{\binom{\text{Defective}}{x} \times \binom{\text{Good}}{4-x}}{\binom{\text{Total}}{4}} = \frac{\binom{5}{x} \times \binom{20}{4-x}}{12,650}$$

| $x$ | $n(X=x)$ (Favorable Cases) | $P(X=x)$ (Probability) |
| :---: | :--- | :--- |
| **0** | $\binom{5}{0} \times \binom{20}{4} = 1 \times 4,845 = 4,845$ | $\frac{4,845}{12,650} \approx \mathbf{0.3830}$ |
| **1** | $\binom{5}{1} \times \binom{20}{3} = 5 \times 1,140 = 5,700$ | $\frac{5,700}{12,650} \approx \mathbf{0.4506}$ |
| **2** | $\binom{5}{2} \times \binom{20}{2} = 10 \times 190 = 1,900$ | $\frac{1,900}{12,650} \approx \mathbf{0.1502}$ |
| **3** | $\binom{5}{3} \times \binom{20}{1} = 10 \times 20 = 200$ | $\frac{200}{12,650} \approx \mathbf{0.0158}$ |
| **4** | $\binom{5}{4} \times \binom{20}{0} = 5 \times 1 = 5$ | $\frac{5}{12,650} \approx \mathbf{0.0004}$ |

---

## 4. Probability Distribution

The **Probability Distribution** of the number of defective bulbs ($X$) drawn is:

| $X$ (Number of Defective Bulbs) |       $P(X=x)$        |
| :-----------------------------: | :-------------------: |
|              **0**              |   $4,845 / 12,650$    |
|              **1**              |   $5,700 / 12,650$    |
|              **2**              |   $1,900 / 12,650$    |
|              **3**              |    $200 / 12,650$     |
|              **4**              |     $5 / 12,650$      |
|             **Sum**             | $12,650 / 12,650 = 1$ |


That's an excellent move! **Continuous Random Variables** are fundamentally different from discrete ones because they deal with ranges rather than distinct points, which is why we use integration instead of summation.

---

## 4. Continuous Random Variable Tools

A **Continuous Random Variable** ($X$) can take any value within a specific interval. Since there are infinitely many possible values, the probability of $X$ being *exactly* equal to a single point is zero. Instead, we calculate the probability that $X$ falls within a range using the **Probability Density Function (PDF)**.

### Probability Density Function (PDF)

The **Probability Density Function ($f(x)$)** is a curve that describes the relative likelihood of the variable taking on a certain value. The probability is represented by the **area under this curve** over a given interval.

* **Conditions for a function to be a PDF:**
    1.  **Non-Negativity:** The function value must be non-negative everywhere, as density cannot be negative.
        $$f(x) \ge 0 \quad \text{for all } x$$
    2.  **Total Area is 1:** The total area under the entire PDF curve must be equal to $1$, representing $100\%$ probability for the entire sample space.
        $$\int_{-\infty}^{\infty} f(x) \, dx = 1$$
        

### Probability in an Interval

The probability that the random variable $X$ lies between two values, $a$ and $b$, is calculated by finding the area under the PDF curve between those two points:

$$P(a < X < b) = \int_{a}^{b} f(x) \, dx$$

---

## Example 6: Finding Constant in PDF (Exponential)

**Problem:** Find the value of $C$ such that $f(x) = C e^{-x}$ for $0 \le x < \infty$ and $f(x)=0$ otherwise, is a valid PDF.

1.  **Apply the Total Area Condition:** Set the integral of the PDF over its domain equal to 1.
    $$\int_{-\infty}^{\infty} f(x) \, dx = 1$$
    Since $f(x)$ is non-zero only for $0 \le x < \infty$:
    $$\int_{0}^{\infty} C e^{-x} \, dx = 1$$

2.  **Solve the improper integral:**
    Factor out the constant $C$:
    $$C \int_{0}^{\infty} e^{-x} \, dx = 1$$

    Evaluate the integral, noting that $\int e^{-x} dx = -e^{-x}$:
    $$C \left[ -e^{-x} \right]_{0}^{\infty} = 1$$

    Apply the limits of integration:
    $$C \left( \lim_{t \to \infty} (-e^{-t}) - (-e^{-0}) \right) = 1$$

3.  **Evaluate the limits:**
    * $\lim_{t \to \infty} (-e^{-t}) = -e^{-\infty} = 0$
    * $(-e^{-0}) = -1$

    Substitute these values back:
    $$C \left( 0 - (-1) \right) = 1$$
    $$C (1) = 1$$
    $$\mathbf{C = 1}$$

---

## Example 7: Finding Constant & Probability in PDF (Polynomial)

**Problem:** A continuous R.V. $X$ has the PDF $f(x) = C x^2$ for $0 < x < 1$.

### 1. Find the value of the constant $C$.

1.  **Apply the Total Area Condition:**
    $$\int_{0}^{1} f(x) \, dx = 1$$
    $$\int_{0}^{1} C x^2 \, dx = 1$$

2.  **Solve the integral:**
    $$C \left[ \frac{x^3}{3} \right]_{0}^{1} = 1$$

3.  **Apply the limits:**
    $$C \left( \frac{(1)^3}{3} - \frac{(0)^3}{3} \right) = 1$$
    $$C \left( \frac{1}{3} - 0 \right) = 1$$
    $$\frac{C}{3} = 1$$
    $$\mathbf{C = 3}$$

### 2. Find the probability $P\left(\frac{1}{3} < X < \frac{1}{2}\right)$.

Now that we know $C=3$, the PDF is $f(x) = 3x^2$.

1.  **Set up the definite integral for the probability:**
    $$P\left(\frac{1}{3} < X < \frac{1}{2}\right) = \int_{1/3}^{1/2} 3x^2 \, dx$$

2.  **Solve the integral:**
    $$P = 3 \left[ \frac{x^3}{3} \right]_{1/3}^{1/2}$$
    $$P = \left[ x^3 \right]_{1/3}^{1/2}$$

3.  **Apply the limits:**
    $$P = \left(\frac{1}{2}\right)^3 - \left(\frac{1}{3}\right)^3$$
    $$P = \frac{1}{8} - \frac{1}{27}$$

4.  **Find a common denominator (LCM of 8 and 27 is 216):**
    $$P = \frac{1 \times 27}{216} - \frac{1 \times 8}{216}$$
    $$P = \frac{27 - 8}{216} = \mathbf{\frac{19}{216}}$$

The probability that $X$ falls between $1/3$ and $1/2$ is $\frac{19}{216}$.

