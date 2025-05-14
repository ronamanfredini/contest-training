def sol(nums, target):
    solutions = set()

    def backtrack(i, curr_set=None):
        if curr_set is None:
            curr_set = []

        s_sum = sum(curr_set)
        if i >= len(nums) or s_sum > target:
            return

        if sum(curr_set) == target:
            curr_set.sort()
            solutions.add(tuple(curr_set))
            return

        backtrack(i + 1, curr_set)
        curr_set.append(nums[i])
        backtrack(i, curr_set)
        curr_set.pop()

    backtrack(0)

    return [list(s) for s in solutions]



print(sol([2, 3, 6, 7], 7))
print(sol([7, 3, 2], 18))

