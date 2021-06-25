from playFibonacciThreeDozens import ThreeDozenStrategy
from playFibonacciSixDozens import SixDozenStrategy

import seaborn as sns
import matplotlib.pyplot as plt

import itertools

winrate = 0
wins = 0
tests = 10000
plotWinrate = []
for i in range(1, tests):
    print("progress = %d of %d" % (i, tests))
    # strat = SixDozenStrategy(1000, 10, (0.66, 1.5))
    strat = ThreeDozenStrategy(1000, 10, (0.3, 1.5))
    strat.play()

    if strat.isWin():
        wins = wins + 1
    
    winrate = (wins/tests)*100
    plotWinrate.append(winrate)
#eof tests

print("Strategy winrate is %.2fpct" % (winrate))
plt.plot(plotWinrate, linewidth=2)

plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
plt.xticks(fontsize=16, fontweight="bold")
plt.yticks(fontsize=16, fontweight="bold")
plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")
plt.show()