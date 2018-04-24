def get_proper_divisors(n):
    # going from 1 to n is pointless, once the divisors crossover
    # we can stop.
    front = 1
    end = n
    factors = [1]
    for i in range(2, n+1):
        # this condition weeds out the primes
        if i == n:
            break
        if front >= end:
            break
        else:
            if n % i == 0:
                factors.append(i)
                factors.append(int(n / i))
                front = i
                end = n / i
    # to make the list of factors unique
    factors = list(set(factors))
    factors.sort()
    # print(n, factors)
    return factors

assert get_proper_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
assert sum(get_proper_divisors(220)) == 284


def type_of_number(n):
    sum_of_proper_divisors = sum(get_proper_divisors(n))
    if sum_of_proper_divisors == n:
        return 'Perfect'
    elif sum_of_proper_divisors > n:
        return 'Abundant' 
    else:
        return 'Deficient'
    

assert get_proper_divisors(28) == [1, 2, 4, 7, 14]
assert type_of_number(12) == 'Abundant'
assert type_of_number(28) == 'Perfect'

# need to find all abundant numbers from 1 to 28123 (inclusive)
abundant_dictionary = {}
for i in range(1, 28124):
#for i in range(1, 300):
    if type_of_number(i) == 'Abundant':
        abundant_dictionary[i] = True

print(abundant_dictionary)
print(len(abundant_dictionary))


# generate a dictionary of stuff that CAN be written as sums of abundant numbers
nums_that_can_be_summed_by_abundant_numbers = {}
for key, value in abundant_dictionary.items():
    abundant_dictionary_copy = abundant_dictionary.copy()
    for key2, value2 in abundant_dictionary_copy.items():
        if key + key2 < 28124:
            nums_that_can_be_summed_by_abundant_numbers[key + key2] = True
        else:
            break

print(nums_that_can_be_summed_by_abundant_numbers)

sum_of_positive_integers_that_cannot_be_written_as_sums_of_two_abundant_numbers = 0

for i in range(1, 28124):
    if not i in nums_that_can_be_summed_by_abundant_numbers:
        sum_of_positive_integers_that_cannot_be_written_as_sums_of_two_abundant_numbers += i

print(sum_of_positive_integers_that_cannot_be_written_as_sums_of_two_abundant_numbers)
