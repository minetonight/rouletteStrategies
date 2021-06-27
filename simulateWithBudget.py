from playFibonacciThreeDozens import ThreeDozenStrategy
from playFibonacciSixDozens import SixDozenStrategy

import matplotlib.pyplot as plt

def reinvestAllStrategy():
    strat = ThreeDozenStrategy(50000, 100, (0.55, 1.15))
    initialMoney = strat.getMoney()
    finalMoney = initialMoney
    chartHistory = []

    while finalMoney > 0:
        strat.play()
        finalMoney = strat.getMoney()
        chartHistory += strat.moneyChart
        print("     The result is a win: %s" % (strat.isWin()))
        strat = ThreeDozenStrategy(finalMoney, strat.bet, (strat.lossCondition, strat.winCondition))
        print("Now we have %dc" % (finalMoney))

    strat.moneyChart = chartHistory
    strat.getPlot()
# eof reinvestAllStrategy

def keepTheGainsStrategy():
    '''overall result - 3 out of many many attempts '''
    strat = ThreeDozenStrategy(50000, 1, (0.75, 1.15))
    initialMoney = strat.getMoney()
    finalMoney = initialMoney
    chartHistory = []
    gains = 0
    gainsHistory = []

    while finalMoney > 0:
        strat.play()
        finalMoney = strat.getMoney()

        print("     The result is a win: %s" % (strat.isWin()))
        if strat.isWin() == True:
            print("gains temp = %d" % (finalMoney - initialMoney))   
            gains += (finalMoney - initialMoney)
            print("gains total = %d" % (gains))   
            finalMoney = initialMoney
        else: 
            initialMoney = finalMoney

        gainsHistory.append(gains)
        chartHistory += strat.moneyChart
        strat = ThreeDozenStrategy(finalMoney, strat.bet, (strat.lossCondition, strat.winCondition))
        print("Now we have %dc" % (finalMoney))

    strat.moneyChart = chartHistory
    strat.getPlot()
    strat.moneyChart = gainsHistory
    strat.getPlot()

# eof keepTheGainsStrategy

# keepTheGainsStrategy()
reinvestAllStrategy()