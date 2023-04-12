class complex:
    def __init__(self,r,i):
        self.real=r
        self.imagenary=i
    
    def __add__(self,c):
        return complex(self.real+c.real,self.imagenary+c.imagenary)
    
    def __str__(self):
        return f"{self.real}i+{self.imagenary}j"

num1=complex(4,5)
num2=complex(5,7)
print(num1+num2)
