from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        return "Stipend:$500 per month"

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return "Stipend:$700 per month+benefits"

class ContractEmployee(Employee):
    def calculate_salary(self):
        return "Stipend:$50 per hour"

employees=[
    Intern("Ayush"),
    FullTimeEmployee("Navya"),
    ContractEmployee("Aryan")
]

for emp in employees:
    print(f"{emp.name}({type(emp).__name__}):{emp.calculate_salary()}")
