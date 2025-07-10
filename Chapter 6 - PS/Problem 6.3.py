p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

a = str(input("Type your Comment: "))

if((p1 in a) or (p2 in a) or (p3 in a) or (p4 in a)):
    print("Spam Detected!!")

else:
    print("Thanks for your Comment")

