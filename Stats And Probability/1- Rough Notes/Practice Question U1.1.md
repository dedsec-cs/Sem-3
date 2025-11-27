### Arithmetic Mean

**Example:**

  * Find the arithmetic mean of the following frequency distribution:

| x | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| f | 5 | 9 | 12| 17| 14| 10| 6 |

**Solution:**
The arithmetic mean ($\bar{x}$) for a discrete frequency distribution is calculated using the formula:
$$\bar{x} = \frac{\sum (f \cdot x)}{\sum f}$$

First, we calculate the sum of frequencies ($\sum f$) and the sum of the product of the value and its frequency ($\sum (f \cdot x)$):

| $x$ | $f$ | $f \cdot x$ |
|---|---|---|
| 1 | 5 | 5 |
| 2 | 9 | 18 |
| 3 | 12| 36 |
| 4 | 17| 68 |
| 5 | 14| 70 |
| 6 | 10| 60 |
| 7 | 6 | 42 |
| **Total**| $\mathbf{\sum f = 73}$ | $\mathbf{\sum (f \cdot x) = 299}$ |

Now, we substitute the values into the formula:
$$\bar{x} = \frac{299}{73} \approx \mathbf{4.0959}$$

-----

**Example:**

  * Calculate the mean for the following frequency distribution:

| Class interval | 0-8 | 8-16 | 16-24 | 24-32 | 32-40| 40-48|
|---|---|---|---|---|---|---|
| Frequency | 8 | 7 | 16 | 24 | 15 | 7 |

**Solution:**
The arithmetic mean ($\bar{x}$) for a grouped frequency distribution is calculated using the formula:
$$\bar{x} = \frac{\sum (f \cdot m)}{\sum f}$$
where $m$ is the **class mark** (midpoint) of the class interval.

First, we find the class mark ($m$) for each interval, calculate $f \cdot m$, and then find the sums.

| Class interval | Frequency ($f$) | Midpoint ($m$) | $f \cdot m$ |
|---|---|---|---|
| 0-8 | 8 | 4 | 32 |
| 8-16 | 7 | 12 | 84 |
| 16-24 | 16 | 20 | 320 |
| 24-32 | 24 | 28 | 672 |
| 32-40| 15 | 36 | 540 |
| 40-48| 7 | 44 | 308 |
| **Total**| $\mathbf{\sum f = 77}$ | | $\mathbf{\sum (f \cdot m) = 1956}$ |

Now, we substitute the values into the formula:
$$\bar{x} = \frac{1956}{77} \approx \mathbf{25.4026}$$

-----

**Example:**

  * The average salary of male employees in a farm was Rs. 5,200 and that of females was Rs. 4,200. The mean salary of all the employees was Rs. 5,000. Find the percentage of male and female employees.

**Solution:**
This problem uses the concept of the **combined mean** ($\bar{x}_{12}$), which is defined as:
$$\bar{x}_{12} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2}$$
Let $n_1$ be the number of male employees and $n_2$ be the number of female employees. Let $p_1$ be the proportion of male employees, $p_1 = \frac{n_1}{n_1+n_2}$, and $p_2$ be the proportion of female employees, $p_2 = \frac{n_2}{n_1+n_2}$. Note that $p_1 + p_2 = 1$.

The formula can be rewritten in terms of proportions:
$$\bar{x}_{12} = p_1 \bar{x}_1 + p_2 \bar{x}_2$$
Given:

  * $\bar{x}_{12} = 5000$
  * $\bar{x}_1 = 5200$ (Male)
  * $\bar{x}_2 = 4200$ (Female)
  * $p_2 = 1 - p_1$

Substitute the values into the equation:
$$5000 = p_1(5200) + (1 - p_1)(4200)$$
$$5000 = 5200p_1 + 4200 - 4200p_1$$
$$5000 - 4200 = 5200p_1 - 4200p_1$$
$$800 = 1000p_1$$
$$p_1 = \frac{800}{1000} = 0.8$$

The proportion of male employees is $p_1 = 0.8$, so the percentage of male employees is $0.8 \times 100 = \mathbf{80\%}$.

The proportion of female employees is $p_2 = 1 - p_1 = 1 - 0.8 = 0.2$, so the percentage of female employees is $0.2 \times 100 = \mathbf{20\%}$.