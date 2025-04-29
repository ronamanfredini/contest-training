def bin_search(arr, x):
    left = 0
    right = len(arr) - 1
    mid = 0
    while left <= right:
        mid = (right + left) // 2
        print(left, right, mid)
        if arr[mid] == x:
            break
        if arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
        
        
    else:
        if right == -1:
            return 0
        if left == len(arr):
            return len(arr)
        
        if left > right:
            return left
        else:
            return right

    return mid

print(bin_search([1,3,5,6], 2))