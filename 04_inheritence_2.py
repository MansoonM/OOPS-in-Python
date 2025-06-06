class Parent:
    # property
    def __init__(self,name,age,how_many_kid):
        self.name=name
        self.age=age
        self.kid=how_many_kid

    # methods
    def display(self):
        return f"✨I am {self.name}. I am {self.age} years old. I have {self.kid} kids."
        
p=Parent("Sasmita",51,2)
print(p.display())

class Child(Parent):
    def __init__(self,child_name,child_age,how_many_sibilings,name,age,how_many_kid):
        self.c_name=child_name
        self.c_age=child_age
        self.sibilings=how_many_sibilings
        super().__init__(name,age,how_many_kid)
    
    def display_child(self):
        return f"🚀Parent name is {self.name}. Parent's age is {self.age}. Parent have {self.kid}. I am {self.c_name}. I am {self.c_age} years old. I have {self.sibilings} sibilings."

c=Child("Mansoon",21,1,"Sasmita",51,2)
print(c.display_child())