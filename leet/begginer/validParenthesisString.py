class Solution(object):
  def validParenthesisString(self, s): #brutefoce
    if not s:
      return True
    A = list(s)
    self.ans = False

    def solve(i):
      if i == len(A):
        self.ans |= valid()
      elif A[i] == "*":
        for c in "()":
          A[i] = c
          solve(i+1)
          if self.ans:
            return 
        A[i] = "*"
      else:
        solve(i+1)

    def valid():
      bal = 0
      for x in A:
        if x == "(":
          bal += 1

        if x == ")":
          bal -= 1

        if bal < 0:
          break

      return bal == 0

    solve(0)
    return self.ans

  def checkValidString(self, s):
    if not s:
      return True
      LEFTY, RIGHTY = "(*", ")*"

    n = len(s)
    dp = [[False] * n for _ in s]
    for i in range(n):
      if s[i] == "*":
        dp[i][i] = True
      if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
        dp[i][i+1] = True
    
    for size in range(2, n):
      for i in range(n - size):
        if s[i] == "*" and dp[i+1][i+size]:
          dp[i][i+size] = True
        elif s[i] in LEFTY:
          for k in range(i+1, i+size+1):
            if (s[k] in RIGHTY and (k == i+1 or dp[i+1][k-1]) and (k == i+size or dp[i+1][i+size])):
              dp[i][i+size] = True

      return dp[0][-1]

if __name__ == '__main__':
  input = "(*)"

  test = Solution()
  print(test.checkValidString(input))
