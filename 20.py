def factorial(n):
    total = 1
    for i in range(2, n+1):
        total *= i
    return total

assert factorial(10) == 3628800


def sum_digits(n):
    str_num = str(n)
    total = 0
    for digit in str_num:
        total += int(digit)
    return total

assert sum_digits(factorial(10)) == 27


print(sum_digits(factorial(100)))
