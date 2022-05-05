#list of all divisors of that number

num= int(input("enter a number:"))
l=[]
for i in range(1,num//2+1):
    if(num%i==0):
        l.append(i)
print(l)
'''

'''##create a program to find the factorial of a user define integer

def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)


num = int(input("Enter any number:"))
result = factorial(num)
print("factorial is :",result)


