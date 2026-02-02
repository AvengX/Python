class Teacher:
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,gpa):
          self.gpa=gpa

class TA(Teacher,Student):
    def __init__(self,salary,gpa,name):
            Teacher.__init__(self,salary)  # super().__init__(salary)
            Student.__init__(self,gpa)
            self.name=name

tal1=TA(15_000,9.3,"Ayush") 
print(tal1.name,tal1.gpa,tal1.salary)      
