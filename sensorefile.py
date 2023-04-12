words=["donkey","mote","chutiye"]
with open("info.txt") as f:
     content=f.read() 

for word in words:  
    content = content.replace(word,"##@#@") 
    with open("info.txt",'w') as f:
       f.write(content)

 
     