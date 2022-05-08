'''# Python Program to check character is Lowercase or Uppercase

ch = input("Please Enter Your Own Character : ")

if(ch.isupper()):
    print("The Given Character ", ch, "is an Uppercase Alphabet")
elif(ch.islower()):
    print("The Given Character ", ch, "is a Lowercase Alphabet")
else:
    print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")'''




##Python Program to check character is Lowercase or not using ASCII Values


ch = input("Please Enter Your Own Character : ")

if(ord(ch) >= 65 and ord(ch) <= 90): 
    print("The Given Character ", ch, "is an Uppercase Alphabet") 
elif(ord(ch) >= 97 and ord(ch) <= 122):
    print("The Given Character ", ch, "is a Lowercase Alphabet")
else:
    print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")
