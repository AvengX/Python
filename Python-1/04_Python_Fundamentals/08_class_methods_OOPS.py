class Laptop:
    storage_type="SSD"

    def __init__(self,RAM,Storage):
        self.RAM=RAM
        self.Storage=Storage
        
    @classmethod
    def get_storage_type(cls):
        print(f"storage type={cls.storage_type}")    

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.Storage} {self.storage_type}")
L1=Laptop("16gb","512gb")
L2=Laptop("8gb","256gb")
L1.get_storage_type()       