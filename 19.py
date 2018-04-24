# approach is to run a loop for every day starting from 1 Jan 1901 until 31 Dec 2000
# have a dictionary that holds every day of the week with a list that appends every single date as the loop runs
# have a way to read the list of sundays and parse how many "firsts" of the month.

# create a number of days generator for each month
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False

assert is_leap_year(1700) is False
assert is_leap_year(1800) is False
assert is_leap_year(1900) is False
assert is_leap_year(2000) is True
assert is_leap_year(2012) is True

def days_in_month(year, month):

    leap_year = is_leap_year(year)
    no_of_days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    return no_of_days_in_month[month]

assert days_in_month(2024, 2) is 29
assert days_in_month(2000, 2) is 29
assert days_in_month(1900, 2) is 28


class Date:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.date} {self.month} {self.year}'

a = Date(1, 12, 1988)
# print(a)
b = Date(1, 12, 1988)
f = Date(1, 4, 2000)
c = [a, b, f]

# filtering how many firsts of the month there are in this list
d = list(filter(lambda x: x.date == 1, c))
print(len(d))


# create a loop to generate dictionary of days with dates
# 1 = monday, 7 = sunday
days = {}
for i in range(1,8):
    days[i] = []

print(days)

start_day = 1 # 1 Jan 1900 is a monday
start_day = 2 # 1 Jan 1901 is a tuesday
total_days = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        for day in range(1, days_in_month(year, month) + 1):
            days[start_day].append(Date(day, month, year))
            start_day += 1
            total_days += 1
            if start_day == 8:
                start_day = 1

print(days)
print(start_day)
print(total_days)
print(days[7])
print(len(list(filter(lambda x: x.date == 1, days[7]))))
