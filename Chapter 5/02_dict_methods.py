marks = {
    "Harry": 100,
    "Shubham": 23,
    "Rohan": 56
    
}

#print(marks.items()) 
#print(marks.keys()) 
#print(marks.values())
marks.update({"Harry": 99, "Renuka": 50})
#print(marks)

#print(marks.get("Harry2")) # Prints None
#print(marks["Harry2"]) # Returns Error

marks.pop("Harry", "default")
print(marks)

 