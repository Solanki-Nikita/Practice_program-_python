## method overlaoding........


class A:
  def area(self,r=None,l=None,b=None):
    if(r!= None and l==None and b==None):
         ar=3.14*r*r
         return ar
    elif(r!=None and l!= None and b==None):
        a=l*r
        return a
    else:
        print("No value provide")
a=A()
y=a.area(2)
print("Area of circle",y)
x=a.area(3,4)
print("Area of Rectangle",x)
