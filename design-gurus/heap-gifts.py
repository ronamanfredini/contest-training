import heapq, math  # Importing the heapq module for efficient heap operations

class Solution:
    def remainingGifts(self, gifts, k):
        negated_gifts = []
        for num in gifts:
            negated_gifts.append(num * -1)

        heapq.heapify(negated_gifts)
        for i in range(k):
            num = heapq.heappop(negated_gifts) * -1
            num = int(math.sqrt(num))
            heapq.heappush(negated_gifts, num * -1)

        sum = 0
        for num in negated_gifts:
            sum += num * -1

        return int(sum)


s = Solution()
print(s.remainingGifts([4, 9, 16], 2))
