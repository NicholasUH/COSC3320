# e7ee42d4-1251-4d61-a61e-c67ea784c217


def divideConsecutive(nums, k):
    if len(nums) == 0:
        return "true"
    
    if len(nums) % k != 0:
        return "false"
    
    minNum = min(nums)
    
    nums.sort()
    
    if k % 2 == 0:
        for i in range(k // 2):
            if minNum + i in nums:
                nums.remove(minNum + i)
            else:
                return "false"
             
            if minNum + k - 1 - i in nums:
                nums.remove(minNum + k - 1 - i)
            else:
                return "false"
    else:
        for i in range(k // 2):
            if minNum + i + 1 == minNum + k - 2 - i and minNum+i+1 in nums:
                nums.remove(minNum + i + 1)

            if minNum + i in nums:
                nums.remove(minNum + i)
            else:
                return "false"
            
            if minNum + k - 1 - i in nums :
                nums.remove(minNum + k - 1 - i)
            else:
                return "false"

    
    return divideConsecutive(nums, k)

def main():
    array = list(map(int, input().split()))
    k = int(input());

    print(divideConsecutive(array,k))
    
main()


'''
1 2 3 4 5 6 7 8 9
3

for 0 in range(2)



'''

