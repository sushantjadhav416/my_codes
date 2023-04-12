import random

def game(a,b):
    if b!='s' and b!='w' and b!='g':
        print("invalid input!!")
    elif a=='s' and b'w':
        
        return False
    elif a=='s' and b=='g':
        return True
    elif a=='w' and b=='s':
        return True
    elif a=='w' and b=='g':
        return False
    elif a=='g' and b=='w':
        return True
    elif a=='g' and b=='s':
        return False
    elif a==b:
        return None

randno=random.randint(1,3)
#print(randno)
if randno==1:
    com='s'

elif randno==2:
    com='w'
elif randno==3:
    com='g'

player=input("Enter the input:")
reult=game(com,player)
print("com choose=",com)
print("You choose=",player)


if reult==True:
    print("You won!!!!")
elif reult==False:
    print("You lose!!!")
elif  reult==None:
    print("the game is draw!!")
