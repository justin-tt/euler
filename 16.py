num = 2**1000

num_str = str(num)

sum = 0
for digit in num_str:
    sum += int(digit)

print(sum)
