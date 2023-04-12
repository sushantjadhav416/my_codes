class vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=1
        for i in self.vec:
            str1+= f" {i} {index} +"
            index +=1 
        return str1[:-1]
    
    def __add__(self,vec2):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
        return vector(newlist)

    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    
    def __len__(self):
        return len(self.vec)


v1=vector([1,2,3])
v2=vector([5,4,3])
print("vector 1:",v1)
print("vector 2:",v2)
print("Length of V1:",len(v1))
print("Length of V2:",len(v2))
print("Vector Addition:",v1+v2)
print("Vector Multiplication:",v1*v2)
print("Length of V1:",len(v1))
print("Length of V2:",len(v2))

        
        


