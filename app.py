name = "kija"
age = 18
print("My name is " + name + " and I am " + str(age) + " years old.")

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

print ("Hello how are you ?")
condition = input("Please enter your condition: ")
condition = str(condition)

if condition == "good":
    print("That's great to hear!")
elif condition == "bad":
    print("I am here for you. If you want to talk I can listen.")
elif condition == "nothing":
    what_happened = input("Please tell me what happened: ")
    print("Thank you for sharing. I hope things get better for you.")
else:
    print("I see. Thank you for sharing your condition with me.")

#html combined 
# render_template = f"""
# <h1>My name is {name} and I am {age} years old.</h1>
# <p>I am {height}cm tall and I weigh {weight}kg.</p>
# <p>Next year I will be {next_year_age} years old.</p>
# <p>{additional_info}</p>
# <p>My BMI is {bmi}.</p>
# """
# print(render_template)

# from flask import Flask, render_template 
# app = Flask(__name__)   
# @app.route("/")
# def index():
#     return (render_template)
# app.run(debug=True)
