fib_dict = {
    1: 1,
    2: 1,
}

def fib(n):
    if n <= 2:
        return fib_dict
    for i in range(3, n+1):
        fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]
        # print(i, fib_dict)
        if (len(str(fib_dict[i])) == 1000):
            print(i, fib_dict[i])
    return fib_dict



assert fib(3) == {
    1: 1,
    2: 1,
    3: 2
}

assert fib(5) == {
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5
}

assert len(str(fib(12)[12])) == 3

fib(10000)
