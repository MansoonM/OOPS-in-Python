class student_2:

    # data/ properties
    def __init__(self,id,name,fee):
        # attributes
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
# It is a special method within a class that get automatically called when object is created.

# It is used to initiate the attributes of the object.

#Constructor is written with " __init__"