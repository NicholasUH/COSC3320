# 6adda463-5d76-476d-a81c-905c5236488e
def is_stepping_number(num):
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

        if last_digit > 0:
            backtrack(curr_num * 10 + (last_digit - 1))

        if last_digit < 9:
            backtrack(curr_num * 10 + (last_digit + 1))

    for i in range(10):
        backtrack(i)

    return sorted(stepping_numbers)

def main():
    low = int(input())
    high = int(input())

    result = generate_stepping_numbers(low, high)
    print(' '.join(str(num) for num in result)) 

main()

