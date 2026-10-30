import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        result = [-heap[0][0]]

        left = 0
        for right in range(k, len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            left += 1
            heap_top = heap[0]
            while heap_top[1] < left:
                heapq.heappop(heap)
                heap_top = heap[0]
            
            result.append(-heap_top[0])

        return result




s = Solution()
print(s.maxSlidingWindow(nums=[-7,-8,7,5,7,1,6,0], k=4))