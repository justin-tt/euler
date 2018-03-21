# http://www.robertdickau.com/lattices.html

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

print(factorial(5)) #120

def binomial_coefficient(n):
    # http://www.robertdickau.com/manhattan.html
    return (factorial(2*n))/(factorial(n)**2)

print(binomial_coefficient(3))
print(binomial_coefficient(20))

