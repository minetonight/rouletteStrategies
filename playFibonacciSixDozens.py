from abstractStrategy import fibonacci
from random import random, randint
from roulette import Roulette
from playFibonacciThreeDozens import ThreeDozenStrategy

class SixDozenStrategy(ThreeDozenStrategy):

    def setupBetPots(self):
        # print("call in inherited")
        super().setupBetPots()
        # print(self.firstDozenCounter) # confirmation that inheritance work

        self.topRowCounter = 1
        self.midRowCounter = 1
        self.lowRowCounter = 1
    #eof setupBetPots
    
    def placeBets(self):
        super().placeBets()

        self.topRowBet      = self.pay(fibonacci(self.topRowCounter) * self.bet)
        self.midRowBet      = self.pay(fibonacci(self.midRowCounter) * self.bet)
        self.lowRowBet      = self.pay(fibonacci(self.lowRowCounter) * self.bet)
    # eof placeBets

    def updateAndCollect(self, roll):
        super().updateAndCollect(roll)
        
        row = Roulette.getRow(roll)

        topMultiplier = 0
        topUpdate = 1
        midMultiplier = 0
        midUpdate = 1
        lowMultiplier = 0
        lowUpdate = 1
        
        if row == None:
            pass
        elif row == 'top':
            topMultiplier = 3
            topUpdate = -2
        elif row == 'mid':
            midMultiplier = 3
            midUpdate = -2
        elif row == 'low':
            lowMultiplier = 3
            lowUpdate = -2
        else:
            raise Exception("unexpected row returned = " + str(row))
        
        self.collect(self.topRowBet, topMultiplier)
        self.topRowCounter = max(self.topRowCounter+topUpdate, 1)

        self.collect(self.midRowBet, midMultiplier)
        self.midRowCounter = max(self.midRowCounter+midUpdate, 1)

        self.collect(self.lowRowBet, lowMultiplier)
        self.lowRowCounter = max(self.lowRowCounter+lowUpdate, 1)
    # eof updateAndCollect

if __name__ == "__main__":
    strat = SixDozenStrategy(1000, 10, (0.66, 1.5))
    strat.play()
    strat.getPlot()
    
    print("The result is a win: %s" % (strat.isWin()))
#eof class tests