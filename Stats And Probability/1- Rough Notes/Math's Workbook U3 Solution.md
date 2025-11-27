#### 71. Write marginal and conditional distribution for continuous Random Variables.
---
For two jointly continuous random variables $X$ and $Y$ with a joint probability density function (pdf) $f(x,y)$:

1. Marginal Probability Density Functions:

The marginal pdf of $X$, denoted as $f_X(x)$ (or $g(x)$), is obtained by integrating the joint pdf over the entire range of $Y$:

$$f_X(x) = \int_{-\infty}^{\infty} f(x, y) \, dy$$

The marginal pdf of $Y$, denoted as $f_Y(y)$ (or $h(y)$), is obtained by integrating the joint pdf over the entire range of $X$:

$$f_Y(y) = \int_{-\infty}^{\infty} f(x, y) \, dx$$

2. Conditional Probability Density Functions:

The conditional pdf of $X$ given that $Y = y$ is defined as:

$$f(x|y) = \frac{f(x, y)}{f_Y(y)}, \quad \text{provided } f_Y(y) > 0$$

The conditional pdf of $Y$ given that $X = x$ is defined as:

$$f(y|x) = \frac{f(x, y)}{f_X(x)}, \quad \text{provided } f_X(x) > 0$$

---

#### 72. A continuous random variable $X$ has a p.d.f. $f(x)=3x^{2}$, $0\le x\le1.$ Find $a$ such that $P(X\le a)=P(X>a)$.

Step 1: Understand the Probability Condition

The total probability over the range $[0, 1]$ is equal to $1$.

Given $P(X \le a) = P(X > a)$, and knowing that $P(X \le a) + P(X > a) = 1$, we can deduce:

$$2 P(X \le a) = 1 \implies P(X \le a) = \frac{1}{2}$$

Step 2: Integrate the PDF

We need to calculate the cumulative probability up to $a$:

$$P(X \le a) = \int_{0}^{a} f(x) \, dx = \int_{0}^{a} 3x^2 \, dx$$

Step 3: Solve the Integral

$$\int_{0}^{a} 3x^2 \, dx = 3 \left[ \frac{x^3}{3} \right]_{0}^{a} = \left[ x^3 \right]_{0}^{a} = a^3$$

Step 4: Equate to 0.5

$$a^3 = \frac{1}{2}$$

$$a = \left(\frac{1}{2}\right)^{1/3} \text{ or } \sqrt[3]{0.5}$$

$a = \frac{1}{\sqrt[3]{2}} \approx 0.7937$

---
#### 73. State the Central Limit Theorem

Statement:

The Central Limit Theorem (CLT) states that if we take random samples of size $n$ from any population (regardless of the population's distribution shape) with a mean $\mu$ and a finite variance $\sigma^2$, the distribution of the sample means $\bar{X}$ will approach a Normal Distribution as the sample size $n$ becomes large (usually $n \ge 30$).

Mathematically, the standardized variable $Z$ converges to the standard normal distribution $N(0,1)$ as $n \to \infty$:

$$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)$$

---

#### 74. Assume that the pair of dice is thrown and the random variable $X$ is the sum of numbers that appears on two dice. Find the mean or the expectation of the random variable $X$.

**Step 1: Identify Sample Space and Random Variable $X$ (Sum)

When two dice are thrown, the total outcomes are $6 \times 6 = 36$.

The possible values for the sum $X$ range from $2$ ($1+1$) to $12$ ($6+6$).

**Step 2: Determine Probability $P(X)$ for each Sum**

$X=2$: (1,1) $\to 1/36$
$X=3$: (1,2), (2,1) $\to 2/36$
$X=4$: (1,3), (2,2), (3,1) $\to 3/36$
$X=5$: (1,4), (2,3), (3,2), (4,1) $\to 4/36$
$X=6$: (1,5), (2,4), (3,3), (4,2), (5,1) $\to 5/36$
$X=7$: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) $\to 6/36$
$X=8$: (2,6), (3,5), (4,4), (5,3), (6,2) $\to 5/36$
$X=9$: (3,6), (4,5), (5,4), (6,3) $\to 4/36$
$X=10$: (4,6), (5,5), (6,4) $\to 3/36$
$X=11$: (5,6), (6,5) $\to 2/36$
$X=12$: (6,6) $\to 1/36$


Step 3: Calculate Expectation $E[X] = \sum x \cdot P(x)$

$$E[X] = \frac{1}{36} [ (2\cdot1) + (3\cdot2) + (4\cdot3) + (5\cdot4) + (6\cdot5) + (7\cdot6) + (8\cdot5) + (9\cdot4) + (10\cdot3) + (11\cdot2) + (12\cdot1) ]$$

