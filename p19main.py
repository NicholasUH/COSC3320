def merge_sort(arr1, arr2, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr1, arr2, start, mid)
        merge_sort(arr1, arr2, mid + 1, end)
        merge(arr1, arr2, start, mid, end)

def merge(arr1, arr2, start, mid, end):
    left_len = mid - start + 1
    right_len = end - mid

    left_half1 = arr1[start : mid + 1]
    left_half2 = arr2[start : mid + 1]

    right_half1 = arr1[mid + 1 : end + 1]
    right_half2 = arr2[mid + 1 : end + 1]

    i = j = 0
    k = start

    while i < left_len and j < right_len:
        if left_half1[i] <= right_half1[j]:
            arr1[k] = left_half1[i]
            arr2[k] = left_half2[i]
            i += 1
        else:
            arr1[k] = right_half1[j]
            arr2[k] = right_half2[j]
            j += 1
        k += 1

    while i < left_len:
        arr1[k] = left_half1[i]
        arr2[k] = left_half2[i]
        i += 1
        k += 1

    while j < right_len:
        arr1[k] = right_half1[j]
        arr2[k] = right_half2[j]
        j += 1
        k += 1

# Example usage
arr1 = [38, 27, 43, 3, 9, 82, 10]
arr2 = [5, 2, 8, 1, 15, 6, 7]
print("Original array 1:", arr1)
print("Original array 2:", arr2)
merge_sort(arr1, arr2, 0, len(arr1) - 1)
print("Sorted array 1:", arr1)
print("Sorted array 2:", arr2)
