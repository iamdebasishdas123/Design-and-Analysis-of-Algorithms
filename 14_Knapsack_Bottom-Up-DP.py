def knapsack(W, wt, val, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

max_value = knapsack(W, wt, val, n)
print("Maximum value in Knapsack =", max_value)
