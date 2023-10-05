# 021ab66c-0f42-46c3-a577-7e22faa3050f

def countWays(height, maxSteps, dp): 
    if height <= 1:
        return 1

    if dp[height] != -1:
        return dp[height]

    dp[height] = 0 

    for i in range(1, min(height, maxSteps) + 1):
        dp[height] += countWays(height - i, maxSteps, dp) 

    return dp[height]

height = int(input())
maxSteps = int(input())
dp = [-1 for _ in range(height + 1)]
print(countWays(height, maxSteps, dp))