$$E[X] = \frac{1}{36} [ 2 + 6 + 12 + 20 + 30 + 42 + 40 + 36 + 30 + 22 + 12 ]$$

$$E[X] = \frac{252}{36} = 7$$

**Answer:** The mean (expectation) is **7**.

---
#### 75. Find the probability distribution for the number of doublets in the three throw of a pair of dice.

Step 1: Identify Parameters

This is a Binomial Distribution problem.

 **Experiment:** Throwing a pair of dice 3 times ($n=3$).

**Success:** Getting a "doublet" (same number on both dice).
Doublets: $\{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\}$
Number of successes: 6
Total outcomes in one throw: 36
**Probability of success ($p$):** $6/36 = 1/6$
**Probability of failure ($q$):** $1 - 1/6 = 5/6$
**Random Variable $X$:** Number of doublets (0, 1, 2, or 3).

Step 2: Calculate Probabilities using Binomial Formula

$$P(X=x) = \binom{n}{x} p^x q^{n-x}$$

For $X=0$ (No doublets):

$$P(0) = \binom{3}{0} \left(\frac{1}{6}\right)^0 \left(\frac{5}{6}\right)^3 = 1 \cdot 1 \cdot \frac{125}{216} = \frac{125}{216}$$
For $X=1$ (One doublet):

$$P(1) = \binom{3}{1} \left(\frac{1}{6}\right)^1 \left(\frac{5}{6}\right)^2 = 3 \cdot \frac{1}{6} \cdot \frac{25}{36} = \frac{75}{216}$$

- For $X=2$ (Two doublets):

$$P(2) = \binom{3}{2} \left(\frac{1}{6}\right)^2 \left(\frac{5}{6}\right)^1 = 3 \cdot \frac{1}{36} \cdot \frac{5}{6} = \frac{15}{216}$$

- For $X=3$ (Three doublets):

$$P(3) = \binom{3}{3} \left(\frac{1}{6}\right)^3 \left(\frac{5}{6}\right)^0 = 1 \cdot \frac{1}{216} \cdot 1 = \frac{1}{216}$$


**Step 3: Write the Probability Distribution Table**

|**X (Number of Doublets)**|**0**|**1**|**2**|**3**|
|---|---|---|---|---|
|**P(X)**|$\frac{125}{216}$|$\frac{75}{216}$|$\frac{15}{216}$|$\frac{1}{216}$|

---
#### 76. A continuous random variable $X$ has a p.d.f. $f(x)=3x^{2}$, $0<x<1$. Find $P(\frac{1}{3}\le x\le\frac{2}{3})$.

Step 1: Set up the Definite Integral

We need to integrate the probability density function $f(x)$ from lower limit $1/3$ to upper limit $2/3$.

$$P\left(\frac{1}{3} \le X \le \frac{2}{3}\right) = \int_{1/3}^{2/3} 3x^2 \, dx$$

Step 2: Solve the Integral

$$\int 3x^2 \, dx = x^3$$

Applying limits:

$$\left[ x^3 \right]_{1/3}^{2/3}$$

Step 3: Calculate Values

$$= \left(\frac{2}{3}\right)^3 - \left(\frac{1}{3}\right)^3$$

$$= \frac{8}{27} - \frac{1}{27}$$

$$= \frac{7}{27}$$

**Answer:** $\frac{7}{27} \approx 0.259$

---
#### 77. The joint probability distribution of two random variables $X$ and $Y$ is given by: $P(X = 0, Y = 1)$, $P(X = 1, Y = -1) = 1/3$ and $P(X=1, Y=1)=1/3$. Find marginal distributions of $X$ and $Y$, and the conditional probability distribution of $X$ given $Y=1$.


Step 1: Determine the missing probability.

The sum of all joint probabilities must equal 1.

Given:

- $P(1, -1) = 1/3$
    
- $P(1, 1) = 1/3$
    
- Let $P(0, 1) = p$
    

Sum: $p + 1/3 + 1/3 = 1 \implies p = 1/3$.

So, $P(X=0, Y=1) = 1/3$.

**Step 2: Construct the Joint Probability Table.**

|**X \ Y**|**-1**|**1**|**Marginal P(X)**|
|---|---|---|---|
|**0**|$0$|$1/3$|**$1/3$**|
|**1**|$1/3$|$1/3$|**$2/3$**|
|**Marginal P(Y)**|**$1/3$**|**$2/3$**|**$1$**|

**Step 3: Marginal Distributions.**

