# class Teacher():
#     def get_designation(self):
#         print("designation=Teacher")

# class Accountant():
#     def get_designation(self):
#         print("designation=Accountant")
# t1=Teacher()
# t1.get_designation()
# acc1=Accountant()
# acc1.get_designation()
class Dog:
    def speak(self):
        print("Bark")
class Cat:
    def speak(self):
        print("Meow")
class Robot:
    def speak(self):
        print("Beep Boop")
def make_it_speak(entity):
    entity.speak() # doesn’t care about type
d = Dog()
c = Cat()
r = Robot()
for e in [d, c, r]:
    make_it_speak(e)