import math
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def get_area(self):
        return math.pi * self.radius ** 2
    
    def get_perimeter(self):
        return self.get_circumference()
    
    def get_circumference(self):
        return 2 * math.pi * self.radius

circle1 = Circle(0, 0, 12)
print(f"Area: {circle1.get_area()}")            
print(f"Perimeter: {circle1.get_perimeter()}")  
print(f"Circumference: {circle1.get_circumference()}") 
