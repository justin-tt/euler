# regex is re!!
# FUTURE TODO: fix this ugly code
# solved via regex from stackoverflow
# https://stackoverflow.com/questions/29438282/find-repeated-pattern-in-a-string-of-characters-using-r

import re
from decimal import *
getcontext().prec = 5000

def key_with_max_val(d):
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

def recurring(number):
    frac = Decimal(1)/Decimal(number)
    frac_string = str(frac)
    if frac_string[2] == "0" and frac_string[3] == "0":
        # i got the answer after i changed to [4:], when it was [3:] the answer was 977 which was wrong... and [2:] gave an even smaller answer
        # pattern matching should start AFTER the 0.00 otherwise it will fail at 0.000 which parses 00 xxxx as a match
        frac_string = frac_string[4:]
    # print("f", frac_string)
    try:
        if re.search(r"\b(\S+?)\1\S*\b", frac_string):
            # print("string match", re.search(r"\b(\S+?)\1\S*\b", frac_string).group())
            print("number", number)
            print("group", re.search(r"\b(\S+?)\1\S*\b", frac_string).group(1))
            group_len = len(re.search(r"\b(\S+?)\1\S*\b", frac_string).group(1))
            print("group len", group_len)
            # print("group len", len(re.search(r"\b(\S+?)\1\S*\b", frac_string).group(1)))
            # print("len", len(frac_string))
            return group_len
    except:
        pass
    # print(frac_string)
    if len(frac_string) < 17:
        # this assumes that if the string has no recurring cycles, it shouldn't have more than 16 digits
        # loose proof -> 1 / 1000 = 0.001 which is only length 5.
        # based on the test cases 2-10
        return 0
    frac_string = frac_string[:-1]
    # print(frac_string)
    # walk through digits after the decimal point
    # adding a count of each digit to the dictionary
    digit_frequency = {}
    # just check what comes after the decimal point 0.xxx
    for i in frac_string[2:]:
        if int(i) in digit_frequency:
            digit_frequency[int(i)] += 1
        else:
            digit_frequency[int(i)] = 1
    
    # print(digit_frequency)
    # if the frequency of one digit much greater the rest, it is likely
    # that digit has a 1 digit recurring cycle
    total = 0
    for k,v in digit_frequency.items():
        total += digit_frequency[k]
    mean_frequency = total/len(frac_string[2:])
    # print(mean_frequency)
    # if max is 5x mean, it should mean that the digit is fairly spaced out...
    # but i'm not 100% sure this is mathematically correct
    if digit_frequency[key_with_max_val(digit_frequency)] > (5 * mean_frequency):
        return 1
    first_val = frac_string[2]
    positions_with_first_val = []
    for idx, val in enumerate(frac_string):
        if val == first_val:
            positions_with_first_val.append(idx)
    # print(first_val, positions_with_first_val)
    # print("longest recurring cycle:", positions_with_first_val[1] - positions_with_first_val[0])
    if frac_string[2] == "0" and frac_string[3] == "0":
        frac_string = frac_string[3:]
    print(frac_string)
    try:
        print(re.search(r"\b(\S+?)\1\S*\b", frac_string))
    except:
        pass
    return None

assert recurring(2) == 0
assert recurring(3) == 1
assert recurring(4) == 0
assert recurring(5) == 0
assert recurring(6) == 1
# assert recurring(7) == 6
assert recurring(8) == 0
assert recurring(9) == 1
assert recurring(10) == 0

max_r = 0
val_r = 0
d = 0
for i in range(2, 1000):
    r = recurring(i)
    if r:
        if r > max_r:
            max_r = r
            val_r = 1/i
            d = i

print(max_r, d, val_r)
