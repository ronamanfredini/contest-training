def sol(nums, k):
    result = []
    for num in nums:
        if len(result) == 0:
            result.append(num)
            continue

        if result[-1] * num <= k:
            result[-1] *= num
        else:
            result.append(num)
    return len(result)

print(sol([2, 3, 4, 5], 10))
print(sol([1,2,2,3], 5))
print(sol([10,5,2,3,4,2,20,1], 50))