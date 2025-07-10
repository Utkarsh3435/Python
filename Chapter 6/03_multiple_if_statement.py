a= int(input("Enter your age: "))

# If statement no.1
if(a%2 == 0):
   print("a is even")
# End of if statement no.1

# If statement no.2
if(a>=18):
    print("You are eligible to vote")
    print("Congrats")

elif(a<0):
    print("Your age is invalid")

else:
    print("You are not eligible")
    print("Oops")
# End of if statement no.2

print("End of program")