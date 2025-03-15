
#task_2
def find_max_number(num1, num2):

    if num1 > num2:
        print("Greater number:", num1)
    else:
        print("Greater number:", num2)

find_max_number(19, 21)

#===================

#task_3

def diff_135(num1, num2):

    if num1 - num2 == 135 or num2 - num1 == 135:
        print("yes")
    else:
        print("тo")

diff_135(150, 15)

#======================

#task_4

def season_of_the_year(month):
    if month == 12 or month == 1 or month == 2:
        print("winter")
    elif month == 3 or month == 4 or month == 5:
        print("spring")
    elif month == 6 or month == 7 or month == 8:
        print("summer")
    elif month == 9 or month == 10 or month == 11:
        print("Autumn")
    else:
        print("We ain't yet on Mars, sadly")


season_of_the_year(13)

#======================

#task_5

def numbers(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        print("yes")
    else:
        print("no")

numbers(3, 9, 18)

#======================

#task_6

def positive_count(num):
    count = 0
    for num in num:
        if num > 0:
            count += 1
    print("Positive numbers:", count)

positive_count([1, 2, 3, -100, -500])

#======================

#task_7

def day_calculus(y, m):
    days = y * 12 * 29 + m * 29
    print("Total amount of days in a given period of time is: ", days)

day_calculus(100, 100)