# LIST EFFICIENCY 2
"""
Implement a test, where the numbers 1,2,...,n are added to the end of the list one at a time.
Then the first element of the list is deleted n times.

Implement the test with n=10^5. Make two time measurements: How much time it takes to do all the additions,
and how much time to do all the deletions.
"""

import time


def addition(n):
    numbers = []
    for number in range(n):
        numbers.append(number + 1)

    return numbers


def deletion(n, numbers):
    for _ in range(n):
        numbers.pop(0)


n = 10**5
print("n:", n)

start_time = time.time()
result = addition(n)
end_time = time.time()
print("time:", round(end_time - start_time, 2), "s")

start_time_2 = time.time()
deletion(n, result)
end_time_2 = time.time()
print("time:", round(end_time_2 - start_time_2, 2), "s")
