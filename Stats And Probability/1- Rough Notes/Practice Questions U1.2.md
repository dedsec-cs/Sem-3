### Median

**Example:**

  * Obtain the median for the following frequency distribution:

| x | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| f | 8 | 10 | 11 | 16 | 20 | 25 | 15 | 9 | 6 |

**Solution:**
For a discrete frequency distribution, the median is the value of $x$ corresponding to the $\left(\frac{N+1}{2}\right)^{\text{th}}$ observation, where $N = \sum f$. We first calculate the **Cumulative Frequency** ($c.f.$).

| $x$       | $f$              | $c.f.$ |
| --------- | ---------------- | ------ |
| 1         | 8                | 8      |
| 2         | 10               | 18     |
| 3         | 11               | 29     |
| 4         | 16               | 45     |
| **5**     | **20**           | **65** |
| 6         | 25               | 90     |
| 7         | 15               | 105    |
| 8         | 9                | 114    |
| 9         | 6                | 120    |
| **Total** | $\mathbf{N=120}$ |        |

Total frequency: $N = 120$.
Median Position $= \frac{N+1}{2} = \frac{120+1}{2} = 60.5$.

The $c.f.$ just greater than $60.5$ is $65$, which corresponds to $\mathbf{x=5}$.
$$\text{Median} = \mathbf{5}$$

-----

**Example:**

  * Find the median wages of the following distribution:

| Wages | 2000-3000 | 3000-4000 | 4000-5000 | 5000-6000 | 6000-7000 |
|---|---|---|---|---|---|
| No. of workers ($f$) | 3 | 5 | 20 | 10 | 5 |

**Solution:**
For a grouped frequency distribution, the median is calculated using the formula:
$$M = L + \left(\frac{\frac{N}{2} - c.f._{p}}{f_M}\right) \times h$$

First, we find $N$ and $N/2$, and then calculate $c.f.$ to find the median class.

| Wages | $f$ | $c.f.$ |
|---|---|---|
| 2000-3000 | 3 | 3 |
| 3000-4000 | 5 | 8 |
| **4000-5000** | **20** | **28** |
| 5000-6000 | 10 | 38 |
| 6000-7000 | 5 | 43 |
| **Total**| $\mathbf{N=43}$ | |

$N = 43$. $N/2 = 43/2 = 21.5$.
The $c.f.$ just greater than $21.5$ is $28$, so the **Median Class** is $\mathbf{4000-5000}$.

  * $L = 4000$ (Lower limit of the median class)
  * $c.f._{p} = 8$ (c.f. of the preceding class)
  * $f_M = 20$ (Frequency of the median class)
  * $h = 1000$ (Class size)

$$M = 4000 + \left(\frac{21.5 - 8}{20}\right) \times 1000$$
$$M = 4000 + \left(\frac{13.5}{20}\right) \times 1000$$
$$M = 4000 + 0.675 \times 1000$$
$$M = 4000 + 675 = \mathbf{4675}$$
The median wage is $\mathbf{Rs. 4675}$.

-----

### Mode

**Example:**

  * Calculate the mode from the following frequency distribution:

| Size (x) | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|
| Frequency (f) | 2 | 5 | 8 | 9 | 12 | 14 | 14 | **15** | 11 | 13 |

**Solution:**
For a discrete distribution, the mode is the value of $x$ that has the highest frequency.
The highest frequency is $\mathbf{15}$, which corresponds to the size $\mathbf{x=11}$.
$$\text{Mode} = \mathbf{11}$$

-----

**Example:**

  * Find the mode of the following:

| Marks | 0-5 | 6-10 | 11-15 | 16-20 | 21-25 | 26-30 | 31-35 | 36-40 | 41-45 |
|---|---|---|---|---|---|---|---|---|---|
| No. of candidates ($f$) | 7 | 10 | 16 | **32** | 24 | 18 | 10 | 5 | 1 |

**Solution:**
The classes are **discontinuous** (inclusive). We first make them continuous (exclusive) by subtracting $0.5$ from the lower limit and adding $0.5$ to the upper limit. (e.g., $0-5$ becomes $-0.5 - 5.5$).

The formula for Mode in grouped data is:
$$\text{Mode} = L + \left(\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) \times h$$

1.  **Identify Modal Class:** The highest frequency is $\mathbf{f_1=32}$, so the modal class is $16-20$.
2.  **Continuous Class:** The continuous modal class is $15.5 - 20.5$.
3.  **Parameters:**
      * $L = 15.5$ (Lower limit of the modal class)
      * $f_1 = 32$ (Frequency of the modal class)
      * $f_0 = 16$ (Frequency of the preceding class, 11-15)
      * $f_2 = 24$ (Frequency of the succeeding class, 21-25)
      * $h = 5$ (Class size: $20.5 - 15.5$)

