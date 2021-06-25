from random import random, randint
from roulette import Roulette
import seaborn as sns
import matplotlib.pyplot as plt

# https://lightning-roulette.com/

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


class ThreeDozenStrategy:
    def __init__(self, budget, bet, exitRules):
        self.startBudget = budget
        self.money = budget
        self.bet = bet
        self.lossCondition = exitRules[0]
        self.winCondition = exitRules[1]
        self.moneyChart = [self.startBudget]
        self.setupBetPots()
    #eof init

    def isWin(self):
        if self.money >= self.startBudget * self.winCondition:
            return True
        elif self.money <= self.startBudget * self.lossCondition:
            return False
        else:
            return None
    #eof isWin

    def getPlot(self):
        
        plt.plot(self.moneyChart, linewidth=2)
        plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
        plt.ylabel("Money", fontsize=18, fontweight="bold")
        plt.xticks(fontsize=16, fontweight="bold")
        plt.yticks(fontsize=16, fontweight="bold")
        plt.title("Money Over Time", fontsize=22, fontweight="bold")
        plt.show()
    #eof getPlot

    def setupBetPots(self):
        # print("call in parent")
        self.firstDozenBet = fibonacci(1) * self.bet
        self.secondDozenBet = fibonacci(1) * self.bet
        self.thirdDozenBet = fibonacci(1) * self.bet
    #eof setupBetPots

    def updateMoney(self, roll):
        self.money = randint(self.startBudget/2, self.startBudget*2)
        self.moneyChart.append(self.money)
    # eof updateMoney
      
    def updateBetPots(self, roll):
        pass
    # eof updateBetPots  

    def play(self):
        '''play until one of the two conditions is met'''

        lowMoney = self.startBudget * self.lossCondition
        bigMoney = self.startBudget * self.winCondition
        roulette = Roulette()

        while lowMoney <= self.money <= bigMoney:
            roll = roulette.roll()
            self.updateMoney(roll)
            self.updateBetPots(roll)
        #while money
        return None
    #eof play


if __name__ == "__main__":
    strat = ThreeDozenStrategy(1000, 10, (0.66, 1.5))
    strat.play()
    strat.getPlot()

    print("" % ())
    strat.isWin()
#eof class tests