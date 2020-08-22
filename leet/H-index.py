class Solution(object):
    def H_index(self, citations):
        citations = sorted(citations, reverse=True)
        for cite_num in range(len(citations)):
            print(citations[cite_num], cite_num)
            if citations[cite_num] < cite_num + 1:
                return cite_num

        return len(citations)


if __name__ == "__main__":
    test      = Solution()
    citations = [1]
    check     = test.H_index(citations)
    print(check)

    citations = [3,0,6,1,5]
    check = test.H_index(citations)
    print(check)

    citations = []
    check = test.H_index(citations)
    print(check)

    citations = [0]
    check = test.H_index(citations)
    print(check)
