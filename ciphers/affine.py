import inverse

class AffineCipher(object):
    def __init__(self, a, b, text):
        self.a = a
        self.b = b
        self.text = text.upper()

    def _encrypt(self):
        cipher_text = ""
        for char in self.text:
            c = ((ord(char) - 65)*self.a + self.b) % 26
            cipher_text = cipher_text + chr(c + 65)
        return cipher_text
    def _decrypt(self):
        inverseResult = inverse.InverseCalculate(moduloNumber=26,
                                                 inverseNumber=self.a)._inverse()
        if inverseResult:
            if inverseResult < 0:
                inverseResult = inverseResult + 26
                plain_text = ""
                for char in self.text:
                    p = ((ord(char) - 65 - self.b)*inverseResult)%26
                    plain_text = plain_text + chr(p + 65)
                return plain_text
        else:
            return False
def main():
    aff = AffineCipher(7,3,"itisaniceday")
    print aff._encrypt()
    affd = AffineCipher(7,3,aff._encrypt())
    print affd._decrypt()

if __name__ == '__main__':
    main()
