import random

# european Roulette https://lightning-roulette.com/

class Roulette: 
    def __init__(self):
        self.roulette = list(range(1, 37))
        self.roulette.append(0)
        # print(self.roulette)
        # print(len(self.roulette))

    def roll(self):
        '''get next roll result'''
        roll = random.choice(self.roulette)
        print(roll)
        return roll
    #eof roll

    @staticmethod
    def getDozen(number):
        ''' return 1st, 2nd or 3rd dozen, or None '''
        if 0 < number < 37:
            return 1 + int(number/12.1)
        else:
            return None
    #eof getDozen

    @staticmethod
    def getRow(number):
        '''return "top", "mid", "low" or None'''
        rows = {1:"low", 2:"mid", 0:"top"}
        if 0 < number < 37:
            return rows[number % 3]
        else:
            return None
    #eof getRow

    def doTests(self):
        for n in self.roulette:
            d = Roulette.getDozen(n)
            print("%d is in %d dozen" % (n, d))
            r = Roulette.getRow(n)
            print("%d is in %s row" % (n, r))
    #eof doTests

if __name__ == "__main__":
    roulette = Roulette()

    # roulette.doTests()
    roll = roulette.roll()
    print(roll)
    print("%d is in dozen %d and %s row." % (roll, roulette.getDozen(roll), roulette.getRow(roll)))
#eof class tests