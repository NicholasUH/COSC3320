# 7/10
import sys

def function(array):
    if len(array) < 3:
        return False
    
    # have more losses than combined wins and draws in the last three games
    if array[-3:].count('L') > array[-3:].count('W') + array[-3:].count('D'):
        print("True by losses")
        return True
    
    # have not had a win in the last four games
    if array[-4:].count('W') == 0 and len(array) > 3:
        print("True by no wins")
        return True
    
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    
    return function(left_array) or function(right_array)


array = sys.stdin.readline().split()

if function(array):
    print("T")
else:
    print("F")