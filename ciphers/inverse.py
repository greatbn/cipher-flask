#!/usr/bin/python
import gcd
class InverseCalculate(object):
    def __init__(self, moduloNumber, inverseNumber):
        self.moduloNumber = moduloNumber
        self.inverseNumber = inverseNumber
    def _inverse(self):
        if(gcd.GcdCalculate(numberOne=self.moduloNumber,
                            numberTwo=self.inverseNumber)._check_coprime()):
            a = 1
            b = 0
            d = 0
            e = 1
            if(self.inverseNumber > self.moduloNumber):
                self.inverseNumber = self.inverseNumber % self.moduloNumber
            c = self.moduloNumber
            f = self.inverseNumber
            try:
                while(True):
                    tempd = d
                    tempe = e
                    tempf = f
                    z = c/f
                    f = c%f
                    d = a - d*z
                    e = b - e*z
                    a = tempd
                    b = tempe
                    c = tempf
                    if f == 1:
                        return e
            except:
                return False
            return False
        else:
            return False

def main():
    inv = InverseCalculate(moduloNumber=26,inverseNumber=7)
    print inv._inverse()

if __name__ == '__main__':
    main()