- **Marginal Distribution of X:**
    
    - $P(X=0) = 1/3$
        
    - $P(X=1) = 2/3$
        
- **Marginal Distribution of Y:**
    
    - $P(Y=-1) = 1/3$
        
    - $P(Y=1) = 2/3$
        

Step 4: Conditional Probability Distribution of $X$ given $Y=1$.

Formula: $P(X=x | Y=1) = \frac{P(X=x, Y=1)}{P(Y=1)}$

- For $X=0$:
    
    $$P(X=0 | Y=1) = \frac{1/3}{2/3} = \frac{1}{2}$$
    
- For $X=1$:
    
    $$P(X=1 | Y=1) = \frac{1/3}{2/3} = \frac{1}{2}$$
    

---
#### 78. A petrol pump is supplied with petrol once a day. If its daily volume of sales ($x$) in thousands of liters is distributed by $f(x)=5(1-x)^{4}, 0\le x\le1$, what must be the capacity of its tank in order that the probability that its supply will be exhausted in a given day shall be $0.01$?


Step 1: Define the condition.

Let $c$ be the tank capacity. The supply is exhausted if sales $X$ exceed capacity $c$.

We need to find $c$ such that $P(X > c) = 0.01$.

Step 2: Set up the integral.

$$P(X > c) = \int_{c}^{1} f(x) \, dx = 0.01$$

$$\int_{c}^{1} 5(1-x)^4 \, dx = 0.01$$

Step 3: Solve the integral.

Let $u = 1-x$, then $du = -dx$.

When $x=c, u=1-c$. When $x=1, u=0$.

Integral becomes:

$$\int_{1-c}^{0} 5u^4 (-du) = \int_{0}^{1-c} 5u^4 \, du$$

$$= \left[ u^5 \right]_{0}^{1-c} = (1-c)^5$$

Step 4: Solve for $c$.

$$(1-c)^5 = 0.01$$

$$1-c = (0.01)^{1/5}$$

$$1-c \approx 0.398$$

$$c \approx 1 - 0.398 = 0.602$$

**Answer:** The capacity must be approximately **602 liters** (since unit is thousands of liters, $0.602 \times 1000$).

---
####  79.If a random variable $X$ has density function $f(x) = 1/4$ for $-2 < x < 2$ (and 0 elsewhere). Obtain i. P(|X|>1) and ii. P(2X+3>5)

 **1. Find P(∣X∣>1)**

The inequality ∣X∣>1 means the distance from 0 is greater than 1. This splits into two regions:

1. X<−1
    
2. X>1
    

We need to integrate the probability density function f(x)=41​ over the valid range of X (which is between −2 and 2).

**Step 1: Define the limits**

- For X<−1: The valid range within the domain is −2<x<−1.
    
- For X>1: The valid range within the domain is 1<x<2.
    

**Step 2: Set up the integrals**

P(∣X∣>1)=P(−2<X<−1)+P(1<X<2)

P(∣X∣>1)=∫−2−1​41​dx+∫12​41​dx

**Step 3: Solve the integrals**

=41​[x]−2−1​+41​[x]12​

=41​(−1−(−2))+41​(2−1)

=41​(1)+41​(1)

=41​+41​=42​=0.5

**Answer:** P(∣X∣>1)=0.5

---

**2. Find P(2X+3>5)**

**Step 1: Simplify the inequality** We need to isolate X:

2X+3>5

2X>5−3

2X>2

X>1

**Step 2: Define the limits** We need to find the probability that X>1. Given the domain of X is −2<x<2, the valid region for this condition is 1<x<2.

**Step 3: Set up the integral**

P(X>1)=∫12​f(x)dx

P(X>1)=∫12​41​dx

**Step 4: Solve the integral**

=41​[x]12​

=41​(2−1)

=41​(1)=0.25

**Answer:** P(2X+3>5)=0.25

---
####  80. If $X$ and $Y$ are two random variables having the joint density function:

$$f(x,y)=\begin{cases}\frac{1}{8}(6-x-y)&0\le x<2, 2\le y<4\\ 0&elsewhere\end{cases}$$

Find: i. $P(X<1 \cap Y<3)$, ii. $P(X+Y<3)$, iii. $P(X<1 | Y<3)$

**Solution:**

i. Find $P(X<1 \cap Y<3)$

This is the integral over the rectangle $0 \le x < 1$ and $2 \le y < 3$.

$$P = \int_{2}^{3} \int_{0}^{1} \frac{1}{8}(6-x-y) \, dx \, dy$$

$$= \frac{1}{8} \int_{2}^{3} \left[ 6x - \frac{x^2}{2} - xy \right]_{0}^{1} \, dy$$

