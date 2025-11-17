def myfunction():
    print("This is my  first function")

myfunction()


# function with parameters
def students(name, age, gender):
    print("students name is {name}")
    print("students age is {age}")
    print("students gender is {gender}")

students("iano",20, "Male")
students("shekii", 23,  "Female")

# functions with return values
def add_numbers(a,b):
    return a+b
result = add_numbers(1,2)
print(F"the sum is {result}")
