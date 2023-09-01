# e4b509d7-1a81-4f6f-93d3-2d8d957a00cf

'''
Given an array A, write a program to find the max(A[j]-A[i]) where i < j. 
If max(A[j]-A[i])<0, output 0. The input will start with an integer n, which indicates 
the length of the given array. The next line will be the array.
'''

def find_maximum_difference(arr,arr_length):
    left, right,current_maximum = 0, 1, 0
    while right < arr_length:
        if arr[left] < arr[right]:
            current_maximum = max(current_maximum, arr[right] - arr[left])
        else:
            left = right
        right += 1
    return current_maximum
            

n = int(input())
array = list(map(int,input().split()))
print(find_maximum_difference(array,n))