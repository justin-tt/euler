"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of and when writing out numbers is in compliance with British usage.
"""
num_strings = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
}

def parse_number_to_english(number):
    num_str = str(number)
    num_length = len(num_str)
    ones = ""
    tens = ""
    hundreds = ""
    thousands = ""
    
    print(thousands, hundreds, tens, ones)
    num_in_english = ""
    for i in range(-1, -num_length-1, -1):
        if i == -1:
            ones = num_str[i]
            num_in_english = num_strings[int(ones)]
        elif i == -2:
            tens = num_str[i]
            if int(tens) == 1:
                num = 10 + int(num_str[-1])
                num_in_english = num_strings[num]
            else:
                num_in_english = num_strings[int(tens)*10] + num_in_english
        elif i == -3:
            hundreds = num_str[i]
            if int(hundreds):
                if not(int(tens)) and not(int(ones)):
                    num_in_english = num_strings[int(hundreds)] + num_strings[int(100)]
                else:
                    num_in_english = num_strings[int(hundreds)] + num_strings[int(100)] + "and" + num_in_english
        elif i == -4:
            thousands = num_str[i]
            if int(thousands):
                num_in_english = num_strings[int(thousands)] + num_strings[int(1000)] + num_in_english

    return num_in_english
   
def print_word_and_length(numstring):
    print(numstring, len(numstring))
    return len(numstring)

print_word_and_length(parse_number_to_english(1234))

print_word_and_length(parse_number_to_english(1000))

total_letters = 0
for i in range(1, 1001):
    total_letters += print_word_and_length(parse_number_to_english(i))

print(total_letters)

