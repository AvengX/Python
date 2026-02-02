class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        info = f"Name: {self.name}"
        if self.age is not None:
            info += f", Age: {self.age}"
        if self.address is not None:
            info += f", Address: {self.address}"
        print(info)

p1 = Person("Rahul")
p2 = Person("Mohan", 20)
p3 = Person("Sohan", 22, "123 Street, Delhi")

p1.display()
p2.display()
p3.display()