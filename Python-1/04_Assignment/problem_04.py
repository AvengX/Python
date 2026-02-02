class Shape:
    def area(self):
        pass

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

class rectangle(Shape):
    def __init__(self,length,breadth):   
        self.length=length
        self.breadth=breadth         

    def area(self):
        return self.length*self.breadth

class triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5*self.base*self.height

shapes=[circle(4),rectangle(5,5),triangle(4,10)]
for s in shapes:
    print(f"The area of the {type(s).__name__} is : {s.area():.2f}")        


