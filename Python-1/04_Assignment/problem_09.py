class Herbivore:
    def __init__(self, veg):
        self.veg = veg

class Carnivore:
    def __init__(self, nonveg):
        self.nonveg = nonveg

class Omnivore:
    def __init__(self, veg_nonveg):
        self.veg_nonveg = veg_nonveg

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, veg, nonveg, veg_nonveg, sound):
        Herbivore.__init__(self, veg)
        Carnivore.__init__(self, nonveg)
        Omnivore.__init__(self, veg_nonveg)
        self.sound = sound

    def display(self):
        print(f"Bear eats: {self.veg}, {self.nonveg}, and {self.veg_nonveg}")
        print(f"Bear sound: {self.sound}")


bear = Bear("Berries", "Fish", "Both", "Growl")
bear.display()