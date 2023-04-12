def sum(n):
    if n==0 :
       return 1
    return sum(n-1)+n
        
n1=int(input("Enter the number:"))
s=sum(n1)
print('Total sum is:',s)


