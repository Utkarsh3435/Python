import random

print("Welcome to Snake, Water, Gun Game")
print("Enter s for Snake, w for Water, g for Gun, e to Exit")

youdict = {"s":1, "w":0, "g":-1}

while True:
    youstr = input("Enter your choice: ")
    if youstr == "e":
        print("Exiting Game!")
        break
    elif youstr not in youdict.keys():
        print("Invalid Input! Try Again")
        continue            

    computer = random.choice([-1,0,1])
    you = youdict[youstr]
    reverseDict = {1:"Snake", 0:"Water", -1:"Gun"}
    print(f"You chose: {reverseDict[you]} \nComputer chose: {reverseDict[computer]}")

    if(computer-you==1 or computer-you==-2):
        print("Computer Wins!")
    elif(computer-you==-1 or computer-you==2):
        print("You Win!")
    else:
        print("Its a Draw!")