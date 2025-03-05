import heapq

class Solution:
    def largestPalindromic(self, num: str) -> str:
        num_list = []
        heapq.heapify(num_list)
        num_map = {}

        for num_char in num:
            num_int = int(num_char)
            num_map[num_int] = num_map.get(num_int, 0) + 1

        for num in num_map:
            heapq.heappush(num_list, (int(num), num_map[num]))

        largest_pivot = -1
        result = ''
        while len(num_list) > 0:
            candidate, frequency = heapq.heappop(num_list)
            candidate = candidate
            if frequency >= 2 and candidate != 0:
                for i in range(int(frequency / 2)):
                    result = str(candidate) + result + str(candidate)
            if frequency % 2 != 0:
              largest_pivot = max(candidate, largest_pivot)

        if largest_pivot != -1:
            half = len(result) // 2
            result = result[0:half] + str(largest_pivot) + result[half:]
          
        return result
    
s = Solution()
s.largestPalindromic('444947137')

