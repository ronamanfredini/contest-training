import heapq

def sol(nums):
    num_count = 0
    n = len(nums)
    heap = []
    heapq.heapify(heap)

    for i in range(n):
        heapq.heappush(heap, (nums[i] * 2, i))

    for i in range(n):
        for num_times_two, index in heap:
            if num_times_two >= nums[i]:
                break

            if i < index:
                num_count += 1
    


    return num_count


# Test cases
# print(sol([1, 3, 2, 3, 5]))  # 2
# print(sol([4, 3, 4, 1])) # 3
print(sol([6, 5, 4, 3, 2, 1]))