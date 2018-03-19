
# Find the largest palindrome made from the product of two 3-digit numbers.

def checkPalindrome(number):
    # Take a string instead of int for easier manipulation
    # Recursively check first and last number and remove them if they match, else return False
    numString = str(number)
    # print(numString)
    if (len(numString) == 1 or len(numString) == 0):
        return True
    if (numString[0] == numString[-1]):
        if checkPalindrome(numString[1:-1]):
            return True
    else:
        return False

# print(checkPalindrome(1001))
# print(checkPalindrome(105))


palindrome = 0
num1 = 0
num2 = 0

for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        calc = i * j
        if (calc > palindrome and checkPalindrome(calc)):
            palindrome = calc
            num1 = i
            num2 = j

print(palindrome, num1, num2)
