**1. A random variable X has the following distribution:**

|**X**|**-2**|**-1**|**0**|**1**|**2**|**3**|
|---|---|---|---|---|---|---|
|**P(X)**|**0.1**|**K**|**0.2**|**2K**|**0.3**|**K**|

**Calculate the value of K, mean and variance.**

**Solution:**

Step 1: Calculate K

The sum of probabilities for a probability distribution must equal 1.

$$\sum P(X) = 1$$

$$0.1 + K + 0.2 + 2K + 0.3 + K = 1$$

$$0.6 + 4K = 1$$

$$4K = 1 - 0.6$$

$$4K = 0.4 \implies K = 0.1$$

Step 2: Calculate Mean ($E[X]$)

Using $K=0.1$, the probabilities are:

$P(-2)=0.1, P(-1)=0.1, P(0)=0.2, P(1)=0.2, P(2)=0.3, P(3)=0.1$.

$$E[X] = \sum x P(x)$$

$$E[X] = (-2)(0.1) + (-1)(0.1) + (0)(0.2) + (1)(0.2) + (2)(0.3) + (3)(0.1)$$

$$E[X] = -0.2 - 0.1 + 0 + 0.2 + 0.6 + 0.3$$

$$E[X] = 0.8$$

Step 3: Calculate Variance ($Var(X)$)

$$Var(X) = E[X^2] - (E[X])^2$$

First, find $E[X^2] = \sum x^2 P(x)$:

$$E[X^2] = (-2)^2(0.1) + (-1)^2(0.1) + (0)^2(0.2) + (1)^2(0.2) + (2)^2(0.3) + (3)^2(0.1)$$

$$E[X^2] = 4(0.1) + 1(0.1) + 0 + 1(0.2) + 4(0.3) + 9(0.1)$$

$$E[X^2] = 0.4 + 0.1 + 0 + 0.2 + 1.2 + 0.9 = 2.8$$

Now, Variance:

$$Var(X) = 2.8 - (0.8)^2 = 2.8 - 0.64 = 2.16$$

**Answer:** $K = 0.1$, Mean $= 0.8$, Variance $= 2.16$.

---

**2. A die is tossed twice. A 'success' is getting an odd number on a random basis. Find the variance of the number of successes.**

Solution:

This is a Binomial Distribution problem where $n$ is the number of trials and $p$ is the probability of success.

- Number of trials ($n$) = 2
    
- Probability of success (odd number: 1, 3, 5) $p = \frac{3}{6} = 0.5$
    
- Probability of failure $q = 1 - p = 0.5$
    

The Variance of a binomial distribution is given by:

$$Var(X) = npq$$

$$Var(X) = 2 \times 0.5 \times 0.5$$

$$Var(X) = 0.5$$

**Answer:** Variance $= 0.5$.

---

**3. Find the probability of drawing a card from a well shuffled pack such that the drawn card is either a king or a queen?**

**Solution:**

- Total cards in a pack ($n(S)$) = 52
    
- Number of Kings = 4
    
- Number of Queens = 4
    
- Event E: Card is King OR Queen. Since these are mutually exclusive events:
    
    $$n(E) = 4 + 4 = 8$$
    

$$P(E) = \frac{n(E)}{n(S)} = \frac{8}{52}$$

Dividing by 4:

$$P(E) = \frac{2}{13}$$

**Answer:** Probability is $\frac{2}{13}$.

---

**4. A bag contains 15 red and 5 blue balls. Without the replacement of the balls, two balls are drawn from a bag one after the other. What is the probability of picking both the balls as red?**

**Solution:**

- Total balls = $15 (\text{Red}) + 5 (\text{Blue}) = 20$.
    
- Probability of first ball being Red ($P(R_1)$):
    
    $$P(R_1) = \frac{15}{20} = \frac{3}{4}$$
    
- Since there is **no replacement**, there are now 19 balls total, and 14 Red balls left.
    
- Probability of second ball being Red ($P(R_2 | R_1)$):
    
    $$P(R_2 | R_1) = \frac{14}{19}$$
    

Total Probability:

$$P(\text{Both Red}) = P(R_1) \times P(R_2 | R_1) = \frac{3}{4} \times \frac{14}{19}$$

$$P(\text{Both Red}) = \frac{3 \times 7}{2 \times 19} = \frac{21}{38}$$

**Answer:** Probability is $\frac{21}{38}$.

---

**5. A two-dimensional random variable (X, Y) have a bivariate distribution given by $P(x=x, Y=y) = \frac{x^2+y}{32}$, for $x = 0,1,2,3$ and $y = 0,1$. Find the marginal distribution of X and Y.**

