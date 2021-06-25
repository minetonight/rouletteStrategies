from roulette import Roulette
from playFibonacciThreeDozens import ThreeDozenStrategy, fibonacci

class SixDozenStrategy(ThreeDozenStrategy):
    
    def setupBetPots(self):

        print("call in inherited")
        self.firstDozenBet = fibonacci(1) * self.bet
        self.secondDozenBet = fibonacci(1) * self.bet
        self.thirdDozenBet = fibonacci(1) * self.bet
    #eof setupBetPots


if __name__ == "__main__":
    strat = SixDozenStrategy(1000, 10, (0.66, 1.5))
    strat.play()
    strat.isWin()
    strat.getPlot()

    print("" % ())
#eof class tests