$$= \frac{1}{8} \int_{2}^{3} \left( 6 - 0.5 - y \right) \, dy = \frac{1}{8} \int_{2}^{3} (5.5 - y) \, dy$$

$$= \frac{1}{8} \left[ 5.5y - \frac{y^2}{2} \right]_{2}^{3}$$

$$= \frac{1}{8} \left[ (16.5 - 4.5) - (11 - 2) \right] = \frac{1}{8} [12 - 9] = \frac{3}{8}$$

ii. Find $P(X+Y < 3)$

Region defined by $x \ge 0$, $y \ge 2$ and $x+y < 3$ (which means $x < 3-y$).

Since $y$ must be at least 2, and $x$ must be positive, $y$ can range from 2 to 3. (If $y>3$, $x$ would be negative).

$$P = \int_{2}^{3} \int_{0}^{3-y} \frac{1}{8}(6-x-y) \, dx \, dy$$

Inner integral w.r.t $x$:

$$\left[ 6x - \frac{x^2}{2} - xy \right]_{0}^{3-y} = 6(3-y) - \frac{(3-y)^2}{2} - y(3-y)$$

$$= (3-y) \left[ 6 - \frac{3-y}{2} - y \right] = (3-y) \left[ \frac{12 - 3 + y - 2y}{2} \right] = \frac{1}{2}(3-y)(9-y)$$

Now integrate w.r.t $y$ from 2 to 3:

$$\frac{1}{16} \int_{2}^{3} (27 - 3y - 9y + y^2) \, dy = \frac{1}{16} \int_{2}^{3} (y^2 - 12y + 27) \, dy$$

$$= \frac{1}{16} \left[ \frac{y^3}{3} - 6y^2 + 27y \right]_{2}^{3}$$

Values at 3: $(9 - 54 + 81) = 36$

Values at 2: $(8/3 - 24 + 54) = 32.66... = 98/3$

Result: $\frac{1}{16} (36 - 32.66) = \frac{1}{16} (\frac{108}{3} - \frac{98}{3}) = \frac{1}{16} \cdot \frac{10}{3} = \frac{5}{24}$


iii. Find $P(X<1 | Y<3)$

$$P(X<1 | Y<3) = \frac{P(X<1 \cap Y<3)}{P(Y<3)}$$

We found the numerator in part (i): $3/8$.

We need $P(Y<3)$.

$$P(Y<3) = \int_{2}^{3} \int_{0}^{2} \frac{1}{8}(6-x-y) \, dx \, dy$$

Inner integral ($0$ to $2$):

$$\left[ 6x - \frac{x^2}{2} - xy \right]_{0}^{2} = 12 - 2 - 2y = 10 - 2y$$

Outer integral ($2$ to $3$):

$$\frac{1}{8} \int_{2}^{3} (10 - 2y) \, dy = \frac{1}{8} \left[ 10y - y^2 \right]_{2}^{3}$$

$$= \frac{1}{8} [ (30-9) - (20-4) ] = \frac{1}{8} [ 21 - 16 ] = \frac{5}{8}$$

Calculation:

$$\frac{3/8}{5/8} = \frac{3}{5}$$

---
#### 81. Five defective bulbs are accidentally mixed with twenty good ones. Find the probability distribution of the number of defective bulbs, if four bulbs are drawn at random.

**Step 1: Identify Parameters.**

- Total bulbs = 25

- Defective (D) = 5

- Good (G) = 20

- Draws (n) = 4

- Let $X$ = number of defective bulbs drawn ($0, 1, 2, 3, 4$).

- Total ways to draw 4 from 25: $N = \binom{25}{4} = \frac{25 \cdot 24 \cdot 23 \cdot 22}{4 \cdot 3 \cdot 2 \cdot 1} = 12,650$.


Step 2: Calculate Probability for each $X$.

Formula: $P(X=x) = \frac{\binom{5}{x} \binom{20}{4-x}}{12650}$

- X = 0:

$$P(0) = \frac{\binom{5}{0} \binom{20}{4}}{12650} = \frac{1 \cdot 4845}{12650} \approx 0.383$$

- X = 1:

$$P(1) = \frac{\binom{5}{1} \binom{20}{3}}{12650} = \frac{5 \cdot 1140}{12650} = \frac{5700}{12650} \approx 0.451$$

- X = 2:

$$P(2) = \frac{\binom{5}{2} \binom{20}{2}}{12650} = \frac{10 \cdot 190}{12650} = \frac{1900}{12650} \approx 0.150$$

- X = 3:

