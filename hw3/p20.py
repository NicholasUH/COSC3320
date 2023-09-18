# 1b356a92-d664-49c1-956c-49f2188b02b7
def is_stepping_number(num):
    # Helper function to check if a number is a stepping number
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if abs(int(num_str[i]) - int(num_str[i+1])) != 1:
            return False
    return True

def generate_stepping_numbers(low, high):
    stepping_numbers = []

    def backtrack(curr_num):
        if low <= curr_num <= high and is_stepping_number(curr_num):
            stepping_numbers.append(curr_num)

        if curr_num == 0 or curr_num > high:
            return

        last_digit = curr_num % 10

        # Explore adjacent digits
        if last_digit > 0:
            backtrack(curr_num * 10 + (last_digit - 1))

        if last_digit < 9:
            backtrack(curr_num * 10 + (last_digit + 1))

    for i in range(10):
        backtrack(i)

    return sorted(stepping_numbers)

# Read input
low = int(input())
high = int(input())

# Generate and print stepping numbers in the range
result = generate_stepping_numbers(low, high)
print(' '.join(str(num) for num in result))
