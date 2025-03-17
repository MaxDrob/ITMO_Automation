class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle1 = Rectangle(9, 10)
rectangle2 = Rectangle(3, 9)
rectangle3 = Rectangle(8, 12)


print(f"Rectangle1: Area = {rectangle1.area()}, Perimeter = {rectangle1.perimeter()}")
print(f"Rectangle2: Area = {rectangle2.area()}, Perimeter = {rectangle2.perimeter()}")
print(f"Rectangle3: Area = {rectangle3.area()}, Perimeter = {rectangle3.perimeter()}")


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        if self.b != 0:
            print(self.a / self.b)
        else:
            print("Division by zero is prohibited")

    def subtraction(self):
        print(self.a - self.b)


math = Math(10, 5)


math.addition()
math.multiplication()
math.division()
math.subtraction()


#Task 3

class Button:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""  #пустой

    def click(self):
        print(f"Клик по кнопке: {self.text}")


textbox = Button("Text Box")
checkbox = Button("Check Box")
radiobutton = Button("Radio Button")
webtables = Button("Web Tables")
buttons = Button("Buttons")
links = Button("Links")
brokenlinks = Button("Broken Links - Images")
upload = Button("Upload and Download")
dynamic = Button("Dynamic Properties")

#текст для каждой кнопки
print(f"Текст кнопки: {textbox.text}")
print(f"Текст кнопки: {checkbox.text}")
print(f"Текст кнопки: {radiobutton.text}")
print(f"Текст кнопки: {webtables.text}")
print(f"Текст кнопки: {buttons.text}")
print(f"Текст кнопки: {links.text}")
print(f"Текст кнопки: {brokenlinks.text}")
print(f"Текст кнопки: {upload.text}")
print(f"Текст кнопки: {dynamic.text}")

# вызов "клик" для каждой кнопки
textbox.click()
checkbox.click()
radiobutton.click()
webtables.click()
buttons.click()
links.click()
brokenlinks.click()
upload.click()
dynamic.click()



#Задача 4

class Car:

    def __init__(self):
        self.color = ""
        self.type = ""
        self.year = None


    def run(self):
        print("Авто заведен")


    def norun(self):
        print("Авто заглушен")


    def set_year(self, year):
        self.year = year
        print(f"Год выпуска: {self.year}")

    # Метод 4: Присвоение типа автомобиля
    def set_type(self, type):
        self.type = type
        print(f"Тип авто: {self.type}")

    # Метод 5: Присвоение цвета автомобиля
    def set_color(self, color):
        self.color = color
        print(f"Цвет: {self.color}")


car = Car()


car.set_year(2010)
car.set_type("Седан")
car.set_color("Красный")


car.run()
car.norun()