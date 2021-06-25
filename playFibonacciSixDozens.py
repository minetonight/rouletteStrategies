from abstractStrategy import fibonacci
from random import random, randint
from roulette import Roulette
from playFibonacciThreeDozens import ThreeDozenStrategy

class SixDozenStrategy(ThreeDozenStrategy):
    
    def setupBetPots(self):
        # print("call in inherited")
        super.setupBetPots()
        print(self.firstDozenCounter)

        self.topRowBet      = fibonacci(1) * self.bet
        self.midRowBet      = fibonacci(1) * self.bet
        self.lowRowBet      = fibonacci(1) * self.bet
    #eof setupBetPots

    def updateMoney(self, roll):
        self.money = randint(self.startBudget/2, self.startBudget*2)
        self.moneyChart.append(self.money)
    # eof updateMoney


if __name__ == "__main__":
    strat = SixDozenStrategy(1000, 10, (0.66, 1.5))
    strat.play()
    strat.isWin()
    strat.getPlot()

    print("" % ())
#eof class tests