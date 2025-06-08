class Student:

    # properties
    def __init__(self,name,std,percentage):
        self.name=name
        self.std=std
        self.percentage=percentage

    # method - 1
    def student_details(self):
        return f"Name of the student is {self.name}, std {self.std} has {self.percentage} Percentage."

# object name is student1
student1=Student("Mansoon Mohanty", 9, 98)
student2=Student("Ayush Mohanty", 2, 83)

# call the method and object
print(student1.student_details())

# call only name and std
print(student2.name,student2.std)


# Polymorphism -> Hiding unnecessary details from users through class and methods...
#              -> Only necessary part will be shown to user and others like calculation will be hidden