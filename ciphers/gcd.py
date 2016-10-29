#!/usr/bin/python
class GcdCalculate(object):
    def __init__(self, numberOne, numberTwo):
        self.numberOne = numberOne
        self.numberTwo = numberTwo
    def _gcd(self):
        if self.numberOne == self.numberTwo:
            return self.numberOne
        elif self.numberOne > self.numberTwo:
            self.numberOne = self.numberOne - self.numberTwo
            return self._gcd()
        elif self.numberOne < self.numberTwo:
            self.numberTwo = self.numberTwo - self.numberOne
            return self._gcd()
    def _check_coprime(self):
        if (self._gcd() == 1):
            return True
        else:
            return False
def main():
    gcdx = GcdCalculate(11,3)
    print gcdx._gcd()
    print gcdx._check_coprime()

if __name__ == '__main__':
    main()
