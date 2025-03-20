from collections import deque

class Solution:

    # Method to find the length of the longest subarray with an absolute difference less than or equal to limit
    def longestSubarray(self, nums, limit):
        deques = []
        unique_integers = set()

        for num in nums:
            for d in deques:
                first = d[0]
                last = d[-1]

                fits_queue = abs(first - num) <= limit and abs(last - num) <= limit
                if fits_queue:
                    if num < first:
                        d.appendleft(num)
                    elif num > last:
                        d.append(num)
                    # else:
                    #     temp = d.pop()
                    #     d.append(num)
                    #     d.append(temp)

            if num not in unique_integers:
                unique_integers.add(num)
                deques.append(deque([num]))
        
        result = 0
        for d in deques:
            result = max(len(d), result)

        return result

s = Solution()
print(s.longestSubarray([8,2,4,10,12], 6)) 