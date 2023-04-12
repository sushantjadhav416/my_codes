class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getstatus(self):
        print("********************************")
        print(f"The train name : {self.name}")
        print(f"The total seats: {self.seats}")

    def Fare(self):
        print(f"The price of ticket is: {self.fare}")

    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked!!\n Your seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry this trian is full!!! kindly try in tatkal!!!")

sivaneri=train("sivaneri",200,100)
sivaneri.getstatus()
sivaneri.Fare()
sivaneri.bookticket()

sivaneri.getstatus()
sivaneri.Fare()
sivaneri.bookticket()

sivaneri.getstatus()
sivaneri.Fare()
sivaneri.bookticket()

sivaneri.getstatus()
sivaneri.Fare()
sivaneri.bookticket()

sivaneri.getstatus()
sivaneri.Fare()
sivaneri.bookticket()

sivaneri.getstatus()
sivaneri.Fare()
sivaneri.bookticket()

sivaneri.getstatus()
sivaneri.Fare()
sivaneri.bookticket()

sivaneri.getstatus()
sivaneri.Fare()
sivaneri.bookticket()
