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
    
    @staticmethod
    def cal_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"discounted_price={final_price}")    

L1=Laptop("16gb","512gb")
L1.cal_discount(40_000, 10)
     