import operator
class VigenereCipher(object):
    def __init__(self, key, text):
        self.key = key.upper()
        self.text = text.upper()
    def _split(self):
        list_string = []
        while(len(self.text) > len(self.key)):
            new_string = self.text[:len(self.key)]
            list_string.append(new_string)
            self.text = self.text[len(self.key):]
        list_string.append(self.text)
        return list_string
    def _convert_to_number(self, text):
        nums = []
        for char in text:
            nums.append(ord(char) - 65)
        return nums

    def _conver_to_word(self, nums):
        text = ""
        for num in nums:
            text = text + chr(int(num)+65)
        return text
    def _encrypt(self):
        splitted_strings = self._split()
        key_nums = self._convert_to_number(self.key)
        ciphers = ""
        for text in splitted_strings:
            text_nums = self._convert_to_number(text)
            cipher_nums = map(operator.add, text_nums, key_nums[:len(text)])
            ciphers = ciphers + self._conver_to_word(cipher_nums)
        return ciphers
    def _decrypt(self):
        splitted_strings = self._split()
        key_nums = self._convert_to_number(self.key)
        ciphers = ""
        for text in splitted_strings:
            text_nums = self._convert_to_number(text)
            cipher_nums = map(operator.sub, text_nums, key_nums[:len(text)])
            ciphers = ciphers + self._conver_to_word(cipher_nums)
        return ciphers
def main():
    key = "abcd"
    plain_text ="saphisaphisaphi"
    v = VigenereCipher(key,plain_text)
    print "Plain text: " + v.text
    print "Key: " + v.key
    print "Cipher text: " + v._encrypt()
    cipher_text = "SBRKITCSHJUDPIK"
    v = VigenereCipher(key,cipher_text)
    print "Plain_text: "+v._decrypt()
if __name__ == '__main__':
    main()
