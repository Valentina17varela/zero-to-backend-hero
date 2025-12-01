# Report the time complexity of each of the following algorithms.
# The correct answer in each case is one of the following: O(1), O(n), O(n^2), O(n^3), O(n^4).


def algo1(n):  # O(n)
    result = 0
    for i in range(n):
        result += i
    return result


def algo2(n):  # O(n) because of two separate O(n) loops, not nested
    result = 0
    for i in range(n):
        result += i
    for i in range(n):
        result -= i
    return result


def algo3(n):  # O(1)
    return 5 * n**2


def algo4(n):  # O(n)
    result = 0
    while n > 0:
        n -= 1
        result += 2
    return result


def algo5(n):  # O(n^2)
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result


def algo6(n):  # O(n)
    result = 0
    for i in range(10):
        result += n
    return result


def algo7(
    n,
):  # O(1) because the loops run a constant number of times, not dependent on n
    result = n
    for i in range(100):
        for j in range(100):
            result -= 1
    return result
