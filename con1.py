text=input("Enter text:")
spam=False
if("make a lot money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click ths" in text):
    spam=True
elif("subscribe this" in text):
    spam=True

if(spam):
    print("Its a spam!!!")
else:
    print("Its a not a spam!!!")