class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def RectangleArea(self):
        return self.l * self.b


R1 = Rectangle(3, 4)
print("Rectangle Area is: ", R1.RectangleArea())
R2 = Rectangle(10.5, 6.2)
print("Rectangle Area is: ", R2.RectangleArea())
