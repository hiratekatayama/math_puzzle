import math

class Solution(object):
    def distributeCandies(self, candies, num_people):
        k, n = num_people, candies
        alloc = [0]*k
        Final = (0, 0)
        for i in range(1, k+1):
            s = ((-1-2*i) + math.sqrt(1+8*n)) / (2*k)
            t = math.floor(s)
            alloc[i-1] = i*(t+1) + k*t*(t+1)//2
            Final      = max(Final, (s - math.floor(s), i))
        alloc[Final[1]-1] += (n - sum(alloc))
        return alloc

if __name__ == "__main__":
    input = Solution()
    candies    = 10
    num_people = 3

    check = input.distributeCandies(candies, num_people)
    print(check)