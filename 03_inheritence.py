class parent:
    def __init__(self,father,mother):
        self.father=father
        self.mother=mother
    def name_of_parent(self):
        print(f"My father name is {self.father}")
        print(f"My mother name is {self.mother}")


first=parent("A Mohanty", "S Mohanty")
print(first.father,first.mother)

class child(parent):
   
    def __init__(self, father, mother,brother,me):
        self.brother=brother
        self.me=me
        super().__init__(father, mother)
 
    def display_members(self):
        print(f"My father name is {self.father} , mother name is {self.mother}, brother name is {self.brother}. My name is {self.me}")

first=child("A Mohanty", "S Mohanty", "Ayush Mohanty", "Mansoon Mohanty")
print(first.father,first.mother, first.brother, first.me)