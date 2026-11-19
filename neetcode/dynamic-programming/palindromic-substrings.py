class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        def ex(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.count += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                ex(i, i + 1)
            ex(i, i)
             
        return self.count

s = Solution()
print(s.countSubstrings('aaa'))