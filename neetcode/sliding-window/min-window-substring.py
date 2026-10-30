class Solution:

    def found_substring(self, counter) -> bool:
        for key in counter:
            if counter[key] > 0:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        counter = {}
        left = -1
        min_substring_end = -1
        initial_sub = (-1, -1)
        min_substring = initial_sub

        if len(t) > len(s):
            return ''

        if s == t:
            return s

        for char in t:
            counter[char] = counter.get(char, 0) + 1
        
        for right, char in enumerate(s):
            if char in counter:
                if left == -1:
                    left = right

                counter[char] -= 1
                while counter[char] <= 0:
                    if self.found_substring(counter):
                        curr_sub_len = min_substring[1] - min_substring[0]
                        if right - left < curr_sub_len or min_substring == initial_sub:
                            min_substring = (left, right)


                        min_substring_end = min(min_substring_end, right)
                        if s[left] in counter:
                            if counter[s[left]] + 1 > 0:
                                break

                            counter[s[left]] += 1
                        
                        left += 1
                    else:
                        break

        
        if min_substring == initial_sub:
            return ''

        return s[min_substring[0]:min_substring[1] + 1]


s = Solution()
print(s.minWindow(s = "OUZODYXAZV", t = "XYZ"))