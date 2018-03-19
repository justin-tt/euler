# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


num = 1

def evenly_divisible(upper_limit, number):
    for i in range(1, upper_limit + 1):
        if (number % i != 0):
            return False
    return True

# print(evenly_divisible(10, 2520))

# This didn't work, bruteforce was way too slow
while (not evenly_divisible(220, num)):
    num += 1

print(num)
