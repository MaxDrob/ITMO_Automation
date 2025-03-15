
#task_1
def find_max_number(num1, num2):

    if num1 > num2:
        print("Greater number:", num1)
    else:
        print("Greater number:", num2)

find_max_number(19, 21)

#===================

#task_2

def diff_135(num1, num2):

    if num1 - num2 == 135 or num2 - num1 == 135:
        print("yes")
    else:
        print("тo")

diff_135(150, 15)

#======================

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