# b4da6e55-e0ab-4e40-b1b9-1e2a4d8fab69

def lastRemainingNumber(n, leftStart=1):
    if n == 1:
        return 1

    if leftStart == 1 or n % 2 == 1:
        return 2 * lastRemainingNumber(n // 2, 1 - leftStart)
    else:
        return 2 * lastRemainingNumber(n // 2, 1 - leftStart) - 1


def main():
    print(lastRemainingNumber(int(input())))


main()
