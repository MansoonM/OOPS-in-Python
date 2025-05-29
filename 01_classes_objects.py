# way 1 : direct data 
class student:

    # data/ properties
    def putdata(self):
        self.id=1
        self.name="Mansoon"
        self.fee=12000
    
    # method
    def display(self):
        print("Student id: ", self.id)
        print("Stuent Name: ",self.name)
        print("Student Fee: ",self.fee)
# create an object
a=student()
a.putdata()
a.display()


# break/spacee
print("------------------------------- ")

# way 2 User Input

class student_1:

    # data/ properties
    def putdata(self):
        self.id=int(input("Enter Student ID: "))
        self.name=str(input("Enter Student Name: "))
        self.fee=int(input("Enter Student Fee: "))
        print("    ")
    # method
    def display(self):
        print("Student id: ", self.id)
        print("Stuent Name: ",self.name)
        print("Student Fee: ",self.fee)
# create an object
b=student_1()
b.putdata()
b.display()


# way 3 with parameters
class student_2:

    # data/ properties
    def __init__(self,id,name,fee):
        self.id=id
        self.name=name
        self.fee=fee
        
    # method
    def display(self):
        print("Student id: ", self.id)
        print("Stuent Name: ",self.name)
        print("Student Fee: ",self.fee)

# create an object
first_student=student_2(1,"Moon",78000)

# execute objects
print(first_student.id)
print(first_student.name)
print(first_student.fee)

# ===========================notes==================================
# 💥class and object
# object is a real world entity

# The group of real world entities are called class
# class is like a blueprint or template

# objects are defined for two things: property/data and methods/functions
