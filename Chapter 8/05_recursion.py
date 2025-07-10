def fact(n):
    if(n==1) or (n==0):
        return 1
    else:
        return n*fact(n-1)
    
n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {fact(n)}")
# kist the factorial if 5 is 120 
# The factorial of 5 is 120 
# The factorial of 0 is 1 
# The factorial of 1 is 1 then 