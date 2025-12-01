"""
Word grid
You are given a grid of letters and your task is to find words in the grid.
A word can be read horizontally, vertically or diagonally in either direction.

- set_grid: sets the contents of the grid as a list, where each element is a string representing a row of the grid
- count: counts the number of occurrences of the given word

If a word can be read both forwards and backwards using the same letters, that should count as one occurrence only.
The height and width of each test grid is at most 20 letters. Each letter is in the range A–Z.
"""


class WordFinder:
    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0

    def set_grid(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def count(self, word):
        if not word or self.rows == 0 or self.cols == 0:
            return 0

        L = len(word)

        # Caso especial: palabra de 1 letra (no debe contarse por dirección)
        if L == 1:
            ch = word[0]
            return sum(row.count(ch) for row in self.grid)

        rev = word[::-1]

        directions = [
            (0, 1),  # derecha
            (1, 0),  # abajo
            (1, 1),  # diagonal abajo-derecha
            (1, -1),  # diagonal abajo-izquierda
        ]

        def in_bounds(r, c):
            return 0 <= r < self.rows and 0 <= c < self.cols

        def matches(r, c, dr, dc, target):
            for k in range(L):
                rr = r + dr * k
                cc = c + dc * k
                if not in_bounds(rr, cc) or self.grid[rr][cc] != target[k]:
                    return False
            return True

        total = 0
        for r in range(self.rows):
            for c in range(self.cols):
                for dr, dc in directions:
                    if matches(r, c, dr, dc, word):
                        total += 1
                    if rev != word and matches(r, c, dr, dc, rev):
                        total += 1

        return total


if __name__ == "__main__":
    grid = ["TIRATIRA", "IRATIRAT", "RATIRATI", "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA"))  # 7
    print(finder.count("TA"))  # 13
    print(finder.count("RITARI"))  # 3
    print(finder.count("A"))  # 8
    print(finder.count("AA"))  # 6
    print(finder.count("RAITA"))  # 0
