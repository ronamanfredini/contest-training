def solution(nums):
    array_count = [0]


    def dfs(i, difference, last_idx, sequence_len):
        if i >= len(nums):
            return

        if last_idx == -1:
            dfs(i + 1, nums[i + 1] - nums[i], i, 1)

        current_difference = nums[i] - nums[last_idx]
        if current_difference > difference:
            return

        if current_difference == difference:
            if sequence_len + 1 >= 3:
                array_count[0] += 1
            dfs(i + 1, difference, i, sequence_len + 1)

        else:
            dfs(i + 1, difference, last_idx, sequence_len)

    dfs(0, 0, -1, 0)
    return array_count[0]

print(solution([1, 2, 3, 4])) # 3
# print(solution([1, 3, 5, 7, 9])) # 6
# print(solution([7, 7, 7, 7])) # 0