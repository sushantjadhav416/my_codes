class programer:
    company="microsoft"
    def __init__(self,name,product):
         self.name=name
         self.product=product
    def getinfo(self):
        print(f"The {self.company} programer is {self.name} and he/she is working on {self.product} project")

sushant=programer("sushant","skype")
viren=programer("viren","Github")
sushant.getinfo()
viren.getinfo()



