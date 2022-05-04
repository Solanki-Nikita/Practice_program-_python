class circle:
    def __init__(self):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius
r=int(input("Enter radius"))
c1=circle(r)
a=c1.area()
print(a)
c=c1.circumference()
print(c)
