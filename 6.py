import functools
    
def sum_of_squares(upper_limit):
    return functools.reduce((lambda x, y: x + y**2 ), range(1, upper_limit+1))

# print(sum_of_squares(10))

def square_of_sum(upper_limit):
    return (functools.reduce((lambda x, y: x + y), range(1, upper_limit+1)) ** 2)

# print(square_of_sum(10))

print(square_of_sum(100) - sum_of_squares(100))
