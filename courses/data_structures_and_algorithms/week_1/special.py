# Special Year
# The year 2025 is special because (20+25)^2=2025, i.e., the the year is the square of the sum of its first and second halves.
# implement the function check_year that reports if the given year is special. The function should return True or False.


def check_year_v1(year):
    year = str(year)
    return (int(year[:2]) + int(year[-2:])) ** 2 == int(year)


def check_year(year: int) -> bool:
    first2 = year // 100
    last2 = year % 100
    return (first2 + last2) ** 2 == year


if __name__ == "__main__":
    print(check_year(1995))  # False
    print(check_year(2024))  # False
    print(check_year(2025))  # True
    print(check_year(2026))  # False
    print(check_year(3025))  # True
    print(check_year(5555))  # False
