"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
# use sieve of eratosthenes

import math
primes = {}
prime_dict = {}
limit = 2000000
sieve_limit = math.ceil(math.sqrt(limit))
for i in range(2, limit):
    primes[i] = 0

for i in range(2, limit):
    if primes[i] == 0:
        primes[i] = 1
        prime_dict[i] = 1

    multiple = i+i
    while (multiple < 2000000):
        primes[multiple] = 1
        multiple += i 

# print(primes)
# print(prime_dict)
sum_of_primes = 0
for key, value in prime_dict.items():
    sum_of_primes += key

print(sum_of_primes)