$$P(3) = \frac{\binom{5}{3} \binom{20}{1}}{12650} = \frac{10 \cdot 20}{12650} = \frac{200}{12650} \approx 0.016$$

- X = 4:

$$P(4) = \frac{\binom{5}{4} \binom{20}{0}}{12650} = \frac{5 \cdot 1}{12650} \approx 0.0004$$


**Distribution Table:**

|**X**|**0**|**1**|**2**|**3**|**4**|
|---|---|---|---|---|---|
|**P(X)**|$\frac{4845}{12650}$|$\frac{5700}{12650}$|$\frac{1900}{12650}$|$\frac{200}{12650}$|$\frac{5}{12650}$|

---
#### 82. If $X$ and $Y$ are two random variables having the joint probability mass function $p(x,y)=\frac{1}{27}(2x+y)$ for $x, y = 0, 1, 2$. Find the conditional distribution of $Y$ for $X = x$.

**Solution:**

Step 1: Find the Marginal Distribution of $X$, $P_X(x)$.

$P_X(x) = \sum_{y=0}^{2} p(x, y)$

$$P_X(x) = \frac{1}{27} [(2x+0) + (2x+1) + (2x+2)]$$

$$P_X(x) = \frac{1}{27} [6x + 3] = \frac{3(2x+1)}{27} = \frac{2x+1}{9}$$

Step 2: Find Conditional Distribution $P(Y=y | X=x)$.

$$P(y|x) = \frac{p(x,y)}{P_X(x)}$$

$$P(y|x) = \frac{\frac{1}{27}(2x+y)}{\frac{2x+1}{9}}$$

$$P(y|x) = \frac{2x+y}{27} \cdot \frac{9}{2x+1}$$

$$P(y|x) = \frac{2x+y}{3(2x+1)}$$

**Answer:** The conditional distribution is $P(Y=y | X=x) = \frac{2x+y}{3(2x+1)}$ for $y=0,1,2$.

---
#### 83. If the pdf of continuous random variable $X$ is $f(x)=kx^{2}(1-x)$ for $0<x<1$. Calculate the value of $k$ and mean for $X$.

**Solution:**

Step 1: Find $k$.

Total probability must be 1.

$$\int_{0}^{1} kx^2(1-x) \, dx = 1$$

$$k \int_{0}^{1} (x^2 - x^3) \, dx = 1$$

$$k \left[ \frac{x^3}{3} - \frac{x^4}{4} \right]_{0}^{1} = 1$$

$$k \left( \frac{1}{3} - \frac{1}{4} \right) = 1 \implies k \left( \frac{1}{12} \right) = 1$$

$$k = 12$$

Step 2: Find the Mean $E[X]$.

$$E[X] = \int_{0}^{1} x \cdot f(x) \, dx$$

$$E[X] = \int_{0}^{1} x \cdot 12x^2(1-x) \, dx$$

$$E[X] = 12 \int_{0}^{1} (x^3 - x^4) \, dx$$

$$E[X] = 12 \left[ \frac{x^4}{4} - \frac{x^5}{5} \right]_{0}^{1}$$

$$E[X] = 12 \left( \frac{1}{4} - \frac{1}{5} \right) = 12 \left( \frac{5-4}{20} \right) = 12 \left( \frac{1}{20} \right)$$

$$E[X] = \frac{12}{20} = \frac{3}{5}$$

**Answer:** $k = 12$, Mean $= 0.6$

---
### 84 Suppose the p.d.f of a continuous random variable $X$ is defined as

$$f(x)=\begin{cases}1+x,&-1<x<0\\ 1-x,&0\le x<1\end{cases}$$

Find the cumulative distribution function (c.d.f) $F(x)$.

**Solution:**

The Cumulative Distribution Function (CDF) is defined as $F(x) = \int_{-\infty}^{x} f(t) \, dt$. We calculate this for each interval.

1. For $x \le -1$:
    
    The probability density is 0.
    
    $$F(x) = 0$$
    
2. For $-1 < x \le 0$:
    
    We integrate $1+t$ from $-1$ to $x$.
    
    $$F(x) = \int_{-1}^{x} (1+t) \, dt = \left[ t + \frac{t^2}{2} \right]_{-1}^{x}$$
    
    $$= \left( x + \frac{x^2}{2} \right) - \left( -1 + \frac{1}{2} \right) = x + \frac{x^2}{2} + \frac{1}{2}$$
    
    $$= \frac{1}{2}(x^2 + 2x + 1) = \frac{1}{2}(x+1)^2$$
    
