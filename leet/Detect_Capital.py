import re

class Solution(object):
    def detect_capital(self, word):
        if word[0].isupper():
            if len(word) == 1 or word[1:].isupper() or word[1:].islower():
                return True
        if word.islower():
            return True

        return False

if __name__ == "__main__":
    test = Solution()

    input = "G"

    check = test.detect_capital(input)
    print(check)