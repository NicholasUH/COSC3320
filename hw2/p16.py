# 7160b9de-6557-42ee-88e0-185a3b234fd5
def lastRemainingNumber(n, leftStart = 1):
    if n == 1:
        return 1

    if leftStart == 1 or n % 2 == 1:
        return 2 * lastRemainingNumber(n // 2, 1 - leftStart)
    else:
        return 2 * lastRemainingNumber(n // 2, 1 - leftStart) - 1


def main():
    print(lastRemainingNumber(int(input())))


main()
