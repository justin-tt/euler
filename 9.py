"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# Use Euclid's formula first
list_of_triples = []
for m in range(1000):
    for n in range(1000):
        if (m**2 - n**2 < 0):
            break
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if (a + b + c > 1000):
            break
        triple = (a, b, c)
        list_of_triples.append(triple)
        if (a + b + c == 1000):
            print(triple)
            print(triple[0] * triple[1] * triple[2])


# print(list_of_triples)

# Then generate multiples with k
