name = "kija"
age = 18
print("My name is " + name + " and I am " + str(age) + " years old.");

height = 170
weight = 67
print("I am " + str(height) + "cm tall and I weigh " + str(weight) + "kg .")

next_year_age = age + 1
print("Next year I will be " + str(next_year_age) + " years old.")

additional_info = "I am a student and I love programming."
print(additional_info)

# let's calculate BMI
bmi = weight / ((height / 100) ** 2)
print("My BMI is " + str(bmi) + ".")    

your_age = input("Please enter your age: ")
your_age = int(your_age)

if your_age < age:
    print("You are younger than me.")
elif your_age > age:
    print("You are older than me.")
else:
    print("We are the same age!")

print ("Next year you will be " + str(your_age + 1) + " years old.")