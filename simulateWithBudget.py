from playTwoDozens import TwoDozenStrategy
from abstractStrategy import AbstractStrategy
from playFibonacciThreeDozens import ThreeDozenStrategy
from playFibonacciSixDozens import SixDozenStrategy

import matplotlib.pyplot as plt

def reinvestAllStrategy(strat:AbstractStrategy, upperBound, showPlot = False):
    initialMoney = strat.getMoney()
    finalMoney = initialMoney
    chartHistory = []

    while 0 < finalMoney < upperBound:
        strat.play()
        finalMoney = strat.getMoney()
        chartHistory += strat.moneyChart
        
        if showPlot:
            print("     The result is a win: %s" % (strat.isWin()))
        stratClass = type(strat)
        strat = stratClass(finalMoney, strat.bet, (strat.lossCondition, strat.winCondition))
        
        if showPlot:
            print("Now we have %dc" % (finalMoney))

    strat.moneyChart = chartHistory
    if showPlot:
        strat.getPlot()

    return finalMoney, chartHistory 
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


if __name__ == "__main__":
    # keepTheGainsStrategy()
    strat = ThreeDozenStrategy(50000, 100, (0.55, 1.15))
    # strat = TwoDozenStrategy(400, 100, (0.05, 1.5))
    money, chart = reinvestAllStrategy(strat, strat.startBudget * 3, showPlot = True)
    # strat.moneyChart = chart
    # strat.getPlot()