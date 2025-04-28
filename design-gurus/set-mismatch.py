def find_missing(nums):
    missing_number = 0
    duplicate = 0
    found_numbers = {}

    for i in range(len(nums)):
        current_num = nums[i]
        if current_num in found_numbers:
            duplicate = current_num
        found_numbers[current_num] = True

    for i in range(1, len(nums)):
        if i not in found_numbers:
            missing_number = i
            break
    if missing_number == 0:
        if 1 not in found_numbers:
            missing_number = 1
        elif len(nums) not in found_numbers:
            missing_number = len(nums)

    return [duplicate, missing_number]

print(find_missing([1,3,3,4]))
print(find_missing([1,2,2,4]))
print(find_missing([2,2,3,5,4]))
print(find_missing([1,5,3,2,7,7,6]))
print(find_missing([1,5,3,2,4,7,7,6]))
print(find_missing([5,3,2,4,7,7,6]))