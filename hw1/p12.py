def canDivideIntoSets(nums, k):
    # Sort the array to make it easier to find consecutive numbers.
    nums.sort()
    
    def divideHelper(start):
        if start == len(nums):
            return True  # All elements have been grouped into sets
        
        # Try to find a set of k consecutive numbers starting from 'start'.
        for i in range(k):
            current = nums[start] + i
            if current not in nums:
                return False  # Consecutive number is missing
            else:
                nums.remove(current)  # Remove the used number from the array
            
        # Recursively continue with the next starting point.
        return divideHelper(start)
    
    return divideHelper(0)

# Read input
nums = list(map(int, input().split()))
k = int(input())

# Check if it's possible to divide into sets of k consecutive numbers
result = canDivideIntoSets(nums, k)
print(result)
