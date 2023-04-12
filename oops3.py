class employee:
     company="Google"
     def __init__(self,name,salary,subunit):
             self.name=name
             self.salary=salary
             self.subunit=subunit

     def details(self):
           
           print(f"*The name of employee\t{self.name}*")
           print(f"salary:{self.salary}")
           print(f"subunit:{self.subunit}")
           print("\n")

company="Google"
print(f"Empolyees of {company}!!!")
sushant=employee("sushant jadhav",30000,"Grad Y")
sushant.details()
viren=employee("viren shah",30000,"Grad E")
viren.details()
rohan=employee("Rohan patil",30000,'Grad Y')
rohan.details()







