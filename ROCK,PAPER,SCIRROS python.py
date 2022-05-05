##Enhance the rock paper scissors game for (player vs computer) codition

#from ctypes.wintypes import Point import random;
round = int(input("How many round do you want to play:"))
point = 0

for i in range(Round):
    print("\n\n*****************Round",i+1,"*******************\n\n")
    sys = random.randint(1,3)
    print("""
          Rock : 1
          Paper : 2
          scissor : 3
          """)

    user = int(input("Enter your choise :"))
    print()

    if(sys == 1):
        print("player1 = Rock")
    elif(sys == 2):
        print("player2 = Paper")
    elif(sys == 3):
        print("player3 = Scissor")


    print()

    if(user == 1):
        print("YOU = Rock")
    elif(user == 2):
        print("YOU = Paper")
    elif(user == 3):
        print("YOU = scirros")
    else:
        print("invalid choise")

    print()
    print()

    if(user == 3 and sys == 1):
        print("***************YOU LOSE*************")

    elif(sys == user):
        print("***************YOU LOSE*************")

    elif(sys == user):
        print("***************DRAW*************")

    elif(sys < user and(user ==1 or 2 or 3)):
        print("*************YOU WIN************")
        point=point+1

print("\n\n***********YOUR SCRORE = ",point,"************\n\n")
    
    
