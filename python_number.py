a=int(input("Enetr a first  number"))
b=int(input("Enetr a second  number"))
c=int(input("Enetr a third  number"))
if a==b==c:
    print("all values are equal")

if a==b and b<c:
        print("a and b is equal and c is greater than a and b ")

if b==c and b<a:
        print("b and c is equal and a is greater than b and c ")

if a==c and c<b:
        print("a and c is equal and b is greater than a and c ")


elif a>=b and a>=c:
    print(a,"is larger than",b,"and",c)

elif b>=a and c>=b:
    print("larger number is:",b)

elif c>=a and c>=b:
    print(" larger number is :",c)

    
