"""
Numbers
Your task is to count how many numbers in the range [a,b] consist of the digits 2 and 5 only.
For example, in the range [1,100] the numbers are 2, 5, 22, 25, 52 and 55, and thus the answer is 6.

The function is given the parameters a and b representing the end points of the range.
Solution: BFS
"""


def count_numbers(a, b):
    numbers = [2, 5]
    count = 0

    for number in numbers:
        if a <= number <= b:
            count += 1

        if number > b:
            continue

        numbers.append(number * 10 + 2)
        numbers.append(number * 10 + 5)

    return count


if __name__ == "__main__":
    print(count_numbers(1, 100))  # 6
    print(count_numbers(60, 70))  # 0
    print(count_numbers(25, 25))  # 1
    print(count_numbers(1, 10**9))  # 1022
    print(count_numbers(123456789, 987654321))  # 512
