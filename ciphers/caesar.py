class CaesarCipher(object):
    def __init__(self, k, text):
        self.k = k
        self.text = text.upper()
    def _encrypt(self):
        cipher_text = ""
        for char in self.text:
            c = (ord(char)-65 + self.k )%26
            cipher_text = cipher_text+chr(c+65)
        return cipher_text
    def _decrypt(self):
        plain_text = ""
        for char in self.text:
            p = (ord(char) - 65 - self.k)%26
            plain_text = plain_text + chr(p+65)
        return plain_text
def main():
    enc = CaesarCipher(18,"saphi")
    print enc._encrypt()
    dec = CaesarCipher(18,enc._encrypt())
    print dec._decrypt()
if __name__ == '__main__':
    main()
