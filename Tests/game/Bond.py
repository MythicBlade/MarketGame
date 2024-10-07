from Investment import *

class Bond(Investment):
    def __init__(self,name: str, value: float, description: str,rate: float, minimimPayment: float):
        super().__init__(name, value, description)
        self.rate = rate
        self.minimumPayment = minimimPayment
        self.totalPayments = 0


    #updates the state of the bond for one step forward in time. 
    #returns the payment recieved
    def update(self,world) -> float:
        payment = 0
        if (self.value * (1+self.rate)) >= self.minimumPayment:
            self.value = (self.value * (1+self.rate))-self.minimumPayment
            payment = self.minimumPayment
        else:
            payment = (self.value * (1+self.rate))
            self.value = 0
        self.history.append(self.getprice())
        if self.value == 0:
            self.delete = True
        self.totalPayments += payment
        return payment