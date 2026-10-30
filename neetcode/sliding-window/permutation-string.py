class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_set = {}
        sub_len = len(s1)
        for c in s1:
            hash_set[c] = hash_set.get(c, 0) + 1

        left = 0
        for right, c in enumerate(s2):
            if c in hash_set and hash_set[c] > 0:
                hash_set[c] -= 1
                sub_len -= 1
                if sub_len == 0:
                    return True
            if c not in hash_set or hash_set[c] < 0:
                while left <= right:
                    if s2[left] in hash_set:
                        hash_set[s2[left]] += 1
                        left += 1
                        sub_len += 1
                        break
                    left += 1
        return False


        

s = Solution()
print(s.checkInclusion('ab', 'eidboaoo'))