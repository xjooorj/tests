import math

class shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius   


class Rectangle(shape):
    def __init__(self, lenth, width):
        self.lenth = lenth
        self.width = width

    def __eq__(self,other):
        if not isinstance(other, Rectangle):
            return False
        return self.lenth == other.lenth and self.width == other.width


    def area(self):
        return self.lenth * self.width

    def perimeter(self):
        return (self.lenth * 2) + (self.width * 2)
    

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)    
                 