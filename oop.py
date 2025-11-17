# define a class

class student:


    # define a constructor
    def __init__(self,name,score):
        self.name=name
        self.score=score

    # define a method
    def display(self):
        print(f"Name:{self.name} Score:{self.score}")

    # define a method to check if student passed
    def check_pass(self):
        return self.score >=50

    # create objects
s1 = student("francis", 85)
s2 = student("jessinta", 40)

# use methods
print(f"passed status:{s2.check_pass()}")