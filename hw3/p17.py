# 07b9993c-b8de-46ee-9fc0-ad607fcbd3f3
def find_rotation_index(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return left

def search_in_rotated_array(arr, target):
    def binary_search(left, right):
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    rotation_index = find_rotation_index(arr)

    # Check which segment of the array the target may lie in
    if arr[rotation_index] <= target <= arr[-1]:
        return binary_search(rotation_index, len(arr) - 1)
    else:
        return binary_search(0, rotation_index - 1)



def main():
    arr = list(map(int,input().split()))
    value = int(input())
    
    print(find_rotation_index(arr))
    print(search_in_rotated_array(arr,value))

main()