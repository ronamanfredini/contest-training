import heapq
class Solution:
    def findLRSLength(self, str):
        subsequences_map = {}
        subsequences = []
        heapq.heapify(subsequences)

        def backtrack(i, curr_subsequence = ''):
            if i >= len(str):
                if curr_subsequence in subsequences_map:
                    heapq.heappush(subsequences, len(curr_subsequence))

                subsequences_map[curr_subsequence] = True

                return
            
            curr_element = str[i]
            take_curr = curr_subsequence + curr_element
            backtrack(i + 1, take_curr)
            backtrack(i + 1, curr_subsequence)
            return

        backtrack(0)
        print(subsequences)
        print(heapq.heappop(subsequences))
        return 1

s = Solution()
print(s.findLRSLength('tomorrow'))