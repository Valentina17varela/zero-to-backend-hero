# Segments
"""
Your task is to divide a string into segments so that each segment is a repeat of the same character.
The segments should be represented as a list of pairs containing the segments lengths and characters.

For example, the string aaabbccdddd has four segments and can be represented as the list
[(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')].

The function returns a list of pairs representing the segments of the string.
Each test string consists of the characters a–z and contains 1–100 characters.
"""


def find_segments(data):
    pairs = []
    find = data[0]
    counter = 1

    for element in data[1:]:

        if element == find:
            counter += 1
        else:
            pairs.append((counter, find))
            find = element
            counter = 1

    pairs.append((counter, find))
    return pairs


if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]
