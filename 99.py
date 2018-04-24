# Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

# However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

# NOTE: The first two lines in the file represent the numbers in the example given above.

import math

with open("p099_base_exp.txt") as f:
  num_list = f.read().splitlines()
f.close()

for i in range(len(num_list)):
  num_list[i] = num_list[i].split(',')
  for j in range(2):
    num_list[i][j] = int(num_list[i][j])
    
# print(num_list)
# print(num_list[999][1])

# https://math.stackexchange.com/questions/8308/working-with-large-exponents
# work out the logs insteadwget https://projecteuler.net/project/resources/p099_base_exp.txt
num_list_dict = {}
for i in range(len(num_list)):
  num_list_dict[i] = num_list[i][1] * math.log(num_list[i][0])

print(num_list_dict)
# https://chrisalbon.com/python/find_the_max_value_in_a_dictionary.html
print(max(zip(num_list_dict.values(), num_list_dict.keys())))
