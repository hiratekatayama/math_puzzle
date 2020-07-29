class Solution(object):
    def addDigits(self, num):
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10

            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0

        return digital_root

    def addDigits_2(self, num):
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

if __name__ == "__main__":
    test = Solution()

    num = 38
    print(test.addDigits(num))

    print(test.addDigits_2(num))