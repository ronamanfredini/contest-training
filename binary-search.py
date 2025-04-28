def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


print(binary_search([1,2,3,4,5,6,7,8,9,10], 5))
print(binary_search([1,2,3,4,5,6,7,8,9,10], 1))