3. For $0 < x < 1$:
    
    We add the full probability from the previous interval ($F(0)$) plus the integral of the current interval.
    
    From step 2, $F(0) = \frac{1}{2}(0+1)^2 = 0.5$.
    
    $$F(x) = 0.5 + \int_{0}^{x} (1-t) \, dt$$
    
    $$= 0.5 + \left[ t - \frac{t^2}{2} \right]_{0}^{x} = 0.5 + x - \frac{x^2}{2}$$
    
4. For $x \ge 1$:
    
    The total probability is accumulated.
    
    $$F(x) = 1$$
    

Answer:

$$F(x) = \begin{cases} 0 & x \le -1 \\ \frac{1}{2}(x+1)^2 & -1 < x \le 0 \\ \frac{1}{2} + x - \frac{x^2}{2} & 0 < x < 1 \\ 1 & x \ge 1 \end{cases}$$

---

#### 85 A random variable $X$ has the following probability mass function (values involving $c$).

|**X**|**0**|**1**|**2**|
|---|---|---|---|
|**P(X)**|$3c^3$|$4c - 10c^2$|$5c - 1$|

Tasks:

i. Find $c$.

ii. Evaluate $P(X<2)$, $P(2X+3\ge5)$, and $P(1<X\le2)$.

---
###### Step 1: Find the value of $c$

For a valid probability distribution, the sum of all probabilities must equal 1.

$$\sum P(X) = 1$$

$$P(0) + P(1) + P(2) = 1$$

$$3c^3 + (4c - 10c^2) + (5c - 1) = 1$$

Rearrange the terms into a standard cubic equation form:

$$3c^3 - 10c^2 + 9c - 1 = 1$$

$$3c^3 - 10c^2 + 9c - 2 = 0$$

Solve for $c$:

We look for integer or rational roots. Let's test $c=1$:

$$3(1)^3 - 10(1)^2 + 9(1) - 2 = 3 - 10 + 9 - 2 = 0$$

Since $c=1$ is a root, $(c-1)$ is a factor.

Now, we factor the cubic equation $(3c^3 - 10c^2 + 9c - 2)$ by dividing by $(c-1)$:

The resulting quadratic is $3c^2 - 7c + 2$.

So, $(c-1)(3c^2 - 7c + 2) = 0$.

Factor the quadratic $3c^2 - 7c + 2$:

$$(3c - 1)(c - 2) = 0$$

The possible values for $c$ are **$1, 2, \text{ and } \frac{1}{3}$**.

Validate $c$:

Probabilities $P(X)$ must be between 0 and 1.

- **If $c = 1$:** $P(2) = 5(1) - 1 = 4$ (Invalid, probability > 1).
    
- **If $c = 2$:** $P(2) = 5(2) - 1 = 9$ (Invalid).
    
- **If $c = 1/3$:**
    
    - $P(0) = 3(1/3)^3 = 3(1/27) = 1/9$
        
    - $P(1) = 4(1/3) - 10(1/3)^2 = 4/3 - 10/9 = 12/9 - 10/9 = 2/9$
        
    - $P(2) = 5(1/3) - 1 = 5/3 - 3/3 = 2/3$ (which is $6/9$)
        
    - **Sum:** $1/9 + 2/9 + 6/9 = 9/9 = 1$. (Valid)
        

**Therefore, $c = \frac{1}{3}$.**

The Probability Distribution Table is:

|**X**|**0**|**1**|**2**|
|---|---|---|---|
|**P(X)**|**1/9**|**2/9**|**6/9 (or 2/3)**|

---

#### **Step 2: Evaluate the Probabilities**

A. Find $P(X < 2)$

This includes all values of $X$ strictly less than 2 ($X=0$ and $X=1$).

$$P(X < 2) = P(0) + P(1)$$

$$P(X < 2) = \frac{1}{9} + \frac{2}{9} = \frac{3}{9}$$

Answer: $\frac{1}{3}$

B. Find $P(2X + 3 \ge 5)$

First, solve the inequality for $X$:

$$2X \ge 5 - 3$$

$$2X \ge 2$$

$$X \ge 1$$

This includes values $X=1$ and $X=2$.

$$P(X \ge 1) = P(1) + P(2)$$

$$P(X \ge 1) = \frac{2}{9} + \frac{6}{9} = \frac{8}{9}$$

Answer: $\frac{8}{9}$

C. Find $P(1 < X \le 2)$

This requires $X$ to be strictly greater than 1 and less than or equal to 2. The only integer value in the table that satisfies this is $X=2$.

$$P(1 < X \le 2) = P(2)$$

$$P(2) = \frac{6}{9} = \frac{2}{3}$$

Answer: $\frac{2}{3}$

---

