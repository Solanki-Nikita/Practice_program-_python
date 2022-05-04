 # area of cricle
'''print("This program is to find the area of circle ")
radius=int(input("Enter a radius of circle."))
area=22/7*radius*radius
print("Area of circle is:",area)



#using function
print("This program is to find the area of circle ")
def circle_area(r):
    a=22/7*r*r
    return a

radius=int(input("Enter the radius of circle:"))
area=circle_area (radius)
print("Area of circle is :",area)'''

#find Round of Area of circle

print("This program is to find the area of circle ")
 
def circle_area(r):
    a=22/7*r*r
    return a
radius=int(input("Enter the radius of circle:"))
area=circle_area (radius)
area= round(area,3)
print(area)
