from random import random, randint
from roulette import Roulette
import seaborn as sns
import matplotlib.pyplot as plt
import abc 

def fibonacci(n):
    '''https://stackoverflow.com/a/32215743 '''
    computed = {0: 0, 1: 1}
    def fib_inner(n):
        if n not in computed:
            computed[n] = fib_inner(n-1) + fib_inner(n-2)
        return computed[n]
    return fib_inner(n)

class AbstractStrategy:
    def __init__(self, budget, bet, exitRules):
        self.startBudget = budget
        self.__money= budget
        self.bet = bet
        self.lossCondition = exitRules[0]
        self.winCondition = exitRules[1]
        self.moneyChart = [self.startBudget]
        self.setupBetPots()
    #eof init

    def isWin(self):
        if self.__money>= self.startBudget * self.winCondition:
            return True
        elif self.__money<= self.startBudget * self.lossCondition:
            return False
        else:
            return None # TODO fixme
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

    @abc.abstractmethod
    def setupBetPots(self):
        '''define your bets pots here in your subclass implementation'''
        pass
    #eof setupBetPots

    @abc.abstractmethod
    def placeBets(self):
        self.__money = randint(self.startBudget/2, self.startBudget*2)
    # eof placeBets
    

    @abc.abstractmethod
    def updateAndCollect(self, roll):
        pass
    # eof updateAndCollect  

    def play(self):
        '''play until one of the two conditions is met'''

        lowMoney = self.startBudget * self.lossCondition
        bigMoney = self.startBudget * self.winCondition
        roulette = Roulette()

        while lowMoney <= self.__money <= bigMoney: # and len(self.moneyChart) < 1000:
            self.placeBets()
            roll = roulette.roll()
            self.updateAndCollect(roll)

            self.moneyChart.append(self.__money)
        #while money
        return None
    #eof play

    def pay(self, amount):
        if self.__money >= amount:
            self.__money = self.__money - amount
        else:
            amount = 0
        
        return amount
    # eof pay

    def collect(self, bet, multiplier):
        self.__money += bet * multiplier
        return None
    # eof collect

    def getMoney(self):
        return self.__money
    # eof getMoney

if __name__ == "__main__":
    strat = AbstractStrategy(1000, 10, (0.66, 1.5))
    strat.play()
    strat.getPlot()

    print("" % ())
    strat.isWin()
#eof class tests