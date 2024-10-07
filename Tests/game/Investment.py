class Investment:
    def __init__(self,name: str, value: float, description: str):
        self.delete = False
        self.name = name
        self.value = value
        self.description = description
        self.history = []
        self.quantity = 0
        self.costBasisAvg = 0
   
        
    #updates the state of the item for one step forward in time.
    # returns the payment recieved 
    def update(self,world) -> float:
        self.history.append(self.getprice())
        return 0
    
    #returns the price that the item is currently selling for no arguments
    def getprice(self)-> float:
        return self.value

    #returns a list of historical prices for the asset
    def gethistory(self)-> list:
        return self.history
        
    #returns the total increase that the investment has had over it's purchase price
    def getIncrease(self) -> float:
        return ((self.getprice() * self.quantity) - (self.costBasisAvg * self.quantity))
    
    #Takes in an amount and returns the price that was required to buy that amount
    def buy(self,amount: float) -> float:
        total = amount * self.getprice()
        buyTotal = self.quantity *self.costBasisAvg
        self.quantity += amount
        self.costBasisAvg = (total + buyTotal)/self.quantity
        return total

    #takes in an amount to sell and returns the total that it was sold for
    #raises @InsufficientQuantityError if there are not enough of the investment owned
    def sell(self,amount: float) -> float:
        if amount > self.quantity:
            raise InsufficientQuantityError()
        else:
            total = amount * self.getprice()
            self.quantity -= amount
            return total

class InsufficientQuantityError(Exception):
    pass
