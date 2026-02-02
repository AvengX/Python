class Student:
    def __init__(self,name,roll_no,marks):
        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks

    def get_name(self):
        return self.__name

    def get_roll(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    def set_name(self,name):
        if name!=" ":
            self.__name=name
        else:
            print("name cannot be empty")

    def set_roll(self,roll_no):
        if 1<=roll_no<=100:
            self.__roll_no=roll_no
        else:
            print("Invalid roll number")

    def set_marks(self,marks):
        if marks<0:
            print("Marks cannot be negative")
        else:
            self.__marks=marks                       

stu = Student("Ayush", 123, 10) 
print("--- Student Details ---")
print("Name:", stu.get_name())
print("Roll No:", stu.get_roll())
print("Marks:", stu.get_marks())

# Test a setter and print again
stu.set_marks(95)
print("Updated Marks:", stu.get_marks())