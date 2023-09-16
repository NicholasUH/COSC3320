#d167d60f-f038-464c-9916-cc6e1a2fea1e

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
