# we don't have to do all 10p10 or 3628800 permutations
# if we fix the first number as 0, we only have to worry about 9p9 permutations or 362880 permutations
# so the 1 millionth permutation must start with digit 2, and we need to get the 274240th permutation out of the 362880th permutation


def permute(list):
    # use recursion
    if len(list) == 1:
        # base case returns an array with just the number
        return [list]
    # else:
        # create a list of lists
    lists = []
    list = sorted(list)
    for idx, num in enumerate(list):
        copy = list.copy()
        copy.remove(num)
        # print(copy)
        permute_copy = permute(copy)
        # print(permute_copy)
        for l in permute_copy:
            lists.append([num] + l)
        # lists.append([num] + permute(copy))
    #print(lists)
    return lists
        

print('1')
assert permute([0]) == [[0]]
print('2')
assert permute([0, 1]) == [[0, 1], [1, 0]]
print('3')
assert permute([0, 1, 2]) == [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
assert permute([0, 1, 2]) == permute([2, 1, 0])
print('4')
five_permutes = permute([0,1,2,3,4])
#print(five_permutes, len(five_permutes), five_permutes[119])

### brute force
# ten_permutes = permute([0,1,2,3,4,5,6,7,8,9])
# print(len(ten_permutes), ten_permutes[999999])
###

### using the 274240th permutation of the remaining 9 numbers
nine_permutes = permute([0,1,3,4,5,6,7,8,9])
print(2, nine_permutes[274239])