**Solution:**

I. Marginal Distribution of X ($P_X(x)$):

We sum the joint probability over all values of y ($y=0, 1$).

$$P_X(x) = \sum_{y=0}^{1} \frac{x^2+y}{32}$$

$$P_X(x) = \frac{x^2+0}{32} + \frac{x^2+1}{32} = \frac{2x^2+1}{32}$$

For $x = 0, 1, 2, 3$.

- $P_X(0) = 1/32$
    
- $P_X(1) = 3/32$
    
- $P_X(2) = 9/32$
    
- $P_X(3) = 19/32$
    

II. Marginal Distribution of Y ($P_Y(y)$):

We sum the joint probability over all values of x ($x=0, 1, 2, 3$).

$$P_Y(y) = \sum_{x=0}^{3} \frac{x^2+y}{32}$$

$$P_Y(y) = \frac{(0^2+y) + (1^2+y) + (2^2+y) + (3^2+y)}{32}$$

$$P_Y(y) = \frac{y + (1+y) + (4+y) + (9+y)}{32} = \frac{14 + 4y}{32} = \frac{7+2y}{16}$$

For $y = 0, 1$.

- $P_Y(0) = 7/16$
    
- $P_Y(1) = 9/16$
    

---

**6. If X and Y are two random variables having the joint pmf $p(x,y) = \frac{1}{27}(2x + y); x = 0,1,2 ; y = 0,1,2$. Find the conditional distribution for Y for $X = x$.**

Solution:

The conditional distribution is given by:

$$P(Y=y | X=x) = \frac{p(x,y)}{p_X(x)}$$

Step 1: Find Marginal Distribution of X ($p_X(x)$)

$$p_X(x) = \sum_{y=0}^{2} \frac{2x+y}{27}$$

$$p_X(x) = \frac{1}{27} [ (2x+0) + (2x+1) + (2x+2) ]$$

$$p_X(x) = \frac{1}{27} [ 6x + 3 ] = \frac{3(2x+1)}{27} = \frac{2x+1}{9}$$

Step 2: Find Conditional Distribution

$$P(Y=y | X=x) = \frac{\frac{2x+y}{27}}{\frac{2x+1}{9}}$$

$$P(Y=y | X=x) = \frac{2x+y}{27} \times \frac{9}{2x+1}$$

$$P(Y=y | X=x) = \frac{2x+y}{3(2x+1)}$$

(Where $y = 0, 1, 2$)

---

**7. Find the value of a so that the function f(x) defined as follows be a density function $f(x) = ae^{-\frac{x}{\sigma}}, 0 \le x \le \infty$.**

Solution:

For $f(x)$ to be a probability density function (PDF), the integral over the entire range must equal 1.

$$\int_{0}^{\infty} f(x) dx = 1$$

$$\int_{0}^{\infty} a e^{-\frac{x}{\sigma}} dx = 1$$

$$a \left[ \frac{e^{-\frac{x}{\sigma}}}{-1/\sigma} \right]_{0}^{\infty} = 1$$

$$-a\sigma \left[ e^{-\infty} - e^{0} \right] = 1$$

$$-a\sigma [ 0 - 1 ] = 1$$

$$a\sigma = 1 \implies a = \frac{1}{\sigma}$$

**Answer:** $a = \frac{1}{\sigma}$

---

8. Given $f(x,y) = e^{-(x+y)}; x \ge 0, y \ge 0$. then find

i. $P(X > 1)$

ii. $P(X < Y | X < 2Y)$

iii. $P(X + Y < 1)$

Solution:

The function can be written as $f(x,y) = e^{-x}e^{-y}$, meaning X and Y are independent standard exponential variables.

i. $P(X > 1)$

$$P(X>1) = \int_{1}^{\infty} e^{-x} dx = [-e^{-x}]_1^{\infty} = 0 - (-e^{-1}) = e^{-1}$$

ii. $P(X < Y | X < 2Y)$

Let $A = \{X < Y\}$ and $B = \{X < 2Y\}$.

Since $x, y \ge 0$, if $x < y$, then $x < 2y$ is automatically true. Thus $A \subset B$, and $A \cap B = A$.

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(X < Y)}{P(X < 2Y)}$$

