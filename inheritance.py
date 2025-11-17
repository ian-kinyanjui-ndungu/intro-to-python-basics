#Inheritance

class Person:      #parent class
    def __init__(self,name):
        self.name=name

    def great(self):
        print(f"hello my name is {self.name}")

class Teacher(Person): #inherits from class person
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject

    def tutor(self):
            print(f"{self.name} is teaching {self.subject}")

class Student(Person):     #inherits from class person
    def __init__(self,name, grade):
        super(). __init__(name)
        self.grade=grade

    def study(self):
        print(f"{self.name} is studying {self.grade}")

t1=Teacher("Maina","Chemistry")
t1.tutor()

s1=Student("Iano", "grade 10")
s1.study()