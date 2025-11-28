# 📘 Data Structures and Algorithms - University of Helsinki

> **Type:** Course

> **Status:** 🚧 In progress
---

## 📝 Overview

The aim of the course Data Structures and Algorithms is to advance your programming skills and teach you techniques and ways of thinking that help you in implementing programs that are correct and efficient in all circumstances.


## 📚  Notes

### <span style="color: red">Introduction</span>

**What is an algorithm?:** An algorithm is a method for solving some computational problem. An algorithm implemented in some programming language can be executed on a computer.

The input of an algorithm is the initial data provided to the algorithm. The output of an algorithm is the answer produced by the algorithm by the end of its execution.

**What is a data structure?:** A data structure is a way of storing data within a program. The basic data structure in Python is the list, but there are many other standard data structures too. The choice of data structures is an important part of designing an algorithm, because the data structures have a big effect on the efficiency of the algorithm.

### Efficiency of algorithms

The same task can be solved by different algorithms, and there can be big differences in their efficiencies. Often the goal is to find an efficient algorithm that solves the task quickly.

The efficiency of an algorithm can be studied with a test program that runs the algorithm for a given input and measures the execution time. It is often a good idea to write the test program so that it generates a random input of a given size. Then it is easy to test the algorithm with inputs of different sizes.

```python
import random
import time

def max_diff(numbers):
    ...

n = 1000
print("n:", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
result = max_diff(numbers)
end_time = time.time()

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")
```

### Analysis of algorithms

The efficiency of an algorithm can be estimated by counting how many steps the algorithm executes for an input of a given size. Often we can think of a step as corresponding to a line of code.

Often we do not need to determine the exact number of steps, but it is enough to know the time complexity O(⋯),, which gives the magnitude of the number of steps on a given input size.

In practice, the time complexity is often determined by the loops in the code.

1. Constant time

If an algorithm has no loops and it executes the same steps independent of the input, its time complexity is O(1).
```python
def middle(numbers):
    n = len(numbers)
    return numbers[n // 2]
```

2. Single loop

If the algorithm contains a single loop that goes through all elements of the input, its time complexity is O(n)
```python
def calc_sum(numbers):
    result = 0
    for x in numbers:
        result += x
    return result
```

3. Nested loops

If an algorithm contains a loop inside a loop, each of which goes through all elements of the input, its time complexity is O(n**k)
```python
# O(n**2)
def has_sum(numbers, x):
    for a in numbers: #1
        for b in numbers: #2
            if a + b == x:
                return True
    return False
```

4. Sequential code segments

If the algorithm consists of multiple code segments in sequence, the whole time complexity is the maximum of the segment time complexities.
```python
def count_min(numbers):
    # stage 1 O(n)
    min_value = numbers[0]
    for x in numbers:
        if x < min_value:
            min_value = x

    # stage 2 O(n)
    result = 0
    for x in numbers:
        if x == min_value:
            result += 1

    return result # Since each stage has time complexity O(n), the time complexity of the whole algorithm is O(n)
```



## 🔗 Resources

- [Course](https://tira.mooc.fi/spring-2025)
