# Bruteforce
# def sol(nums):
#     max_area = 0
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             curr_area = min(nums[i], nums[j]) * (j - i)
#             max_area = max(curr_area, max_area)

#     return max_area


def sol(nums):
    max_area = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        curr_area = min(nums[left], nums[right]) * (right - left)
        max_area = max(max_area, curr_area)
        if nums[right] > nums[left]:
            left += 1
        else:
            right -= 1

    return max_area

# print(sol([1, 3, 2, 4, 5]))
# print(sol([5, 2, 4, 2, 6, 3]))
print(sol([2, 3, 4, 5, 18, 17, 6]))
# print(sol([2, 3, 5, 1, 3, 1]))
