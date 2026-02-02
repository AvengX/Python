class Employee:
    start_time="6am"
    end_time="2pm"

    def change_time(self,new_time):
        self.end_time=new_time

class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject

class AdminStaff(Employee):
    def __init__(self,role):
        self.role=role

t1=Teacher("Maths")
t1.change_time("10am")
print(t1.subject,t1.start_time,t1.end_time)  

staff1=AdminStaff("Clerk")
print(staff1.role,staff1.start_time,staff1.end_time) 

      