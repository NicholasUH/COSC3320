# eff505c4-7c9f-4730-9705-ec8ba17b7fea
'''
Given an array A, write a program to find the max(A[j]-A[i]) where i < j. 
If max(A[j]-A[i])<0, output 0. The input will start with an integer n, which indicates 
the length of the given array. The next line will be the array.
'''

'''
Variables:
left = holds the lowest value in array
right = iterates through lists looking for the highest difference after left pointer
current_maximum = holds the highest maximum different
'''

'''
Logic:
use a left and right pointer to create a "sliding window", left starts on index 0, right
starts on index 1

use the right pointer to traverse the array and evaluate each index based on its value
    -if a new lowest value was found ,move left pointer to where right currently is 
    and continue traversing
    -else, see if the current value provides a new maximum difference, if it does, update
    the current maximum, and continue traversing
'''


def find_maximum_difference(arr,arr_length):
    left, right,current_maximum = 0, 1, 0
    while right < arr_length:
        if arr[left] < arr[right]:
            current_maximum = max(current_maximum, arr[right] - arr[left])
        elif(arr[left] > arr[right]):
            left = right
        right += 1
    return current_maximum
            

def main():
    n = int(input())
    array = list(map(int,input().split()))
    print(find_maximum_difference(array,n))



main()

