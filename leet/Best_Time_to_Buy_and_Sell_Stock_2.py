class Solution(object):
    def maxProfit(self, prices):
        return self.Best_Time_to_Buy(prices, 0)

    def Best_Time_to_Buy(self, prices, nums):
        if nums > len(prices):
            return 0
        max = 0
        for start in range(nums, len(prices)):
            maxprofit = 0
            for i in range(start+1, len(prices)):
                if prices[start] < prices[i]:
                    profit = self.Best_Time_to_Buy(prices, i+1) + prices[i] - prices[start]
                    if profit > maxprofit:
                        maxprofit = profit
            if maxprofit > max:
                max = maxprofit
        return max

    def Peak_Valley_Approach(self, prices):
        i = 0
        valley    = prices[0]
        peak      = prices[0]
        maxprofit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley

        return maxprofit

    def Simple_One_Pass(self, prices):
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit

if __name__ == "__main__":
    test = Solution()

    input = [7,1,5,3,6,4]
    check = test.maxProfit(input)
    print(check)

    check = test.Peak_Valley_Approach(input)
    print(check)