def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1
    for denoms in denoms:
        for amount in range(1, n + 1):
            if denoms <= amount:
                ways[amount] = ways[amount] + ways[amount - denoms]

    return ways[n]
