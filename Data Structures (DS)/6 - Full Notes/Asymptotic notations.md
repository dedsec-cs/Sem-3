# 1. What is Algorithm Complexity?

When we write code, we want it to be efficient. But how do we measure "efficiency"?

We cannot measure it in seconds because that depends on the computer (a Supercomputer is faster than an old laptop).

Instead, we measure **Growth Rate**: How much _more_ work does the algorithm have to do as the input size ($N$) increases?

### **A. Time Complexity**

- **Definition:** Not the actual time (in seconds), but the number of **operations** (steps) an algorithm performs relative to the input size ($N$).
    
- **Goal:** We want to know: If I double the input ($2N$), does the time double? Quadruple? Or stay the same?
    

### **B. Space Complexity**

- **Definition:** The amount of **extra memory** (RAM) the algorithm needs to solve the problem, relative to the input size ($N$).
    
- **Note:** We usually talk about _Auxiliary Space_ (extra space used temporarily). We don't count the space used to store the input itself.
    

---

# 2. Asymptotic Notations (The Language of Complexity)

Asymptotic notation is the mathematical way to describe the "limits" of an algorithm's performance.

![Image of asymptotic notations graph](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTOZHXVr-HZgtDXBlUtJn6YFGXG-UcxnjpXSDGIJSSwH_KavXW-GqtSxXGIsaSiGjh2YvKiHYYZCH9FgQTrRymAvRYLFZYQWuLgmTlIBUuCDvGR5Aw)

Getty Images

### **1. Big Oh Notation ($O$) – "The Pessimist" (Upper Bound)**

This is the most popular notation. It describes the **Worst-Case Scenario**.

- **Meaning:** "The algorithm will **never take longer** than this."
    
- **Formal:** $f(n) = O(g(n))$ if $f(n) \le c \cdot g(n)$.
    
- **Analogy:** If you ask a friend, "How long will it take to fix my PC?" and they say, "**At most** 2 hours," that is Big O. It might take 10 minutes, but it definitely won't take 3 hours.
    
- **Use:** We use this to guarantee performance limits.
    

### **2. Big Omega Notation ($\Omega$) – "The Optimist" (Lower Bound)**

This describes the **Best-Case Scenario**.

- **Meaning:** "The algorithm will take **at least** this much time."
    
- **Formal:** $f(n) = \Omega(g(n))$ if $f(n) \ge c \cdot g(n)$.
    
- **Analogy:** "It will take **at least** 10 minutes to fix the PC." (It could take 10 years, but definitely not 5 minutes).
    
- **Use:** Rarely used in interviews because we rarely care about the best case (e.g., sorting a list that is already sorted).
    

### **3. Big Theta Notation ($\Theta$) – "The Realist" (Tight Bound)**

This describes the **Average/Exact Case**.

- **Meaning:** "The algorithm takes **exactly around** this much time." It sandwhiches the function between an upper and lower bound.
    
- **Formal:** $c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n)$.
    
- **Analogy:** "It will take **about** 1 hour (give or take a few minutes)."
---
