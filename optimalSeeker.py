from random import randint, shuffle
from playFibonacciThreeDozens import ThreeDozenStrategy
from playFibonacciSixDozens import SixDozenStrategy

import seaborn as sns
import matplotlib.pyplot as plt

import itertools

# plotWinrate = []

moneyOptions = list(range(10000, 100001, 1000))
betOptions = [1, 5, 10, 20, 50, 100, 500, 1000, 2000, 5000]
lossLimits = [x * 0.05 for x in range(2, 20)]
# winLimits = [1 + (x * 0.05) for x in range(2, 11)]
winLimits = [1.25]

# https://www.codegrepper.com/code-examples/python/python+generate+all+combinations+from+multiple+lists
# a = [[1,2,3],[4,5,6],[7,8,9,10]]

a = [moneyOptions, betOptions, lossLimits, winLimits]
testTuples = list(itertools.product(*a))
shuffle(testTuples)

counter = 0
testsLen = len(testTuples)
bestWinrate = 0
bestTuple = ()
for aTuple in testTuples:
    counter += 1
    print("progress = %d of %d" % (counter, testsLen))

    winrate = 0
    wins = 0
    tests = 10000
    for i in range(1, tests):
        print("     progress = %d of %d" % (i, tests))
        strat = ThreeDozenStrategy(aTuple[0], aTuple[1], (aTuple[2], aTuple[3]))
        strat.play()

        if strat.isWin():
            wins = wins + 1
        
        winrate = (wins/tests)*100
    #eof tests
    
    if winrate > bestWinrate:
        bestWinrate = winrate
        bestTuple = aTuple
        print("%.2fpct winrate in %d rolls for %s" % (winrate, len(strat.moneyChart), str(bestTuple)))
        print("===")
#eof testTuples    


# plt.plot(plotWinrate, linewidth=2)

# plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
# plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
# plt.xticks(fontsize=16, fontweight="bold")
# plt.yticks(fontsize=16, fontweight="bold")
# plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")
# plt.show()