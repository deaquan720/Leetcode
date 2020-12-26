class Solution:
    def minCost(self, houses, cost, m, n, target):
        for i in range(m):
            if houses[i] != 0:
                cost[i] = [float('inf')]*n
                cost[i][houses[i]-1] = 0
        
        dp = [[[float('inf')] * n for _ in range(target + 1)] for _ in range(m)]
        for j in range(n):
            dp[0][1][j] = cost[0][j]
        
        for i in range(1, m):
            for k in range(1, min(i+2, target+1)):
                for j in range(n):
                    res = min(dp[i-1][k-1][c] + cost[i][j] for c in range(n) if c!=j) 
                    res = min(res, dp[i-1][k][j] + cost[i][j])
                    dp[i][k][j] = res
                
        res = min(dp[m-1][target])
        return res if res != float('inf') else -1
