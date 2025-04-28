class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash_set = set(nums)
        longest_sequence = 0

        for num in hash_set:
            is_sequence_start = (num - 1) not in hash_set
            if is_sequence_start:
                curr_sequence_len = 1
                while (num + curr_sequence_len) in hash_set:
                    curr_sequence_len += 1
                
                longest_sequence = max(longest_sequence, curr_sequence_len)
        
        return longest_sequence

        
s = Solution()
print(s.longestConsecutive([ 100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([1,0,1,2]))