class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        hash_lst = []
        for i in s:
            hash_num = hash(i)
            if hash_num in hash_lst:
                if max_len < len(hash_lst):
                    max_len = len(hash_lst)
                hash_lst = []
                hash_lst.append(hash_num)
            else:
                hash_lst.append(hash_num)
        return max_len

if __name__ == "__main__":
    test = Solution()
    input = " "
    check = test.lengthOfLongestSubstring(input)
    print(check)