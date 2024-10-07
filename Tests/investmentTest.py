from game.Investment import *
from game.Investment import Bond


class Testing:
    def __init__(self):
        pass
    @staticmethod
    def investmentTest():
        des = 'This is a test of the class.\nThis description is deliberately weird'
        testInst = Investment(name='TestInvestment',value=1,description=des)

        assert(testInst.getprice() == 1)
        account = 100
        testInst.update([])
        testInst.update([])
        testInst.update([])
        assert(testInst.gethistory() == [1,1,1])
        account -= testInst.buy(99)
        assert(testInst.quantity == 99)
        try:
            testInst.sell(100)
        except(InsufficientQuantityError):
            pass
        else:
            raise AssertionError('Failed to raise error on illegal transaction')
        account += testInst.sell(90)
        assert(testInst.quantity == 9)
        testInst.value = 3
        account -= testInst.buy(5)
        testInst.value = 5
        n = testInst.getIncrease()
        account += testInst.sell(14)
        assert(n == (account - 100))
        
    @staticmethod
    def bondTest():
        des = 'This is a test of the bond.\nThis description is deliberately weird'
        testInst = Bond(name='TestBond',value=1000,description=des,rate=0.05,minimimPayemnt=100)

        assert(testInst.getprice() == 1)   
        account = 100
        account -= testInst.buy(99)
        assert(testInst.quantity == 99)
        account += testInst.update([])
        account += testInst.update([])
        account += testInst.update([])
        assert(testInst.gethistory() == [1,1.05,1.1025])
        try:
            testInst.sell(100)
        except(InsufficientQuantityError):
            pass
        else:
            raise AssertionError('Failed to raise error on illegal transaction')
        account += testInst.sell(90)
        assert(testInst.quantity == 9)
        acount += testInst.update()
        acount += testInst.update()
        acount += testInst.update()
        acount += testInst.update()
        acount += testInst.update()
        account -= testInst.buy(5)
        acount += testInst.update()
        acount += testInst.update()
        acount += testInst.update()
        acount += testInst.update()
        acount += testInst.update()
        acount += testInst.update()
        n = testInst.getIncrease()
        account += testInst.sell(14)
        assert(n == (account - 100))

            


Testing.investmentTest()