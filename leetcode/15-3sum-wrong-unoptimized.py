class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		result = set()
		def dfs(i, current_set):
			if len(current_set) == 3:
				i1, j, k = nums[current_set[0]], nums[current_set[1]], nums[current_set[2]]
				if i1 + j + k == 0 and tuple(current_set) not in result:
					result.add(tuple(current_set))
			if i >= len(nums):
				return
					
			current_set.append(i)
			dfs(i + 1, current_set)
			current_set.pop()
			dfs(i + 1, current_set)
				

		dfs(0, [])

		return list(result)


s = Solution()

print(s.threeSum([-1,0,1,2,-1,-4]))