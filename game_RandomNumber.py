import random
print("!!!!!!Guess The number!!!!!")
rnum= random.randint(1,100) 
#print(n1)
userguesses=0
guess=None

while (guess!=rnum):
    guess=int(input("Enter you guess:"))
    userguesses += 1
    if (guess==rnum):
       print("***You guessed it right***!!!")
    else:
        if (guess>rnum):
             print("sorry,your guess is wrong,enter smallar number")
        else:
            print("sorry,your guess is wrong,enter greater number")

print(f"YOU guesssed in {userguesses} attempts")
with open('highscore.txt','r') as f:
    higestscore = int(f.read())
if(userguesses<higestscore): 
    print("You have just broken your high score!!")
    with open('highscore.txt','r') as f:

       f.write(str(userguesses))