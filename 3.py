class Shape():
    def area(self):
        self.Area=0
class Square(Shape):
    def __init__(self):
        self.length=int(input())
        self.Area=self.length*self.length
        self.area()
    def area(self):
        print(self.Area)
class Rectangle(Shape):
    def __init__(self):
        self.length=int(input())
        self.width=int(input())
        self.Area=self.length*self.width
        self.area()
    def area(self):
        print(self.Area)

ex = Rectangle()