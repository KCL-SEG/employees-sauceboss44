"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

# self.__dict__.update(kwargs)
class Employee:

    def __init__(self, name="", rate=0, payType="", hours=0, commissionType="", numOfContracts=0, commission = 0, ):
        self.name = name
        # SALARY/WAGE
        self.payType = payType
        # monthly salary total or hourly wage
        self.rate = rate
        # hours worked - relevant to wage only
        self.hours = hours
        # BONUS/CONTRACT
        self.commissionType = commissionType
        # commission amount
        self.commission = commission
        # only relevant to CONTRACT commission type
        self.numOfContracts = numOfContracts
        self.totalPay = 0
        self.calcTotalPay()
        self.explanationString = ""
        self.constructString()

    def get_pay(self):
        return self.totalPay

    def __str__(self):
        return self.explanationString

    def lookUpString(self, attribute):
        explanation = {"SALARY": f" works on a monthly salary of {self.rate}",
                       "WAGE": f" works on a contract of {self.hours} hours at {self.rate}/hour",
                       "BONUS": f" and receives a bonus commission of {self.commission}",
                       "CONTRACT": f" and receives a commission for {self.numOfContracts} contract(s) at {self.commission}/contract"}
        if attribute in explanation:
            return explanation[attribute]
        else:
            return ""
    def constructString(self):
        self.explanationString += self.name
        for (attributeName, attribute) in vars(self).items():
            self.explanationString += self.lookUpString(attribute)
        self.explanationString += "."
        self.explanationString += f"  Their total pay is {self.totalPay}."

    def calcTotalPay(self):
        if self.payType:
            if self.payType == "SALARY":
                self.totalPay += self.rate
            elif self.payType == "WAGE":
                self.totalPay += self.rate * self.hours
        if self.commissionType:
            if self.commissionType == "BONUS":
                self.totalPay += self.commission
            elif self.commissionType == "CONTRACT":
                self.totalPay += self.commission * self.numOfContracts

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', payType="SALARY", rate=4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',payType="WAGE",hours=100,rate=25)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',payType="SALARY",rate=3000,commissionType="CONTRACT",commission=200,numOfContracts=4)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',payType="WAGE",rate=25,hours=150,commissionType="CONTRACT",commission=220,numOfContracts=3)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',payType="SALARY",rate=2000, commissionType="BONUS", commission=1500)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',payType="WAGE",rate=30,hours=120,commissionType="BONUS",commission=600)
