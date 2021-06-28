from simulateWithBudget import reinvestAllStrategy
from playTwoDozens import TwoDozenStrategy
from random import randint, shuffle
from playFibonacciThreeDozens import ThreeDozenStrategy
from playFibonacciSixDozens import SixDozenStrategy

import seaborn as sns
import matplotlib.pyplot as plt

import itertools

"""
$ grep "pct winrate" results.txt 
$grep "pct roi" roiSeek.txt
"""

def findTopWinratePercentage():

    moneyOptions = list(range(50000, 100001, 1000))
    betOptions = [1, 5, 10, 20, 50, 100, 500, 1000, 2000, 5000]
    lossLimits = [x * 0.05 for x in range(20, 10, -1)]
    winLimits = [1 + (x * 0.05) for x in range(13, 2, -1)]
    # winLimits = [1.30]

    # https://www.codegrepper.com/code-examples/python/python+generate+all+combinations+from+multiple+lists
    # a = [[1,2,3],[4,5,6],[7,8,9,10]]

    a = [moneyOptions, betOptions, lossLimits, winLimits]
    testTuples = list(itertools.product(*a))
    # shuffle(testTuples)

    counter = 0
    testsLen = len(testTuples)
    bestWinrate = 0
    bestTuple = ()
    for aTuple in testTuples:
        counter += 1
        print("progress = %d of %d" % (counter, testsLen))

        winrate = 0
        wins = 0
        avgLen = 0
        tests = 10000
        for i in range(1, tests):
            # print("     progress = %d of %d" % (i, tests))
            strat = ThreeDozenStrategy(aTuple[0], aTuple[1], (aTuple[2], aTuple[3]))
            strat.play()

            if strat.isWin():
                wins = wins + 1
                avgLen += len(strat.moneyChart)
            
        #eof tests
        winrate = (wins/tests)*100
        
        if winrate > bestWinrate:
            avgLen = avgLen/wins 
            bestWinrate = winrate
            bestTuple = aTuple
            print("%.2fpct winrate in %d rolls agv for params %s" % (winrate, avgLen, str(bestTuple)))
            print("===")
    #eof testTuples    


    # plt.plot(plotWinrate, linewidth=2)

    # plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
    # plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
    # plt.xticks(fontsize=16, fontweight="bold")
    # plt.yticks(fontsize=16, fontweight="bold")
    # plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")
    # plt.show()

    # results

#eof findTopWinratePercentage

def findTopMoneyGains():
    '''compare ROI = money in vs money out
    roi = total money out / total money in'''

    moneyOptions = list(range(50000, 100001, 1000))
    betOptions = [1, 5, 10, 20, 50, 100, 500, 1000, 2000, 5000]
    lossLimits = [x * 0.05 for x in range(20, 10, -1)]
    winLimits = [1 + (x * 0.05) for x in range(13, 2, -1)]

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
    for aTuple in testTuples:
        counter += 1
        print("progress = %d of %d" % (counter, testsLen))

        avgLen = 0
        tests = 10000
        for i in range(1, tests):
            # print("     progress = %d of %d" % (i, tests))
            strat = ThreeDozenStrategy(aTuple[0], aTuple[1], (aTuple[2], aTuple[3]))
            strat.play()

            totalMoneyIn += strat.startBudget
            totalMoneyOut += strat.getMoney()

            avgLen += len(strat.moneyChart)
        #eof tests
        roi = (totalMoneyOut/totalMoneyIn)*100
        
        if roi > bestROI:
            avgLen = avgLen/tests
            bestROI = roi
            bestTuple = aTuple
            print("%.2fpct roi (%d) in %d rolls agv for params %s" % (roi, (totalMoneyOut-totalMoneyIn)/tests, avgLen, str(bestTuple)))
    #eof testTuples    


    # # plt.plot(plotWinrate, linewidth=2)

    # # plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
    # # plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
    # # plt.xticks(fontsize=16, fontweight="bold")
    # # plt.yticks(fontsize=16, fontweight="bold")
    # # plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")
    # # plt.show()

# eof findTopMoneyGains


def optimizeReinvestAllStrategy():
    '''compare ROI = money in vs money out
    roi = total money out / total money in'''

    # as per the youtube video
    moneyOptions = [50000]
    betOptions = [100]
    lossLimits = [0.55]
    winLimits = [1.15]

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
    moneyChart = []
    for aTuple in testTuples:
        counter += 1
        print("progress = %d of %d" % (counter, testsLen))

        avgLen = 0
        tests = 1000
        gainGoal = 2
        for i in range(1, tests+1):
            print("     progress = %d of %d" % (i, tests))
            # strat = TwoDozenStrategy(aTuple[0], aTuple[1], (aTuple[2], aTuple[3]))
            strat = ThreeDozenStrategy(aTuple[0], aTuple[1], (aTuple[2], aTuple[3]))

            totalMoneyIn += strat.startBudget
            result, chart = reinvestAllStrategy(strat, gainGoal * strat.startBudget)
            totalMoneyOut += result

            avgLen += len(chart)
            moneyChart += chart
        #eof tests
        roi = (totalMoneyOut/totalMoneyIn)*100
        
        if roi > bestROI:
            avgLen = avgLen/tests
            bestROI = roi
            bestTuple = aTuple
            print("%.2fpct roi (%d) in %d rolls agv for params %s" % (roi, (totalMoneyOut-totalMoneyIn)/tests, avgLen, str(bestTuple)))
    #eof testTuples    
    print("Best is %.2fpct roi (%d) in %d rolls agv for params %s" % (roi, (totalMoneyOut-totalMoneyIn)/tests, avgLen, str(bestTuple)))


    plt.plot(moneyChart, linewidth=2)

    plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
    plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
    plt.xticks(fontsize=16, fontweight="bold")
    plt.yticks(fontsize=16, fontweight="bold")
    plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")
    plt.show()

# eof optimizeReinvestAllStrategy
if __name__ == "__main__":
    optimizeReinvestAllStrategy()