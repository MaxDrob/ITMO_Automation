class Soda:
    def __init__(self, adding=None):
        self.adding = adding

    def show_my_drink(self):
        if self.adding:
            print(f"Soda and {self.adding}")

        else:
            print("Usual soda")


drink1 = Soda()
drink2 = Soda("Lime")
drink1.show_my_drink()
drink2.show_my_drink()
