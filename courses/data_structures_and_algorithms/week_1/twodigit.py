"""
Numbers
Your task is to count how many numbers in the range [a,b] consist of the digits 2 and 5 only.
For example, in the range [1,100] the numbers are 2, 5, 22, 25, 52 and 55, and thus the answer is 6.

The function is given the parameters a and b representing the end points of the range.
"""


def count_numbers(a, b):
    if a > b:
        return 0

    total = 0
    queue = [2, 5]
    idx = 0  # puntero para usar la lista como cola sin pop(0)

    while idx < len(queue):
        x = queue[idx]
        idx += 1

        if x > b:
            continue

        if x >= a:
            total += 1

        # genera los siguientes números válidos
        queue.append(x * 10 + 2)
        queue.append(x * 10 + 5)

    return total


if __name__ == "__main__":
    print(count_numbers(1, 100))  # 6
    print(count_numbers(60, 70))  # 0
    print(count_numbers(25, 25))  # 1
    print(count_numbers(1, 10**9))  # 1022
    print(count_numbers(123456789, 987654321))  # 512