#### 86. A random variable $X$ is distributed at random between the values $0$ and $1$. Its probability density function is $f(x)=kx^{2}(1-x^{3})$. Find the value of $k$, find its mean and variance.

**Solution:**

1. Find $k$:

$$\int_{0}^{1} k x^2 (1 - x^3) \, dx = 1$$

$$k \int_{0}^{1} (x^2 - x^5) \, dx = 1$$

$$k \left[ \frac{x^3}{3} - \frac{x^6}{6} \right]_{0}^{1} = 1$$

$$k \left( \frac{1}{3} - \frac{1}{6} \right) = 1 \implies k \left( \frac{1}{6} \right) = 1$$

$$k = 6$$

2. Find Mean ($\mu$):

$$E[X] = \int_{0}^{1} x \cdot f(x) \, dx = \int_{0}^{1} 6x(x^2 - x^5) \, dx$$

$$= 6 \int_{0}^{1} (x^3 - x^6) \, dx$$

$$= 6 \left[ \frac{x^4}{4} - \frac{x^7}{7} \right]_{0}^{1} = 6 \left( \frac{1}{4} - \frac{1}{7} \right)$$

$$= 6 \left( \frac{7-4}{28} \right) = 6 \left( \frac{3}{28} \right) = \frac{18}{28} = \frac{9}{14}$$

Mean $\mu \approx 0.643$

3. Find Variance ($\sigma^2$):

First, find $E[X^2]$:

$$E[X^2] = \int_{0}^{1} x^2 \cdot f(x) \, dx = \int_{0}^{1} 6x^2(x^2 - x^5) \, dx$$

$$= 6 \int_{0}^{1} (x^4 - x^7) \, dx$$

$$= 6 \left[ \frac{x^5}{5} - \frac{x^8}{8} \right]_{0}^{1} = 6 \left( \frac{1}{5} - \frac{1}{8} \right)$$

$$= 6 \left( \frac{8-5}{40} \right) = 6 \left( \frac{3}{40} \right) = \frac{18}{40} = \frac{9}{20}$$

Variance formula: $Var(X) = E[X^2] - (E[X])^2$

$$Var(X) = \frac{9}{20} - \left( \frac{9}{14} \right)^2$$

$$= 0.45 - \frac{81}{196} \approx 0.45 - 0.4132$$

$$Var(X) \approx 0.0368$$

(In fraction: $9/245$)

---

####  87. Let $X$ and $Y$ be jointly distributed with pdf $f(x,y) = \frac{1}{4}(1+xy)$ for $|x|<1,|y|<1$. Show that $X$ and $Y$ are not independent but $X^{2}$ and $Y^{2}$ are independent.


1. Show $X$ and $Y$ are Dependent:

For independence, $f(x,y)$ must equal $f_X(x) \cdot f_Y(y)$.

Find marginal $f_X(x)$:

$$f_X(x) = \int_{-1}^{1} \frac{1}{4}(1+xy) \, dy = \frac{1}{4} \left[ y + \frac{xy^2}{2} \right]_{-1}^{1}$$

$$= \frac{1}{4} \left[ (1 + x/2) - (-1 + x/2) \right] = \frac{1}{4}(2) = \frac{1}{2}$$

Similarly, $f_Y(y) = 1/2$.

Product of marginals: $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.

Since $\frac{1}{4} \neq \frac{1}{4}(1+xy)$ (unless $xy=0$), $X$ and $Y$ are NOT independent.

2. Show $X^2$ and $Y^2$ are Independent:

Consider the joint cumulative distribution of $U=X^2$ and $V=Y^2$:

$P(X^2 \le u, Y^2 \le v) = P(-\sqrt{u} < X < \sqrt{u}, -\sqrt{v} < Y < \sqrt{v})$

$$= \int_{-\sqrt{v}}^{\sqrt{v}} \int_{-\sqrt{u}}^{\sqrt{u}} \frac{1}{4}(1+xy) \, dx \, dy$$

$$= \frac{1}{4} \left( \int \int 1 \, dx dy + \int \int xy \, dx dy \right)$$

The integral of $xy$ over a region symmetric about the origin is 0.

$$= \frac{1}{4} \int_{-\sqrt{v}}^{\sqrt{v}} \int_{-\sqrt{u}}^{\sqrt{u}} 1 \, dx \, dy$$

$$= \frac{1}{4} (2\sqrt{u})(2\sqrt{v}) = \sqrt{u}\sqrt{v}$$

Since the joint probability $F(u,v) = \sqrt{u}\sqrt{v}$ factors into a function of $u$ only ($\sqrt{u}$) and $v$ only ($\sqrt{v}$), $X^2$ and $Y^2$ are independent.

