N1=int(input("Enter the inputs:"))
N2=int(input("Enter the inputs:"))
class number:
    def __init__(self,num):
       self.num =num

    def __add__(self,num2):
        print("Lets add!")
        return self.num + num2.num
    def __sub__(self,num2):
        print("Lets substarct")
        return self.num - num2.num
    def __mul__(self,num2):
        print("Lets multiply!")
        return self.num * num2.num
    def __str__(self):
       return f"The numbers are:{self.num}"
       

    
n1=number(N1)
n2=number(N2)
print(n1)
print(n2)
sum=n1+n2
print(sum)
sub=n1-n2
print(sub)
mul=n1*n2
print(mul)
