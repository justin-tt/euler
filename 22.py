with open('p022_names.txt') as file:
    name_list = file.read().split(',')
# print(sorted(name_list))
name_list = sorted(name_list)


sum_name_scores = 0

def get_name_score(name):
    name_score = 0
    for c in name:
        if c.isalpha():
            name_score += (ord(c) - 64)
    return name_score

assert get_name_score("COLIN") == 53


for index, name in enumerate(name_list):
    # index starts at 0
    sum_name_scores += ((index + 1) * get_name_score(name))

print(sum_name_scores)
