import itertools
from random import shuffle

from matplotlib import pyplot as plt
from abstractStrategy import AbstractStrategy
from roulette import Roulette

class TwoDozenStrategy(AbstractStrategy):
    
    def setupBetPots(self):
        pass
    #eof setupBetPots

    def placeBets(self):
        self.firstDozenBet  = self.pay(self.bet)
        self.thirdDozenBet  = self.pay(self.bet)
    # eof placeBets  
    
    def updateAndCollect(self, roll):
        '''collect bets, track strategy and place new bets'''
        dozen = Roulette.getDozen(roll)

        firstMultiplier = 0
        thirdMultiplier = 0
        
        if dozen == 0:
            pass
        elif dozen == 1:
            firstMultiplier = 3
        elif dozen == 2:
            pass
        elif dozen == 3:
            thirdMultiplier = 3
        else:
            raise Exception("unexpected dozen returned = " + str(dozen))
        
        self.collect(self.firstDozenBet, firstMultiplier)
        self.collect(self.thirdDozenBet, thirdMultiplier)
    # eof updateBetPots  



def testThousandGames():
    '''compare ROI = money in vs money out
    roi = total money out / total money in'''

    # as per the youtube video
    moneyOptions = [400]
    betOptions = [50]
    lossLimits = [0.05]
    winLimits = [1.5]

    # https://www.codegrepper.com/code-examples/python/python+generate+all+combinations+from+multiple+lists
    # a = [[1,2,3],[4,5,6],[7,8,9,10]]

    a = [moneyOptions, betOptions, lossLimits, winLimits]
    testTuples = list(itertools.product(*a))
    shuffle(testTuples)

    counter = 0
    testsLen = len(testTuples)
    bestROI = 0
    totalMoneyIn = 0
    totalMoneyOut = 0
    bestTuple = ()
    plotWinrate = []
    for aTuple in testTuples:
        counter += 1
        print("progress = %d of %d" % (counter, testsLen))

        avgLen = 0
        tests = 10000
        for i in range(1, tests):
            # print("     progress = %d of %d" % (i, tests))
            strat = TwoDozenStrategy(aTuple[0], aTuple[1], (aTuple[2], aTuple[3]))
            strat.play()

            totalMoneyIn += strat.startBudget
            totalMoneyOut += strat.getMoney()

            avgLen += len(strat.moneyChart)
            plotWinrate += strat.moneyChart
        #eof tests
        roi = (totalMoneyOut/totalMoneyIn)*100
        
        if roi > bestROI:
            avgLen = avgLen/tests
            bestROI = roi
            bestTuple = aTuple
            print("%.2fpct roi (%d) in %d rolls agv for params %s" % (roi, (totalMoneyOut-totalMoneyIn)/tests, avgLen, str(bestTuple)))
    #eof testTuples    


    plt.plot(plotWinrate, linewidth=2)

    plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
    plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
    plt.xticks(fontsize=16, fontweight="bold")
    plt.yticks(fontsize=16, fontweight="bold")
    plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")
    plt.show()

# eof testThousandGames

if __name__ == "__main__":
    strat = TwoDozenStrategy(400, 50, (0.05, 1.5))
    strat.play()
    # strat.getPlot()

    print("The result is a win: %s" % (strat.isWin()))
    
    testThousandGames()
#eof class tests