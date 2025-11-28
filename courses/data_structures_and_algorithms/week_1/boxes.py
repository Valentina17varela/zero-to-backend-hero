# BOXES
# A given maximum number of products fits in each box. How many boxes is needed at least?
# Input:
# product_count: the total number of products
# box_size: the number of products that fits in one box
# Output:
# the minimum number of boxes needed to pack all products
# Alternative solution:
# def min_count(product_count, box_size):
#   return (product_count + box_size - 1) // box_size


def min_count(product_count, box_size):
    if box_size > product_count:
        return 1

    sum = 0
    if (product_count % box_size) > 0:
        sum = 1

    return (product_count // box_size) + sum


if __name__ == "__main__":
    print(min_count(10, 3))  # 4
    print(min_count(10, 4))  # 3
    print(min_count(100, 1))  # 100
    print(min_count(100, 100))  # 1
    print(min_count(100, 99))  # 2
    print(min_count(5, 5))  # 1
    print(min_count(5, 6))  # 1
