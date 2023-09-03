import heapq
'''
Given an array of positive integers nums and a positive integer k, check whether it is 
possible to divide nums into sets of k consecutive numbers.

Write a recursive function to solve this problem. Return true if it is possible. 
Otherwise, return false. The input has 2 lines. The first line is the array of positive 
integers nums. The second line is the positive integer k.
'''

def can_divide_into_k_subsets(minHeap, k):
    if len(minHeap) == 0:
        return True
    
    temp = []
    def can_divide(counter, currNum):
        if counter == 0:
            return True
        
        if len(minHeap) == 0:
            return False
        
        if currNum == minHeap[0]+1:
            temp.append(heapq.heappop(minHeap))
            return can_divide(counter, currNum)
        elif currNum == minHeap[0]:
            heapq.heappop(minHeap)
            return can_divide(counter-1, currNum+1)
        else:
            return False
        
    if can_divide(k, minHeap[0]):
        for x in temp:
            heapq.heappush(minHeap, x)
        return can_divide_into_k_subsets(minHeap, k)
    
    return False

def main():
    array = list(map(int,input().split()))
    k = int(input())
    heapq.heapify(array)
    if can_divide_into_k_subsets(array,k):
        print("true")
    else:
        print("false")

main()