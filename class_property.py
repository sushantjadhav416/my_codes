class employee:
    company="BSNL"
    salary=50000
    bonus=10000
    @property
    def totalsalary(self):
        return self.salary+self.bonus
    @totalsalary.setter
    def totalsalary(self,val):
         self.bonus = val - self.salary

sushant=employee()
print(sushant.salary)
print(sushant.totalsalary)
sushant.totalsalary=60500
print(sushant.bonus)



