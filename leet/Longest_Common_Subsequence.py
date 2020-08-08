class Solution(object):
    def Longest_Common_Subsequence(self, text1, text2):
        dp      = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for j in range(1, len(text1) + 1):
            for i in range(1, len(text2) + 1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)

        return dp[len(text2)][len(text1)]

if __name__ == "__main__":
    test = Solution()

    text1 = "abcde"
    text2 = "ace"
    check = test.Longest_Common_Subsequence(text1, text2)
    print(check)