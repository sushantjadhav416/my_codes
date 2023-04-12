print("!!!Calculator is on!!!!")
N1=int(input("Enter the number:\n"))
N2=int(input(" "))

class calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def sum(self):
        print(f"Addition:{self.n1}+{self.n2}={self.n1+self.n2}")

    def sub(self):
        print(f"Substraction:{self.n1}-{self.n2}={self.n1-self.n2}")

    def mul(self):
        print(f"Multiplication:{self.n1}*{self.n2}={self.n1*self.n2}")

    def div(self):
        print(f"Division:{self.n1}/{self.n2}={self.n1/self.n2}")
    
    @staticmethod
    def greet():
        print("Here is you all results!!!")


Input=calculator(N1,N2)
Input.sum()
Input.sub()
Input.mul()
Input.div()
Input.greet()
    