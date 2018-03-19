# find the GCD, LCM, then use LCM to consecutively roll from 1-20

# using euclidean algorithm to find GCD

def gcd(a, b):
    # b must be bigger than a
    temp1 = a
    temp2 = b
    while (temp2 % temp1 != 0):
        remainder = temp2 % temp1
        temp2 = temp1
        temp1 = remainder
        # print(remainder, temp2, temp1)
    return temp1


# print(gcd(24, 60))  # 12
# print(gcd(40, 64))  # 8

def lcm(a, b):
    return a*(b / gcd(a, b)) # comment in stack overflow that it's better than (a*b) / gcd(a,b) since a*b could be huge

# print(lcm(24, 60)) # 120

n = 1
for i in range(1,21):
    n = lcm(n, i)

print(n)
