import heapq
# passes 7/10 test cases
def divideConsecutive(nums, k):

    if len(nums) == 0:
        return "true"
    
    if len(nums) % k != 0:
        return "false"
    
    minNum = min(nums)
    
    nums.sort()
    
    for i in range(k):
        if minNum + i in nums:
            nums.remove(minNum + i) 
        else:
            return "false"
    
    return divideConsecutive(nums, k)


nums = list(map(int, input().split()))
k = int(input())
print(divideConsecutive(nums,k))
