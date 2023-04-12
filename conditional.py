physics=int(input("Enter the marks of physics:"))
chemistry=int(input("Enterthe marks of chemitry:"))
maths=int(input("Ener the mark of maths:"))

total= physics+chemistry+maths
persentage=float(total/3)

if(persentage>33 and physics>40 and chemistry>40 and maths>40):
    print("The candidate is pass!!!!")
else:
    print("The candidate is Fail!!!!")



