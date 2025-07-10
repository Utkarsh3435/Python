'''def nsum():
    n = int(input("Enter a number: "))
    sum = 0
    for i in range(1,n+1):
        sum+=i
    print(f"Sum of {n} natural nos is: {sum}")

nsum()'''

def sum(n):
    if(n==1):
        return 1
    else:
        return (n + sum(n-1))

print(sum(5))   