class Solution(object):
    def HouseRobber(self, input):
        dp = [0] * len(input)
        max_len = 0
        for i in range(len(input)):
            dp[i] = dp[i] + input[i]
            mat = 0
            for j in range(0, i):
                if j < i-1:
                    mat = max(mat, dp[i] + dp[j])
            if mat > dp[i]:
                dp[i] = mat
            if max_len < dp[i]:
                max_len = dp[i]

        return max_len

    def Rob(self, input):
        a, b = 0, 0

        for n in input:
            a, b = b, max(a+n, b)
        return b

if __name__ == "__main__":
    test = Solution()
    nums = [2,7,9,3,1]

    check = test.HouseRobber(nums)
    print("===my answer===")
    print(check)

    check = test.Rob(nums)
    print("===right answer===")
    print(check)