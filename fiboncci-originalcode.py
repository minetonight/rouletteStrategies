
import random
import seaborn as sns
import matplotlib.pyplot as plt


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
def fibonacci_strategy(bankroll):
    fibonacci_number = 1
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll > 0:
        bet = fibonacci(fibonacci_number) * .01
        if bet > bankroll:
            bet = bankroll
        roll = random.choice(pockets)
        if roll == "Red":
            bankroll += bet
            fibonacci_number = max(fibonacci_number - 2, 1)
        else:
            bankroll -= bet
            fibonacci_number += 1
        bankroll_history.append(bankroll)
    return bankroll_history

for i in range(4):
    plt.plot(fibonacci_strategy(bankroll=100), linewidth=2)
    
plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
plt.xticks(fontsize=16, fontweight="bold")
plt.yticks(fontsize=16, fontweight="bold")
plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")
plt.show()