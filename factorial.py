#program for factorial
n=int(input("Enter the number to calculate factorial: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of {} is : {}".format(n,fact))
