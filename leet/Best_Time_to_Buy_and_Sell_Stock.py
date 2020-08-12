class Solution(object):
    def Best_Time_to_Buy_Sll(self, nums):
        start = nums[0]
        max_num = 0
        for i in range(len(nums)):
            if start > nums[i]:
                start = nums[i]
            elif nums[i] - start > max_num:
                max_num = nums[i] - start

        return max_num

if __name__ == "__main__":
    test = Solution()
    input = [7,1,5,3,6,4]
    check = test.Best_Time_to_Buy_Sll(input)
    print(check)