n = int(input("Enter the number: "))
p = 1
for i in range(1,n+1):
    p*=i

print("The factorial of",n,"is",p)
