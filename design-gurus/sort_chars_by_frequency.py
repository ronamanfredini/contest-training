import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        letter_count = {}
        for char in s:
            char_count = letter_count.get(char, 0) + 1
            letter_count[char] = char_count
        
        my_heap = []
        heapq.heapify(my_heap)
        for key in letter_count:
            heapq.heappush(my_heap, (letter_count[key] * -1, key))
        
        result = ''
        while len(my_heap) > 0:
            heap_res = heapq.heappop(my_heap)
            for i in range(heap_res[0] * -1):
                result += heap_res[1]


        # ToDo: Write Your Code Here.
        return result


s = Solution()
print(s.frequencySort('trersesess'))