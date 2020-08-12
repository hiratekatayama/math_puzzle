class Solution(object):
    def MaxSubarray(self, input):
        max_sum = input[0]
        for i in range(0, len(input)+1):
            for j in range(len(input)-i):
                first = j
                last  = j + i + 1
                max_sum = max(sum(input[first:last]), max_sum)
        return max_sum

    def MaxSubarray2(self, input):
        max_sum = input[0]
        min_sum = 0
        for i in input:
            if min_sum < 0:
                print(i)
                min_sum = 0
            min_sum += i
            max_sum = max(max_sum, min_sum)
        return max_sum


if __name__ == "__main__":
    test = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    #nums = [1]
    #nums = [1,2]

    check = test.MaxSubarray2(nums)
    print(check)