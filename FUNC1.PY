def greatestnum(a,b,c):
    if(a>b and a>c):
        print('{} is greater!!!!!'.format(a))
    elif(b>a and b>c):
        print("{} is greater!!!!!".format(b))
    else:
        print("{} is greater!!!!!".format(c))

n1=int(input("Enter the number1:"))
n2=int(input("Enter the number2:"))
n3=int(input("Enter the number3:"))
greatestnum(n1,n2,n3)
