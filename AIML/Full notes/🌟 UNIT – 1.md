Hello! Based on the uploaded presentation on "Unit 1: Introduction to AI and Problem-Solving Methods" for Artificial Intelligence & Machine Learning, here are the detailed notes for each topic covered.

## 📜 Unit-I Content Overview

The content of Unit-I focuses on the fundamentals of Artificial Intelligence and problem-solving through search techniques.

- Introduction to AI and Intelligent Agents
    
- Different Approaches of AI
    
- Problem Solving by Searching Techniques
    
    - **Uninformed Search**: BFS, DFS, Iterative Deepening, Bidirectional Search
        
    - **Informed Search**: Iterative Deepening, Bidirectional Search, Heuristic Search, Greedy Best First Search, A* search
        
    - **Local Search Algorithms**: Hill Climbing and Simulated Annealing
        
    - **Adversarial Search**: Game Playing (minimax, alpha-beta pruning)
        
    - Constraint Satisfaction Problems
        

---

## 🤖 Introduction to Artificial Intelligence (AI)

AI is a field in computer science where computers are trained to perform tasks that humans are typically good at, such as visualizing capabilities and recognizing patterns.

- **Definition**: AI is a branch of computer science focused on creating systems capable of performing tasks that normally require human intelligence. This involves developing algorithms and models that allow machines to **learn from data**, **recognize patterns**, and **make decisions**.
    
- **Subfields**: It encompasses subfields like **Machine Learning** (systems improve through experience) and **Natural Language Processing** (machines understand/generate human language).
    

### History and Key Figures

- **Early Work (1943)**: The first generally recognized work in AI was done by **Warren McCulloh and Walter Pitts**. They proposed a model of artificial neurons that could be either on or off. They showed that any computable function could be computed by a network of connected neurons, suggesting that suitably defined networks could also learn. Their work drew upon:
    
    - Knowledge of basic Physiology and Functions of Neurons in the brain.
        
    - A formal analysis of propositional logic.
        
    - Turing’s Theory of Computation.
        
- **Turing Test**: Proposed by **Alan Turing** (1950), it provides an operational definition of intelligence. A computer passes the test if a human interrogator cannot distinguish its written responses from those of a person.
    
- **The Birth of AI (1956)**: The term "AI" was coined by **John McCarthy** at the Dartmouth Conference. He is often known as the **"Father of AI"** and developed the LISP programming language in 1958.
    

### Drawbacks of AI (Disadvantages)

- **Job Displacement and Unemployment**: AI takes over tasks traditionally performed by humans, putting certain professions (e.g., in manufacturing) at risk.
    
- **Loss of Human Skills**: Over-reliance on AI (e.g., using GPS for navigation) risks losing essential human skills.
    
- **Privacy Concerns**: AI systems are data-hungry and often require personal information, which, as AI collects and analyzes this data, can lead to escalating privacy concerns.
    

---

## Forms of AI
![[Pasted image 20251105165852.png]]
## ⚙️ Intelligent Agents

### Agent Definition

- An agent is anything that **perceives** its environment through **sensors** and **acts** upon that environment through **actuators**.
    
- An Agent runs in the cycle of **perceiving**, **thinking**, and **acting**.
    
- An **intelligent agent** is an autonomous entity that acts upon an environment using sensors and actuators for achieving goals and may learn from the environment to achieve them. A thermostat is an example.
    

### Rules for an AI Agent

1. Must have the ability to **perceive** the environment.
    
2. The observation must be used to make **decisions**.
    
3. Decision should result in an **action**.
    
4. The action must be a **rational action**.
    

### Structure of an AI Agent

An agent is a combination of **Architecture** and an **Agent Program**.

- **Architecture**: The physical machinery or device (e.g., a robotic car, a camera, or a PC) that the agent executes on, equipped with sensors and actuators.
    
- **Agent Program**: An implementation of an **agent function**, which is a map from the **percept sequence** (history of all that an agent has perceived) to an action.
- Agent = Architecture + Agent Program

### Types of Agents

Agents are grouped into classes based on their perceived intelligence and capability. The five core classes are:

1. **Simple Reflex Agents**:
    
    - Ignores the rest of the percept history and acts only based on the **current percept**.
        
    - The agent function relies on a **condition-action rule** (If [condition] is true, then [action] is taken).
        
2. **Model-Based Reflex Agents**:
    
    - Uses a **model about the world** to handle **partially observable environments**.
        
    - Keeps track of the **internal state**, which is adjusted by each percept and depends on the percept history. This state describes the unseen part of the world.
        
