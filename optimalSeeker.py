from random import randint, shuffle
from playFibonacciThreeDozens import ThreeDozenStrategy
from playFibonacciSixDozens import SixDozenStrategy

import seaborn as sns
import matplotlib.pyplot as plt

import itertools

# plotWinrate = []

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
"""
1.25 gains 

aleks@aleks-Aspire-E5-572-2020:~/Development/Python/rouletteStrategies$ grep "pct winrate" results.txt 
39.69pct winrate in 28 rolls for (58000, 10, 0.8500000000000001, 1.25)
40.18pct winrate in 63 rolls for (58000, 1, 0.8500000000000001, 1.25)
55.78pct winrate in 10 rolls for (33000, 1000, 0.6000000000000001, 1.25)
67.34pct winrate in 24 rolls for (45000, 100, 0.35000000000000003, 1.25)
69.01pct winrate in 62 rolls for (51000, 5, 0.4, 1.25)
70.89pct winrate in 49 rolls for (40000, 5, 0.2, 1.25)
71.05pct winrate in 19 rolls for (20000, 20, 0.2, 1.25)
71.06pct winrate in 33 rolls for (44000, 50, 0.15000000000000002, 1.25)
71.51pct winrate in 55 rolls for (70000, 20, 0.15000000000000002, 1.25)
72.63pct winrate in 46 rolls for (30000, 1, 0.1, 1.25)
73.07pct winrate in 50 rolls for (97000, 10, 0.1, 1.25)

1.3

55.70pct winrate in 28 rolls for (54000, 50, 0.6000000000000001, 1.3)
64.09pct winrate in 33 rolls for (45000, 50, 0.4, 1.3)
66.00pct winrate in 24 rolls for (44000, 500, 0.1, 1.3)
66.72pct winrate in 11 rolls for (78000, 1000, 0.1, 1.3)
68.91pct winrate in 64 rolls for (19000, 1, 0.15000000000000002, 1.3)
69.05pct winrate in 38 rolls for (24000, 1, 0.15000000000000002, 1.3)

bruteforce all no shuffle
)
0.02pct winrate in 138 rolls for (50000, 1, 1.0, 1.65)
0.04pct winrate in 114 rolls for (50000, 1, 1.0, 1.3)
10.13pct winrate in 108 rolls for (50000, 1, 0.9500000000000001, 1.65)
10.54pct winrate in 106 rolls for (50000, 1, 0.9500000000000001, 1.6)
11.18pct winrate in 106 rolls for (50000, 1, 0.9500000000000001, 1.55)
12.25pct winrate in 102 rolls for (50000, 1, 0.9500000000000001, 1.5)
13.64pct winrate in 98 rolls for (50000, 1, 0.9500000000000001, 1.45)
14.53pct winrate in 95 rolls for (50000, 1, 0.9500000000000001, 1.4)
15.63pct winrate in 92 rolls for (50000, 1, 0.9500000000000001, 1.35)
18.11pct winrate in 89 rolls for (50000, 1, 0.9500000000000001, 1.3)
20.13pct winrate in 84 rolls for (50000, 1, 0.9500000000000001, 1.25)
24.53pct winrate in 79 rolls for (50000, 1, 0.9500000000000001, 1.2)
27.91pct winrate in 72 rolls for (50000, 1, 0.9500000000000001, 1.15)
28.20pct winrate in 82 rolls for (50000, 1, 0.9, 1.3)
31.80pct winrate in 78 rolls for (50000, 1, 0.9, 1.25)
35.82pct winrate in 74 rolls for (50000, 1, 0.9, 1.2)
42.43pct winrate in 68 rolls for (50000, 1, 0.9, 1.15)
44.57pct winrate in 71 rolls for (50000, 1, 0.8500000000000001, 1.2)
50.65pct winrate in 65 rolls for (50000, 1, 0.8500000000000001, 1.15)
51.64pct winrate in 69 rolls for (50000, 1, 0.8, 1.2)
56.86pct winrate in 64 rolls for (50000, 1, 0.8, 1.15)
63.01pct winrate in 63 rolls for (50000, 1, 0.75, 1.15)
65.87pct winrate in 63 rolls for (50000, 1, 0.7000000000000001, 1.15)
69.48pct winrate in 63 rolls for (50000, 1, 0.65, 1.15)
70.17pct winrate in 62 rolls for (50000, 1, 0.6000000000000001, 1.15)
72.70pct winrate in 62 rolls for (50000, 1, 0.55, 1.15)
73.21pct winrate in 44 rolls for (50000, 5, 0.55, 1.15)
73.34pct winrate in 19 rolls for (50000, 100, 0.55, 1.15)
73.77pct winrate in 38 rolls for (52000, 10, 0.55, 1.15)
73.95pct winrate in 38 rolls for (53000, 10, 0.55, 1.15)
74.19pct winrate in 38 rolls for (57000, 10, 0.55, 1.15)
74.34pct winrate in 64 rolls for (59000, 1, 0.55, 1.15)
74.42pct winrate in 65 rolls for (64000, 1, 0.55, 1.15)
74.56pct winrate in 65 rolls for (65000, 1, 0.55, 1.15)
74.57pct winrate in 48 rolls for (74000, 5, 0.55, 1.15)
74.88pct winrate in 43 rolls for (93000, 10, 0.55, 1.15)
"""