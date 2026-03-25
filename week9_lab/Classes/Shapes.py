# Shapes exercise


import math


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
       
    def area(self):
        return self.width * self.heigth    

    def perimeter(self):
        return 2 * self.width + 2 * self.heigth
    
    def __str__(self):
        return f"Rectangle W= {self.width} H= {self.heigth}"

class Cirle():
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * self.radius * math.pi

# class Cylinder():
#     def __init__(self, heigth, radius, surface_area):     ####### To fix this!!!!
#         self.heigth = heigth 
#         self.radius = radius 
#         self.surface_area = surface_area

if __name__ == '__main__':
    x = Rectangle(5,8)
    print (x)
    print (x.area())
    print (x.perimeter())