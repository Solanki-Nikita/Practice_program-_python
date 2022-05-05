def area(r):
     return 3.14*r*r
def area(l,b):
    return l*b

radius= int(input("Enter the radius:"))
length=int(input("Enter the length of rectangle:"))
breadth=int(input("Enter the breadth of rectangle:"))
a=area(radius)
a1= areas(length,breadth)
print("Area of circle:",a,"\nArea of rectangle:",a1)
