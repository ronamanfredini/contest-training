def solution(nums):
    max_len = 0
    if len(nums) <= 1:
        return 0
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                max_len = max(max_len, j - i + 1)
    return max_len


print(solution([1, 2, 3, 4, 5]))  
print(solution([8, 4, 5, 3, 2]))  
print(solution([1,2,12,2,5,11,13]))
print(solution([2,1,4,7,5,3]))  