- Find $P(X < Y)$:
    
    $$\int_{0}^{\infty} \int_{x}^{\infty} e^{-x}e^{-y} dy dx = \int_{0}^{\infty} e^{-x} [ -e^{-y} ]_x^{\infty} dx$$
    
    $$= \int_{0}^{\infty} e^{-x} (0 - (-e^{-x})) dx = \int_{0}^{\infty} e^{-2x} dx = [\frac{e^{-2x}}{-2}]_0^\infty = \frac{1}{2}$$
    
- Find $P(X < 2Y)$ (which means $y > x/2$):
    
    $$\int_{0}^{\infty} \int_{x/2}^{\infty} e^{-x}e^{-y} dy dx = \int_{0}^{\infty} e^{-x} (e^{-x/2}) dx$$
    
    $$= \int_{0}^{\infty} e^{-1.5x} dx = \frac{1}{1.5} = \frac{2}{3}$$
    
- Result:
    
    $$\frac{1/2}{2/3} = \frac{3}{4}$$
    

iii. $P(X + Y < 1)$

Region: Triangle bounded by $x=0, y=0, y=1-x$.

$$\int_{0}^{1} \int_{0}^{1-x} e^{-x} e^{-y} dy dx = \int_{0}^{1} e^{-x} [ -e^{-y} ]_0^{1-x} dx$$

$$= \int_{0}^{1} e^{-x} (1 - e^{-(1-x)}) dx = \int_{0}^{1} (e^{-x} - e^{-1}) dx$$

$$= [-e^{-x} - x e^{-1}]_0^1$$

$$= (-e^{-1} - e^{-1}) - (-1 - 0)$$

$$= 1 - 2e^{-1}$$

---

**9. Find k so that $f(x,y) = kxy, 1 \le x \le y \le 2$ will be the pdf.**

Solution:

Total integral must be 1. The region is $1 \le x \le 2$ and $x \le y \le 2$.

$$\int_{1}^{2} \int_{x}^{2} kxy \, dy \, dx = 1$$

Inner integral w.r.t y:

$$\int_{x}^{2} y \, dy = [\frac{y^2}{2}]_x^2 = \frac{4 - x^2}{2}$$

Outer integral:

$$\int_{1}^{2} kx (\frac{4 - x^2}{2}) dx = \frac{k}{2} \int_{1}^{2} (4x - x^3) dx$$

$$= \frac{k}{2} [ 2x^2 - \frac{x^4}{4} ]_1^2$$

Evaluate at limits:

Upper (2): $2(4) - 16/4 = 8 - 4 = 4$

Lower (1): $2(1) - 1/4 = 1.75 = 7/4$

$$\frac{k}{2} (4 - \frac{7}{4}) = \frac{k}{2} (\frac{9}{4}) = \frac{9k}{8}$$

Set to 1:

$$\frac{9k}{8} = 1 \implies k = \frac{8}{9}$$

**Answer:** $k = \frac{8}{9}$.

---

10. The joint pdf of 2-D random variable (X, Y) is given by $f(x,y) = \frac{8}{9}xy$ for $1 \le x \le y \le 2$ and 0 elsewhere.

i). Find the marginal density functions of X and Y.

ii). Find the conditional density function of Y given X=x, and conditional density function of X given Y=y.

**Solution:**

**i) Marginal density functions**

- For X ($f_X(x)$): Range of $y$ is $x$ to $2$.
    
    $$f_X(x) = \int_{x}^{2} \frac{8}{9}xy dy = \frac{8}{9}x [\frac{y^2}{2}]_x^2$$
    
    $$f_X(x) = \frac{4}{9}x (4 - x^2), \quad 1 \le x \le 2$$
    
- For Y ($f_Y(y)$): Range of $x$ is $1$ to $y$.
    
    $$f_Y(y) = \int_{1}^{y} \frac{8}{9}xy dx = \frac{8}{9}y [\frac{x^2}{2}]_1^y$$
    
    $$f_Y(y) = \frac{4}{9}y (y^2 - 1), \quad 1 \le y \le 2$$
    

**ii) Conditional density functions**

- Y given X=x ($f(y|x)$):
    
    $$f(y|x) = \frac{f(x,y)}{f_X(x)} = \frac{\frac{8}{9}xy}{\frac{4}{9}x(4-x^2)}$$
    
    $$f(y|x) = \frac{2y}{4-x^2}, \quad x \le y \le 2$$
    
- X given Y=y ($f(x|y)$):
    
    $$f(x|y) = \frac{f(x,y)}{f_Y(y)} = \frac{\frac{8}{9}xy}{\frac{4}{9}y(y^2-1)}$$
    $$f(x|y) = \frac{2x}{y^2-1}, \quad 1 \le x \le y$$
---
    