def optimal_bottling(prices):
    n = len(prices) - 1
    revenue = [0] * (n + 1)
    bottles = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = float('-inf')
        max_j = -1
        for j in range(1, i + 1):
            if prices[j] + revenue[i - j] > max_val:
                max_val = prices[j] + revenue[i - j]
                max_j = j
        revenue[i] = max_val
        bottles[i] = max_j

    result = []
    while n > 0:
        result.append(bottles[n])
        n -= bottles[n]

    return result

# Take input from the user
prices_input = input()
prices = list(map(int, prices_input.split()))

# Call the function with the input prices
output = optimal_bottling(prices)

print(" ".join(map(str, output)))
