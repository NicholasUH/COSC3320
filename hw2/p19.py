def merge_sort(arr1, arr2, left, right, points1, points2):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr1, arr2, left, mid, points1, points2)
        merge_sort(arr1, arr2, mid + 1, right, points1, points2)

        merge_helper(arr1, arr2, left, mid, right, points1, points2)

    return

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
    leftSubarr1 = arr1[left:mid + 1]
    rightSubarr1 = arr1[mid + 1:right + 1]

    leftSubarr2 = arr2[left:mid + 1]
    rightSubarr2 = arr2[mid + 1:right + 1]

    




def main():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    robert_score,rachel_score = merge_sort(arr1,arr2)
    print(f"{robert_score} {rachel_score}")
