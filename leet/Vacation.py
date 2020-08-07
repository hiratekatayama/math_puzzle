class Solution(object):
    def Vacation(self, N, test):
        dp = [[0 for _ in range(3)] for _ in range(len(test)+1)]

        for i in range(len(test)):
            for j in range(len(test[0])):
                for k in range(len(dp[0])):
                    if j != k:
                        dp[i+1][j] = max(dp[i+1][j], dp[i][k] + test[i][j])

        print(dp)
        max_len = dp[len(test)][0]
        for i in range(1, len(dp[0])):
            if max_len < dp[len(test)][i]:
                max_len = dp[len(test)][i]

        return max_len

if __name__ == "__main__":
    test = Solution()

    print("input N")
    N = int(input())
    a = [[0 for i in range(3)] for j in range(N)]
    for i in range(N):
        for j in range(3):
            print("input a[" + str(i) + "][" + str(j) + "]")
            a[i][j] = int(input())

    print(test.Vacation(N, a))