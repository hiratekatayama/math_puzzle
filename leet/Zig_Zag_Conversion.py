class Solution(object):
    def ZigZag(self, str_list, num_rows):
        output = [[]]
        now_len = 0
        for i in range(str_list):
            output[i, j] = str_list[i]
            now_len += 1
            if now_len == num_rows:
                now_len

            for j in range(num_rows):

        return str_list[:4]

if __name__ == "__main__":
    test = Solution()

    s = "PAYPALISHIRING"
    numRows = 3

    result = test.ZigZag(s, numRows)
    print(result)