class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        for start in range(len(nums)):
            for end in range(start + 1, len(nums)):
                sum = 0
                for pointer in range(start, end + 1):
                    sum += nums[pointer]
                if sum == k:
                    count += 1
        return count

    def subarraySum2(self, nums, k):
        count = 0
        sum = [0] * (len(nums) + 1)
        sum[0] = 0
        for i in range(1, len(nums)):
            sum[i] = sum[i - 1] + nums[i - 1]
        for start in range(len(nums)):
            for end in range(start+1, len(nums)):
                if sum[end] - sum[start] == k:
                    count += 1
        return count

if __name__ == "__main__":
    test = Solution()

    nums = [1,1,1]
    k    = 2
    check = test.subarraySum(nums, k)
    print(check)

    check = test.subarraySum2(nums, k)
    print(check)

#public class Solution {
#    public int subarraySum(int[] nums, int k) {
#        int count = 0;
#        for (int start = 0; start < nums.length; start++) {
#            for (int end = start + 1; end <= nums.length; end++) {
#                int sum = 0;
#                for (int i = start; i < end; i++)
#                    sum += nums[i];
#                if (sum == k)
#                    count++;
#            }
#        }
#        return count;
#    }
#}