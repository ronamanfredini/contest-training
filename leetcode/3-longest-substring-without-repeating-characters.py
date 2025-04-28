class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_substring = 0
        curr_string = set()

        if len(s) == 1:
            return 1

        if len(s) == 0:
            return 0

        for right in range(len(s)):
            curr_char = s[right]
            while curr_char in curr_string:
                curr_string.remove(s[left])
                left += 1
            
            curr_string.add(curr_char)
            longest_substring = max(len(curr_string), longest_substring)

        return longest_substring
        