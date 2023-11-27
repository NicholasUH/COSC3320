def job_profit_scheduling(start_time, end_time, profit):
    n = len(start_time)
    tasks = sorted(zip(start_time, end_time, profit), key=lambda x: x[1])

    dp = [0] * n
    dp[0] = tasks[0][2]

    for i in range(1, n):
        j = i - 1
        while j >= 0 and tasks[j][1] > tasks[i][0]:
            j -= 1

        dp[i] = max(dp[i - 1], tasks[i][2] + (dp[j] if j >= 0 else 0))

    return dp[-1]

def main():
    start_time = list(map(int, input().split()))
    end_time = list(map(int, input().split()))
    profit = list(map(int, input().split()))
    print(job_profit_scheduling(start_time, end_time, profit))

main()