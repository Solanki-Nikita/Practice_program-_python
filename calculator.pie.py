#welcome to my computer
#This function addition two numbers
def add(a,b):
    return a+b
#This function substraction two numbers
def subtracts(a,b):
    return a-b
#This function Division two numbers
def multiply(a,b):
    return a/b
#This function Multiplication two numbers
def divide(a,b):
    return a*b
#This function modulo two numbers
def modulo(a,b):
    return a%b

print("In which type do you want to take number")
print("""1. int
         2. float""")
type = int(input ("Enter your choice 1 or 2:"))

if type==1:
     num1 = int(input("Enter your  first number:"))
     num2 = int(input("Enter your second number:"))
if type==2:
     num1 = float(input("Enter your  first number:"))
     num2 = float(input("Enter your second nunber:"))
print("which opertor do you want to perform :")
print("""choose operator :
        1. Addition
        2. Substraction
        3. Division
        4. Multipication
        5. modulo""")
print("""Enter      + for Addition
            - for substraction
            / for Division
            * for Multipication
            % for modulo """)
optr = (input())
if optr == "+":
        result = addition(num1,num2)
        print("Result : a+b = ",result)

if optr == "-":
        result = substraction(num1,num2)
        print("Result : a-b = ",result)

if optr == "*":
        result = Division(num1,num2)
        print("Result : a/b = ",result)

if optr == "/":
        result = multiplication(num1,num2)
        print("Result : a*b = ",result)

if optr == "%":
        result = modulo(num1,num2)
        print("Result : a%b = ",result)
    
























