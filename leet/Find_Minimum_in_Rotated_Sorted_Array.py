class Solution(object):
    def find_min(self, list):
        min = list[0]
        for i in range(1, len(list)):
            if min > list[i]:
                min = list[i]
        return min

if __name__ == "__main__":
    test = Solution()
    list = [2,2,0]

    print(test.find_min(list))
