class Solution(object):
    def ClimbingStairs(self, input):
        memo = [0]*(input + 1)
        return self.ClimbingStairText(0, input)

    def ClimbingStairText(self, num, input):
        if num > input:
            return 0
        if num == input:
            return 1
        result = self.ClimbingStairText(num, input-1) + self.ClimbingStairText(num, input-2)

        return result

    def ClimbingStairText2(self, num, input):
        if num > input:
            return 0
        if num == input:
            return 1
        result = self.ClimbingStairText2(num+1, input) + self.ClimbingStairText2(num+2, input)

        return result

    def memoClimbingStairText(self, num, input, memo):
        if (num > input):
            return 0
        if (num == input):
            return 1
        if (memo[input])

if __name__ == "__main__":
    test = Solution()

    input_num = 3
    check = test.ClimbingStairs(input_num)
    print(check)