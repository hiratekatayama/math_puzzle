class Solution(object):
    def numsSameConsecDiff(self, N, K):
        if N == 1:
            return [i for i in range(10)]

        ans = []
        def DFS(N, num):
            if N == 0:
                return ans.append(num)
            tail_digit = num % 10
            next_digits = set([tail_digit+K, tail_digit-K])

            for next_digits in next_digits:
                if 0 <= next_digits and next_digits < 10:
                    new_num = num * 10 + next_digits
                    DFS(N-1, new_num)

        for num in range(1, 10):
            DFS(N-1, num)

        return list(ans)

    def numSameConsecDiff2(self, N, K):
        if N == 1:
            return [i for i in range(10)]

        queue = [digit for digit in range(1,10)]

if __name__ == "__main__":
    test = Solution()
    N = 3
    K = 2

    check = test.numsSameConsecDiff(N, K)
    print(check)