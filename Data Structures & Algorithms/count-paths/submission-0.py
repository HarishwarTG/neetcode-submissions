class Solution:
    def uniquePaths(self, r: int, c: int) -> int:
        dp = [1] * c

        for i in range(r - 2, -1, -1):
            for j in range(c - 2, -1, -1):
                dp[j] += dp[j+1]
            
        return dp[0]