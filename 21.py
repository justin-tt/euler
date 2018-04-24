def get_proper_divisors(n):
    # going from 1 to n is pointless, once the divisors crossover
    # we can stop.
    front = 1
    end = n
    factors = []
    for i in range(1, n+1):
        if front > end:
            factors.pop()
            factors.pop()
            factors.remove(n)
            factors.sort()
            break
        else:
            if n % i == 0:
                factors.append(i)
                factors.append(int(n / i))
                front = i
                end = n / i

    return factors

assert get_proper_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
assert sum(get_proper_divisors(220)) == 284


def generate_amicable_pair(n):
    sum_proper_divisors = sum(get_proper_divisors(n))
    if sum_proper_divisors == n:
        return False
    if sum(get_proper_divisors(sum_proper_divisors)) == n:
        return True

amicable_dictionary = {}
for i in range(1, 10001):
    if i not in amicable_dictionary:
        if generate_amicable_pair(i):
            amicable_dictionary[i] = True
            amicable_dictionary[sum(get_proper_divisors(i))] = True

print(amicable_dictionary)

amicable_sum = 0
for key in amicable_dictionary:
    amicable_sum += key

print(amicable_sum)
