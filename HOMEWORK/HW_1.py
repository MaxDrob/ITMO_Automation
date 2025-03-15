# def task_1() -> None:
#     num = 10001
#     decimal = 9.1
#     text = "All your base are belong to us"
#     items = [10, 1000, 10000]
#     is_valid = True
#
#     print(num)
#     print(decimal)
#     print(text)
#     print(items)
#     print(is_valid)
#
# task_1()

# def task_2() -> list:
#     a = [1, 2, 3, 5, 8, 13, 21]
#     return a[:3]
#
# r = task_2()
# print(r)


# def task_3(num: int) -> int:
#     return num * num
#
# print(task_3(4))



#Лекция 2, задание 1

# Объявляем функцию task_1() с аннотацией возвращаемого типа
def task_1() -> None:
    i: int = 1000
    f: float = 9.16
    st: str = "This is a test task"
    l: list = [1, 3, 3, 4, 4]
    b: bool = True

    print(i, type(i))
    print(f, type(f))
    print(st, type(st))
    print(l, type(l))
    print(b, type(b))


task_1()
