class Product:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1

    def get_info(self):
        print(f"price {self.name} is Rs.{self.price}") 

    @classmethod
    def get_count(cls):
        print(f"total products in store={cls.count}")   

    @staticmethod
    def cal_discount(price,discount):
        print(f"Discounted price ={price-(price*discount/100)}")    


p1=Product("Phone",10_000)
p2=Product("Laptop",20_000)        
p1.get_info()
p2.get_info()

p1.cal_discount(10_000,10) #p1.cal_discount(p1.price,10) 

Product.get_count()