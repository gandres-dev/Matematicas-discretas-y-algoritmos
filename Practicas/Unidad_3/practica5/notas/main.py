def knapsack_memo_2(weights, values, capacity, memo=None):
    if memo is None:
        memo = [[None for _ in range(len(weights))] for _ in range(capacity+1)]
        
        for c in range(capacity+1):
            memo[c][0] = values[0] if weights[0] <= c else 0

        for i in range(len(weights)):
            memo[0][i] = 0
    for i in range(1, len(weights)):
        for c in range(1, capacity+1):
            p1 = memo[c][i-1]
            p2 = 0
            if weights[i] <= c:
                p2 = values[i] + memo[c-weights[i]][i-1]
            memo[c][i] = max(p1, p2)
    return memo[capacity][len(weights)-1]