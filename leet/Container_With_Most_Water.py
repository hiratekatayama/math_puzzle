class Solution(object):
    def maxArea(self, height):
        max_area = 0

        for i in range(0,len(height)):
            for j in range(i+1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j-i))

        return max_area

    def maxArea2(self, height):
        max_area = 0; l = 0; r = len(height) - 1
        while l < r:
           max_area = max(max_area, min(height[l], height[r]) * (r-l))
           if height[l] < height[r]:
                l += 1
           else:
                r -= 1
        return max_area

if __name__ == "__main__":
    test = Solution()
    input_list = [1,8,6,2,5,4,8,3,7]

    print(test.maxArea(input_list))
    print(test.maxArea2(input_list))