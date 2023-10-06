# 1724c025-8be3-4681-ac79-10810c974574

def countWays(height, maxSteps, dp): 
    if height <= 1:
        return 1

    if dp[height] != -1:
        return dp[height]

    dp[height] = 0 

    for i in range(1, min(height, maxSteps) + 1):
        dp[height] += countWays(height - i, maxSteps, dp) 

    return dp[height]

def main():
    height = int(input())
    maxSteps = int(input())
    dp = [-1 for _ in range(height + 1)]
    print(countWays(height, maxSteps, dp))  


main()