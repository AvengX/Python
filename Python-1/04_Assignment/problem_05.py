class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display_info(self):
        print(f"Vehicle:{self.brand}{self.model}")   

class car(Vehicle):
    def __init__(self,brand,model,seats):
        self.seats=seats
        Vehicle.__init__(self,brand,model)

    def  display_info(self):
        print(f"Bike:{self.brand} {self.model} {self.seats}")   

class bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        self.engine_cc=engine_cc
        super().__init__(brand,model)

    def  display_info(self):
        print(f"Bike:{self.brand} {self.model} {self.engine_cc}")   

my_car=car("Honda","City",5)
my_bike=bike("BMW","S-series",250)        

my_car.dipplay_info()
my_bike.display_info()






