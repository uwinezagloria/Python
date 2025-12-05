class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self) :
        area=self.length*self.width
        return f"area of rectangle is {area}"
length=int(input("Enter the length of triangle: ")) 
width=int(input("Enter the width of rectangle "))
rec1=Rectangle(length,width)
print(rec1.area())
       
        
        