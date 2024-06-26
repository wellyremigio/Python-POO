import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)

c = Circle(2)

print(c.calculate_area())

