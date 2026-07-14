# This is the sing file for the learning python and quzing entrance exam for Bsc.CSIT.
# It also helps improve the typing speed so I will be typing the code and also learning python and quzing entrance exam for Bsc.CSIT.

#People data 

name = input("Please enter your name: ")
age = input("Please enter your age: ")
height = input("Please enter your height in cm: ")
is_student = input("Are you a student? (yes/no): ")

print("name: " + str(name))
print("age: " + str(int(age)))
print("height: " + str(int(height)))    
print("is_student: " + str(is_student))

#   STRING OPERATIONS

greeting = "Hello," + name
print(greeting)
print(len(name))
print(name.upper())
print(name.lower())
print(name[0])

print(name[-1])
print(name[0:3])
print(f"My name is {name} and I am {age} years old.")

#   arithmetic operations

a = 10 
b = 3 
print("Addition: " + str(a + b))
print("Subtraction: " + str(a - b))
print("Multiplication: " + str(a * b))
print("Division: " + str(a / b))
print("Modulus: " + str(a % b))
print("Exponentiation: " + str(a ** b)) 

#  Comparison operations

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# logical 

print(True and False)
print(True or False)
print(not True)

# conditional statements

marks = (input("DeprecationWarning: Please enter your marks: "))
marks = int(marks)

if marks >= 90:
    print("You got an A grade.")
elif marks >= 80:
    print("You got a B grade.")
elif marks >= 70:
    print("You got a C grade.")
elif marks >= 60:       
    print("You got a D grade.")
else:
    print("You got an F grade.")    

#   loops 

for i in range(5):  # for loop 
    print(i)

for i in range (1, 11, 2):  #for loop with range 9 start, stop, step)
    print(i)

count = 0
while count < 5:    #while loop 
    print("Count:", count)
    count+= 1

for i in range (20):     # break and continue 
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")  

# lists 