$$\text{Mode} = 15.5 + \left(\frac{32 - 16}{2(32) - 16 - 24}\right) \times 5$$
$$\text{Mode} = 15.5 + \left(\frac{16}{64 - 40}\right) \times 5$$
$$\text{Mode} = 15.5 + \frac{16}{24} \times 5$$
$$\text{Mode} = 15.5 + \frac{2}{3} \times 5 \approx 15.5 + 3.3333 = \mathbf{18.83}$$

-----

**Example:**

  * Define the Mode and calculate Mode for the distribution of monthly rent Paid by Libraries in Karnataka:

| Monthly rent | 500-1000 | 1000-1500 | 1500-2000 | **2000-2500** | 2500-3000 | 3000 and above |
|---|---|---|---|---|---|---|
| No. of Library ($f$) | 5 | 10 | 8 | **16** | 14 | 12 |

**Solution:**
The **Mode** is defined as the value that occurs most frequently in a distribution. For grouped data, it is the value with the greatest density (highest frequency).

We use the same formula as above:
$$\text{Mode} = L + \left(\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) \times h$$

1.  **Identify Modal Class:** The highest frequency is $\mathbf{f_1=16}$, so the **Modal Class** is $\mathbf{2000-2500}$.
2.  **Parameters:**
      * $L = 2000$ (Lower limit of the modal class)
      * $f_1 = 16$
      * $f_0 = 8$ (Frequency of the preceding class, 1500-2000)
      * $f_2 = 14$ (Frequency of the succeeding class, 2500-3000)
      * $h = 500$ (Class size)

$$\text{Mode} = 2000 + \left(\frac{16 - 8}{2(16) - 8 - 14}\right) \times 500$$
$$\text{Mode} = 2000 + \left(\frac{8}{32 - 22}\right) \times 500$$
$$\text{Mode} = 2000 + \frac{8}{10} \times 500$$
$$\text{Mode} = 2000 + 0.8 \times 500 = 2000 + 400 = \mathbf{2400}$$
The modal monthly rent is $\mathbf{Rs. 2400}$.

-----
### Mean, Median, and Mode

**Example:**

  * Calculate the mean, median and mode of the following data:

| Wages (in Rs) | 0-20 | 20-40 | 40-60 | 60-80 | 80-100 | 100-120 | 120-140 |
|---|---|---|---|---|---|---|---|
| No. of Workers ($f$) | 6 | 8 | 10 | 12 | 6 | 5 | 3 |

**Solution:**
We calculate the midpoint ($m$) and cumulative frequency ($c.f.$) to find the measures of central tendency.

| Wages | $f$ | $m$ | $f \cdot m$ | $c.f.$ |
|---|---|---|---|---|
| 0-20 | 6 | 10 | 60 | 6 |
| 20-40 | 8 | 30 | 240 | 14 |
| 40-60 | 10 | 50 | 500 | 24 |
| **60-80** | **12** | **70** | **840** | **36** |
| 80-100 | 6 | 90 | 540 | 42 |
| 100-120 | 5 | 110 | 550 | 47 |
| 120-140 | 3 | 130 | 390 | 50 |
| **Total**| $\mathbf{N=50}$ | | $\mathbf{\sum (f \cdot m) = 3120}$ | |

#### 1\. Mean ($\bar{x}$)

$$\bar{x} = \frac{\sum (f \cdot m)}{N} = \frac{3120}{50} = \mathbf{62.4}$$

#### 2\. Median ($M$)

$N/2 = 50/2 = 25$. The $c.f.$ just greater than $25$ is $36$, so the **Median Class** is $\mathbf{60-80}$.

  * $L = 60$, $h = 20$, $f_M = 12$, $c.f._{p} = 24$.
    $$M = L + \left(\frac{\frac{N}{2} - c.f._{p}}{f_M}\right) \times h = 60 + \left(\frac{25 - 24}{12}\right) \times 20$$
    $$M = 60 + \frac{1}{12} \times 20 \approx 60 + 1.6667 = \mathbf{61.67}$$

#### 3\. Mode ($Z$)

The highest frequency is $12$, so the **Modal Class** is $\mathbf{60-80}$.

  * $L = 60$, $h = 20$, $f_1 = 12$, $f_0 = 10$, $f_2 = 6$.
    $$\text{Mode} = L + \left(\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) \times h = 60 + \left(\frac{12 - 10}{2(12) - 10 - 6}\right) \times 20$$
    $$\text{Mode} = 60 + \frac{2}{24 - 16} \times 20 = 60 + \frac{2}{8} \times 20 = 60 + 5 = \mathbf{65.0}$$

**Final Results:**

  * Mean $\approx \mathbf{Rs. 62.40}$
  * Median $\approx \mathbf{Rs. 61.67}$
  * Mode $=\mathbf{Rs. 65.00}$