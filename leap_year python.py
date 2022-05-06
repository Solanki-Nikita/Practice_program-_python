print("-------- Welcome to my leap year checking program --------") 
x = int(input("Enter the year for checking:"))  

if x is x%400 == 0 and x%100 == 0 :  
    print("{} is leap year ".format(x))
elif x%4 == 0 and x%100!= 0: 
    print("{} is leap year ".format(x)) 
else: 
        print("{} is not leap year ".format(x)) 
