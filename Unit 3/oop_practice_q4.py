class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (2*self.length) + (2*self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

def shape_area(shape):
    return shape.area()

def shape_perimeter(shape):
    return shape.perimeter()

rect1 = Rectangle(3,4)
rect2 = Rectangle(1,10)
print(rect1.area())
print(rect1.perimeter())

circle1 = Circle(4)
circle2 = Circle(2)
print(circle1.area())
print(circle1.perimeter())

print("-" * 10)
print(shape_area(rect1))
print(shape_area(circle1))
print("-" * 5)
print(shape_perimeter(rect1))
print(shape_perimeter(circle1))