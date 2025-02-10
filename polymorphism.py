class Shape:
    def draw(self):
        print("drawing a shape")

class Rectangle(Shape):
    def draw(self):
        print("drawing a rectangle")

class Square(Shape):
    def draw(self):
        print("drawing a square")

sh = Shape()
sh.draw()
r = Rectangle()
r.draw()
s = Square()