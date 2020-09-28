def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    coins = [float("inf") for i in range(n + 1)]
    coins[0] = 0
    for denoms in denoms:
        for amount in range(1, n + 1):
            if denoms <= amount:
                coins[amount] = coins[amount - denoms] + 1 if coins[amount - denoms] + 1 < coins[amount] else coins[
                    amount]
    return coins[n] if coins[n] != float("inf") else -1

