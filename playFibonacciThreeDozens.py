from abstractStrategy import AbstractStrategy, fibonacci
from random import random, randint
from roulette import Roulette

class ThreeDozenStrategy(AbstractStrategy):
    
    def setupBetPots(self):
        # print("call in ThreeDozenStrategy")

        self.firstDozenCounter  = 1
        self.secondDozenCounter = 1
        self.thirdDozenCounter  = 1
    #eof setupBetPots

    def placeBets(self):
        self.firstDozenBet  = self.pay(fibonacci(self.firstDozenCounter) * self.bet)
        self.secondDozenBet = self.pay(fibonacci(self.secondDozenCounter) * self.bet)
        self.thirdDozenBet  = self.pay(fibonacci(self.thirdDozenCounter) * self.bet)
    # eof placeBets  
    
    def updateAndCollect(self, roll):
        '''collect bets, track strategy and place new bets'''
        dozen = Roulette.getDozen(roll)

        firstMultiplier = 0
        firstUpdate = 1
        secondMultiplier = 0
        secondUpdate = 1
        thirdMultiplier = 0
        thirdUpdate = 1
        
        if dozen == 0:
            pass
        elif dozen == 1:
            firstMultiplier = 3
            firstUpdate = -2
        elif dozen == 2:
            secondMultiplier = 3
            secondUpdate = -2
        elif dozen == 3:
            thirdMultiplier = 3
            thirdUpdate = -2
        else:
            raise Exception("unexpected dozen returned = " + str(dozen))
        
        self.collect(self.firstDozenBet, firstMultiplier)
        self.firstDozenCounter = max(self.firstDozenCounter+firstUpdate, 1)

        self.collect(self.secondDozenBet, secondMultiplier)
        self.secondDozenCounter = max(self.secondDozenCounter+secondUpdate, 1)

        self.collect(self.thirdDozenBet, thirdMultiplier)
        self.thirdDozenCounter = max(self.thirdDozenCounter+thirdUpdate, 1)
    # eof updateBetPots  

if __name__ == "__main__":
    strat = ThreeDozenStrategy(1000, 10, (0.66, 1.5))
    strat.play()
    strat.getPlot()

    print("The result is a win: %s" % (strat.isWin()))
    
#eof class tests