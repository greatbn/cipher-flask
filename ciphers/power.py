class PowerCalculate(object):
    def __init__(self, number, powerNumber, moduloNumber):
        self.number = number
        self.powerNumber = powerNumber
        self.moduloNumber = moduloNumber
    def _calculate(self):
        return (self.number**self.powerNumber)%self.moduloNumber
