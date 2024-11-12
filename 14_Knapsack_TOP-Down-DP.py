def knapsack_util(wt, val, n, W, dp):
    if n == 0 or W == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
    
    if wt[n-1] > W:
        dp[n][W] = knapsack_util(wt, val, n-1, W, dp)
    else:
        include = val[n-1] + knapsack_util(wt, val, n-1, W - wt[n-1], dp)
        exclude = knapsack_util(wt, val, n-1, W, dp)
        dp[n][W] = max(include, exclude)
    
    return dp[n][W]

def knapsack(W, wt, val):
    n = len(val)
    dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
    return knapsack_util(wt, val, n, W, dp)

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50

max_value = knapsack(W, wt, val)
print("Maximum value in Knapsack =", max_value)
