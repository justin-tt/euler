import time
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# Using sieve of Eratosthenes

def sieve_hash_table(max_prime):
  numbers = range(2, max_prime+1)
  prime_flags = []
  for i in range(2, max_prime+1):
    prime_flags.append("unflagged")

  # generate hash table/dictionary
  dictionary = dict(zip(numbers, prime_flags))
  #print(dictionary)
  for i in range(2, max_prime+1):
    if dictionary[i] == "unflagged":
      dictionary[i] = True
    for j in range(i*2, max_prime+1, i):
      if dictionary[j] == "unflagged": # this line costs half the time
        dictionary[j] = False
  #print(dictionary)
  primes = []
  for key in dictionary:
    if dictionary[key] == True:
      primes.append(key)
  return(primes)

time_start = time.time()
list = sieve_hash_table(250000)
print(list[len(list)-1])

remainder = 0
ceiling = 10**10

  
for idx, val in enumerate(list):
  n = idx+1
  if n % 2 == 0:
    continue
  p_n = val
  prime_square_remainder = ((p_n-1)**n + (p_n+1)**n) % (p_n**2)
  if prime_square_remainder > remainder:
    remainder = prime_square_remainder
  # print(idx, prime_square_remainder)
  if remainder > ceiling:
    print(remainder, idx, ceiling)
    break
    

time_end = time.time()
print((time_end - time_start), 'seconds')

