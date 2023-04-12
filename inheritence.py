class employee:
    company="TCSL"

    def showdetails(self):
        print(f"This is an employee of {self.company}")

class language(employee):
    language="python"
   
    def getlanguage(self):
        print(f"His language of programing is {self.language}")

sushant=employee()
sushant=language()
sushant.showdetails()
sushant.getlanguage()