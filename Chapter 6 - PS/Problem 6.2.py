marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

# Check for total percentage
total_percentage = (marks1 + marks2 + marks3)*100/300
print("Percentage is: ", total_percentage)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("The student is Passed")

else:
    print("The student is Failed")