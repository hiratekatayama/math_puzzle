class Solution(object):
  def maxProfit(self, prices): #fruteforce
    return self.calculate(prices, 0)

  def calculate(self,prices, s):
    if s >= len(prices):
      return 0
    max = 0
    for start in range(s, len(prices)):
      maxprofit = 0
      for i in range(start+1, len(prices)):
        if prices[start] < prices[i]:
          profit = self.calculate(prices, i+1) + prices[i] - prices[start]
          if profit > maxprofit:
            maxprofit = profit

      if maxprofit > max:
        max = maxprofit
    return max

  def calculate_2(self, prices): #peak valley approach
    i = 0
    vally = prices[0]
    peak = prices[0]
    maxprofit = 0

    while i < len(prices)-1:
      while i < len(prices)-1 and prices[i] >= prices[i+1]:
        i += 1
      valley = prices[i]
      while i < len(prices)-1 and prices[i] <= prices[i+1]:
        i += 1
      peak = prices[i]
      maxprofit += peak - valley
    return maxprofit

if __name__ == '__main__':
  input_list = [7,1,5,3,6,4]

  test = Solution()
  print(test.maxProfit(input_list))
  print(test.calculate_2(input_list))

