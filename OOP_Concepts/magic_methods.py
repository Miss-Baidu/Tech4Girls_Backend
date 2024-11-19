class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    
    @property
    def area(self):
        return self.length * self.width

    
    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    
    def __str__(self):
        return f"Rectangle(Length: {self.length}, Width: {self.width})"

    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False



rect1 = Rectangle(6, 4)
rect2 = Rectangle(4, 6)


print(rect1)              
print(f"Area of rect1: {rect1.area}")        
print(f"Perimeter of rect1: {rect1.perimeter}") 

print(rect2)             
print(f"Area of rect2: {rect2.area}")        
print(f"Perimeter of rect2: {rect2.perimeter}") 

print(f"Are rect1 and rect2 equal in area? {rect1 == rect2}") 
