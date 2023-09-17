def merge_sort(arr1, arr2, left, right, points1, points2):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr1, arr2, left, mid, points1, points2)
        merge_sort(arr1, arr2, mid + 1, right, points1, points2)

        merge_helper(arr1, arr2, left, mid, right, points1, points2)

def count_helper(arr1,arr2):

    index = final_score = 0

    while index < len(arr1):
        curr_score = 0
        while curr_score < len(arr1) and arr2[index] < arr1[index]:
            curr_score += 1
        final_score += curr_score
        index += 1
    
    return final_score

def merge_helper(arr1, arr2, left, mid, right,points1, points2):

    size1 = (right - left) + 1
    size2 = right - mid

    leftSubarr1 = arr1[left:mid + 1]
    rightSubarr1 = arr1[mid + 1:right + 1]

    leftSubarr2 = arr2[left:mid + 1]
    rightSubarr2 = arr2[mid + 1:right + 1]


    i1 = i2 = j1 = j2 = 0
    index1 = index2 = left

    if i1 < size1 and j1 < size2:
        points1 += count_helper(leftSubarr2,rightSubarr1)
        i1 += 1

    if i2 < size1 and j2 < size2:
        points2 += count_helper(leftSubarr1,rightSubarr2)


    #merge back subarrays

    


def main():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    score1,score2 = 0,0
    merge_sort(arr1, arr2, 0 , max(len(arr1),len(arr2)) - 1, score1,score2)
    print(f"{score1} {score2}")


main()


#5 3 6 9
#7 5 8 4
