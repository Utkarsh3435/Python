def i2c(i):
    return i*2.54

n = int(input("Enter value in inches: "))
print("Value in centimeters:",i2c(n))