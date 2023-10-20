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
ex = Square()