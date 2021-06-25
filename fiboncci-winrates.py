#from https://mindingthedata.medium.com/simulating-roulette-betting-strategies-with-python-61bf40fc4a1c 

import random
import seaborn as sns
import matplotlib.pyplot as plt

random.seed = 121

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_strategy(initialBankroll, betStep):
    bankroll = initialBankroll
    fibonacci_number = 1
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll > 0 and bankroll < initialBankroll*1.33:
        bet = fibonacci(fibonacci_number) * betStep
        if bet > bankroll:
            bet = bankroll
        roll = random.choice(pockets)
        if roll == "Red":
            bankroll += bet
            # fibonacci_number = max(fibonacci_number - 2, 1)
            fibonacci_number = 1
        else:
            bankroll -= bet
            fibonacci_number += 1
        bankroll_history.append(bankroll)

    topwin = max(bankroll_history)
    gameindex = bankroll_history.index(topwin)+1
    roi = (topwin-initialBankroll)/gameindex

    # print("%d$ in %d games => roi = %.2f $/game" % (topwin, gameindex, roi))
    return (bankroll_history, bankroll >=150)

initialBankroll = 1000
# betStep = 5
tests = 10000
plotWinrate = [] 
start = 1
# end = int(initialBankroll/1.9)
end = initialBankroll
for betStep in range (start, end):
    wins = 0
    for i in range(tests):
        datapoints, isWin = fibonacci_strategy(initialBankroll, betStep)
        if isWin:
            wins = wins + 1
    
    winrate = (wins/tests)*100
    plotWinrate.append(winrate)
    print("With step %d strategy winrate is %.2fpct" % (betStep, winrate))
#eof betSteps

plt.plot(plotWinrate, linewidth=2)

topwin = max(plotWinrate)
betValue = plotWinrate.index(topwin)+1

print("%.2f pct with %d $ bets" % (topwin, betValue+start))
    


plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
plt.xticks(fontsize=16, fontweight="bold")
plt.yticks(fontsize=16, fontweight="bold")
plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")
plt.show()

# 71.53 pct with 334 $ bets for 1.33 gains
# 62.5 pct with 500$ bets for 1.5 gains