3. **Goal-Based Agents**:
    
    - Makes decisions based on how close they are to their **goal** (a description of desirable situations).
        
    - Every action is intended to **reduce the distance from the goal**, allowing the agent to choose among multiple possibilities.
        
4. **Utility-Based Agents**:
    
    - Used when there are **multiple possible alternatives** to decide which one is best.
        
    - Chooses actions based on a **preference (utility)** for each state, maximizing the agent's expected utility.
        
5. **Learning Agents**:
    
    - Can **learn from past experiences** and have capabilities for continuous learning.
        
    - Starts with basic knowledge and can then automatically **act and adapt** through learning.
        

_Additional Types mentioned_: Multi-agent systems, Hierarchical agents.

---
## Uses of Agents:
![[Pasted image 20251105170437.png]]

## 📊 Problem Solving by Searching Techniques

Problem-solving is achieved through search algorithms, which result in a sequence of actions called a **plan** that transforms the **Start State** to the **Goal State**.

### Components of a Search Problem

- **State Space**: Set of all possible states where the agent can be.
    
- **Start State**: The state from where the search begins.
    
- **Goal State**: A function that returns whether the current state is the goal state.
    

### Types of Search Algorithms
![[Pasted image 20251105170908.png]]
Search algorithms are primarily classified into two types

1. **Uninformed Search (Blind Search)**
    
2. **Informed Search (Heuristic Search)**
    

---

### 1. Uninformed Search Algorithms

These algorithms have **no additional information** about the goal node other than what is in the problem definition. They only generate successors and differentiate between the goal and non-goal state.

