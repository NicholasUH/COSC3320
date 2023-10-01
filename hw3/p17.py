# fb727d92-2a38-4017-80f9-9389b817ae25
def find_rotation_index(arr, low, high):
    if low >= high:
        return low
    
    mid = (low + high) // 2
    if arr[mid] > arr[high]:
        return find_rotation_index(arr, mid+1, high)
    else:
        return find_rotation_index(arr, low, mid)

def find_value(arr, value):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if value== arr[mid]:
            return mid

        if arr[low] <= arr[mid]:
            if value> arr[mid] or value< arr[low]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if value< arr[mid] or value> arr[high]:
                high = mid - 1
            else:
                low = mid + 1
    return -1

def main():
    arr = list(map(int,input().split()))
    value = int(input())
    
    print(find_rotation_index(arr, 0, len(arr) - 1))
    print(find_value(arr, value))

main()