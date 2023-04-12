class c2d:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"

class c3d(c2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    
    def __str__(self):
         return f"{self.icap}i+{self.jcap}j+{self.kcap}k"


number=c2d(2,3)
print(number)
number=c3d(1,2,3)
print(number)



