"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

"""

# triangle number generator
# factoriser, returns a dict of factors
# repeat until -> generate triangle number (i to i++ ..), factorise it, count factors, if factors > 500, stop

def triangle_generator(num):
    triangles = { 1: 1 }
    for i in range(2, num+1):
        triangles[i] = triangles[i-1] + i
    return triangles

print(triangle_generator(7))

def factoriser(num):
    factors = {}
    factor1 = 1
    factor2 = num
    factors[1] = True
    factors[num] = True
    while factor1 < factor2:
        factor1 += 1
        if (num % factor1 == 0):
            factors[factor1] = True
            factor2 = int(num/factor1)
            factors[factor2] = True

    return factors

print(factoriser(30))
print(len(factoriser(30)))

triangles = { 1: 1 }
factors = 0
index = 2
while factors <= 500:
    triangles[index] = triangles[index - 1] + index
    num_of_factors = len(factoriser(triangles[index]))
    if num_of_factors > factors:
        factors = num_of_factors
    index += 1

print(index-1, triangles[index-1])
