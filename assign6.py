def knapsack_top_down(weights, values, capacity, n, memo):
    if n == 0 or capacity == 0:
        return 0
        
    if memo[n][capacity] != -1:
        return memo[n][capacity]
        
    if weights[n-1] <= capacity:
        memo[n][capacity] = max(
            values[n-1] + knapsack_top_down(weights, values, capacity - weights[n-1], n - 1, memo),
            knapsack_top_down(weights, values, capacity, n - 1, memo)
        )
        return memo[n][capacity]
    else:
        memo[n][capacity] = knapsack_top_down(weights, values, capacity, n - 1, memo)
        return memo[n][capacity]


def knapsack_bottom_up(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[n][capacity]


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    n = len(values)
    
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    max_val_top_down = knapsack_top_down(weights, values, capacity, n, memo)
    print(max_val_top_down)
    
    max_val_bottom_up = knapsack_bottom_up(weights, values, capacity)
    print(max_val_bottom_up)