class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"Колір фігури - {self.color}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_rectangle(self):
        print(f"Колір цього прямокутника - {self.color}, ширина - {self.width}, висота - {self.height}")

pryamokutnyk1 = Rectangle("червоний", 5, 7)
pryamokutnyk1.display_rectangle()