---

#### 88. The joint probability density function of $(X,Y)$ is $f(x,y)=2$ for $0\le x<1, 0<y<x$.

**Solution:**

**i. Marginal density functions:**

- $X$ (Integrate out $y$):
    
    The limits for $y$ are $0$ to $x$.
    
    $$f_X(x) = \int_{0}^{x} 2 \, dy = 2[y]_{0}^{x} = 2x, \quad 0 \le x < 1$$
    
- $Y$ (Integrate out $x$):
    
    Since $y < x < 1$, the limits for $x$ are $y$ to $1$.
    
    $$f_Y(y) = \int_{y}^{1} 2 \, dx = 2[x]_{y}^{1} = 2(1-y), \quad 0 < y < 1$$
    

**ii. Conditional density functions:**

- $f(y|x)$:
    
    $$f(y|x) = \frac{f(x,y)}{f_X(x)} = \frac{2}{2x} = \frac{1}{x}, \quad 0 < y < x$$
    
- $f(x|y)$:
    
    $$f(x|y) = \frac{f(x,y)}{f_Y(y)} = \frac{2}{2(1-y)} = \frac{1}{1-y}, \quad y < x < 1$$
    

---

#### 89. A random variable $X$ has a given probability distribution involving $k$.

|**X**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|---|
|P(x)|0|$k$|$2k$|$2k$|$3k$|$k^2$|$2k^2$|$7k^2+k$|

**Solution:**

i. Find $k$:

Sum of probabilities must equal 1.

$$\sum P(x) = k + 2k + 2k + 3k + k^2 + 2k^2 + (7k^2+k) = 1$$

$$10k^2 + 9k = 1 \implies 10k^2 + 9k - 1 = 0$$

Factor the quadratic: $(10k - 1)(k + 1) = 0$.

Possible roots: $k = 0.1$ or $k = -1$. Since probability cannot be negative, $k = 0.1$.

**ii. Evaluate:**

- $P(X < 6)$:
    
    Sum of probabilities from $X=0$ to $X=5$. Alternatively, $1 - P(X \ge 6)$.
    
    $$P(X \ge 6) = P(6) + P(7) = 2k^2 + (7k^2+k) = 9k^2 + k$$
    
    Using $k=0.1$: $9(0.01) + 0.1 = 0.09 + 0.1 = 0.19$.
    
    $$P(X < 6) = 1 - 0.19 = 0.81$$
    
- $P(3 < X \le 6)$:
    
    Includes $X=4, 5, 6$.
    
    $$P(4) + P(5) + P(6) = 3k + k^2 + 2k^2 = 3k + 3k^2$$
    
    $$= 3(0.1) + 3(0.01) = 0.3 + 0.03 = 0.33$$
    

**iii. Find minimum $x$ so that $P(X \le x) > 1/2$:**

Calculate Cumulative Probabilities (CDF):

- $P(X \le 0) = 0$
    
- $P(X \le 1) = 0.1$
    
- $P(X \le 2) = 0.1 + 0.2 = 0.3$
    
- $P(X \le 3) = 0.3 + 0.2 = 0.5$ (Exactly 1/2)
    
- $P(X \le 4) = 0.5 + 0.3 = 0.8$ (Greater than 1/2)
    

The minimum $x$ where the cumulative sum is strictly _greater_ than $1/2$ is **$x = 4$**.

---

####  90. Joint distribution of $X$ and $Y$ is given by $f(x,y) = 4xye^{-(x^{2}+y^{2})}; x \ge 0, y\ge0$. Test whether $X$ and $Y$ are independent. Find the conditional density of $X$ given $Y=y$.

**1. Test for Independence:

Can $f(x,y)$ be written as $g(x)h(y)$?

$$f(x,y) = 4xy e^{-x^2} e^{-y^2} = (2x e^{-x^2}) \cdot (2y e^{-y^2})$$

Let $g(x) = 2x e^{-x^2}$ and $h(y) = 2y e^{-y^2}$.

Since the joint PDF factors perfectly into a function of $x$ and a function of $y$, and the limits ($x \ge 0, y \ge 0$) do not depend on each other:

Yes, $X$ and $Y$ are Independent.

**2. Find Conditional Density $f(x|y)$:

Formula: $f(x|y) = \frac{f(x,y)}{f_Y(y)}$.

Since $X$ and $Y$ are independent, the conditional density of $X$ given $Y$ is simply the marginal density of $X$.

$$f(x|y) = f_X(x) = 2x e^{-x^2}, \quad x \ge 0$$