| Algorithm                              | Strategy / Data Structure                                                                                                                                             | Advantages                                                                                                                           | Disadvantages                                                                                                      |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| **Depth First Search (DFS)**           | Explores as far as possible along each branch before backtracking; uses **Last In - First Out (LIFO)** implemented with a **stack**                                   | Requires very little memory; can reach the goal node faster than BFS (if on the correct path)                                        | May go into an **infinite loop** in deep searching; no guarantee of finding the solution; many states may re-occur |
| **Breadth First Search (BFS)**         | Searches breadthwise, expanding all successor nodes at the current level before moving to the next; uses **First In - First Out (FIFO)** implemented with a **queue** | **Guaranteed to find a solution** if one exists; finds the **minimal solution** (least number of steps) if multiple solutions exist  | Requires lots of **memory** as each level must be saved; time-consuming if the solution is far from the root node[ |
| **Iterative Deepening Search (IDDFS)** | Combination of DFS and BFS. Gradually increases a **"depth limit"** and performs DFS up to that limit until the goal is found                                         | Combines the **fast search of BFS** and the ** memory efficiency of DFS**Useful when search space is large and goal depth is unknown | Repeats all the work of the previous phase/iteration.                                                              |
| **Bidirectional Search**               | Runs two simultaneous searches: **forward-search** from the initial state and **backward-search** from the goal node. Stops when the two subgraphs intersect.         | Is **fast** and requires **less memory**                                                                                             | Implementation is **difficult**; the **goal state must be known in advance**.                                      |


---

### 2. Informed Search Algorithms

These algorithms use information about the goal state to search more efficiently. This information is provided by a **heuristic**.

#### Search Heuristics

- A heuristic is a **function** that estimates how close a state is to the goal state, represented by **h(n)**.
    
- Examples: Manhattan distance, Euclidean distance (Lesser the distance, closer the goal).
    
- **Admissibility**: A heuristic function is admissible if __$h(n) \le h_(n)$_*, where h∗(n) is the true estimated cost to the goal (the heuristic never overestimates the actual cost).
    
- A heuristic method is guaranteed to find a **good solution in reasonable time**, though not always the best one.
    

#### Greedy Search

- Expands the node **closest to the goal node**.
    
- **Strategy**: Expand the node with the **lowest h(x) value** (closest to the goal).
    

#### A* Algorithm

- A powerful graph traversal and pathfinding algorithm used to find the **shortest path** between two nodes.
    
- It combines the advantages of **Dijkstra's algorithm** and **Greedy Best-First Search**.
    
- **Evaluation Function**: The main idea of A* is to evaluate each node n based on **f(n)=g(n)+h(n)**.
    
    - **g(n)**: The **actual cost** to get from the initial node to node n.
        
    - **h(n)**: The **heuristic cost** (estimation cost) from node n to the destination node; must be admissible.
        
- **Strategy**: Selects the nodes to be explored based on the **lowest value of f(n)**.
    
- **Advantages**:
    
    - **Optimal solution** (shortest path) when using an admissible heuristic.
        
    - **Completeness**: Will find a solution if one exists and the graph doesn't have an infinite cost.
        
    - **Efficiency**: Highly efficient with a good, acceptable heuristic.
        

---

### 3. Local Search Algorithms

#### Hill Climbing Algorithm

- A local search algorithm that continuously moves in the direction of **increasing elevation/value** to find the peak (or best solution).
    
- It terminates when it reaches a peak where no neighbor has a higher value.
    
- Also called **greedy local search** because it only looks at its good immediate neighbor state.
    
- It is a variant of the **Generate and Test** method and is often used when a good heuristic is available.
    
- **Key Feature**: **No backtracking** – it does not remember the previous states.
    
- **Example**: Traveling-salesman Problem (to minimize the distance traveled).
    

---

### 4. Game Playing Algorithms (Adversarial Search)

Game playing is an application of AI for developing programs to play games like chess or checkers. The goal is to develop algorithms that can learn to play and make decisions that lead to winning outcomes.

#### Minimax Algorithm

- A **recursive or backtracking** algorithm used in decision-making and game theory.
    
- Provides an **optimal move** for the player, assuming the opponent is also playing optimally.
    
- It is a **depth-first search** of the complete game tree.
    
- **Players**: **MAX** (seeks to maximize benefit) and **MIN** (seeks to minimize MAX's benefit).
    
- **Limitation**: Can be very **slow** for complex games (like Chess, Go) due to a huge branching factor.
    

#### Alpha-Beta Pruning

- A **modified and optimized version** of the Minimax algorithm used to reduce the number of game states examined, effectively cutting the exponent of search states in half.
    
- Uses two threshold parameters for future expansion:
    
    - **Alpha (α):** The best (**highest-value**) choice found so far along the path of the **Maximizer**. Initial value is **−∞**.
        
    - **Beta (β):** The best (**lowest-value**) choice found so far along the path of the **Minimizer**. Initial value is **+∞**.
        
- **Pruning Condition**: If α≥β, the node (and its right successor/entire sub-tree) is pruned because the current MAX player can achieve a better outcome earlier in the tree, making the current branch irrelevant.
    
- Returns the **same optimal move** as standard Minimax but is much faster by eliminating irrelevant nodes.
    

---

## 🎯 Approaches of AI

There are four main approaches to Artificial Intelligence:

1. **Thinking Humanly**: The cognitive modeling approach.
    
2. **Thinking Rationally**: The laws of thought approach.
    
3. **Acting Humanly**: The Turing Test approach.
    
4. **Acting Rationally**: The rational agent approach.

    
5. **Machine Learning approach**: This approach involves training machines to learn from data and improve performance on specific tasks over time. It is widely used in areas such as image and speech recognition, natural language processing, and recommender systems.
6. **Evolutionary approach:** This approach is inspired by the process of natural selection in biology. It involves generating and testing many variations of a solution to a problem, and then selecting and combining the most successful variations to create a new generation of solutions.
7. **Neural Networks approach:** This approach involves building artificial neural networks that are modeled after the structure and function of the human brain. Neural networks can be used for tasks such as pattern recognition, prediction, and decision-making.
8. **Fuzzy logic approach:** This approach involves reasoning with uncertain and imprecise information, which is common in real-world situations. Fuzzy logic can be used to model and control complex systems in areas such as robotics, automotive control, and industrial automation.
9. **Hybrid approach:** This approach combines multiple AI techniques to solve complex problems. For example, a hybrid approach might use machine learning to analyze data and identify patterns, and then use logical reasoning to make decisions based on those patterns.



## 🚀 Applications of AI (Branch Wise)

AI has applications across many industries:

- Healthcare
    
- Finance
    
- Education
    
- Retail and E-Commerce
    
- Manufacturing
    
- Automotive
    
- Cyber Security
    
- Natural Language Processing
    

---

## ❓ Quiz Questions (with Answers)

| Question                                                 | Answer                                                                                                                                            |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI is intelligence demonstrated by **________**. [       | **Machine**                                                                                                                                       |
| Artificial Intelligence is about_____.                   | **Making a machine Intelligent**                                                                                                                  |
| Who is known as the "Father of AI"?                      | **John McCarthy**                                                                                                                                 |
| Which of the given language is not commonly used for AI? | **Perl**                                                                                                                                          |
| Agents' behavior can be best described by ______         | **Perception sequence**                                                                                                                           |
| Which of the following are examples of Machine Learning? | **All the above** (Learning to recognize spoken words, Learning to drive an autonomous vehicle, Learning to classify new astronomical structures) |
