# 5b65288e-7c67-4365-bcf3-21809c5dafd1

def divideConsecutive(nums, k):
    if(k == 0 or k == 1):
        return "true"
    
    if len(nums) == 0:
        return "true"
    
    if len(nums) % k != 0:
        return "false"
    
    
    minNum = min(nums)
    
    if minNum + k - 1 not in nums:
        return "false"
    
    for i in range(k):
        if minNum + i in nums:
            nums.remove(minNum + i) 
        else:
            return "false"
    
    return divideConsecutive(nums, k)

def main():
    array = list(map(int, input().split()))
    k = int(input());

    print(divideConsecutive(array,k))
    
main()
