# DP

def sol(heights, bricks, ladders):
    def dfs(i, bricks, ladders):
        if i >= len(heights) - 1:
            return len(heights) - 1

        if bricks == 0 and ladders == 0:
            return i

        if heights[i] >= heights[i + 1]:
            return dfs(i + 1, bricks, ladders)

        ladder_path = i
        if ladders > 0:
            ladder_path = dfs(i + 1, bricks, ladders - 1)

        height_diff = heights[i + 1] - heights[i]
        brick_path = i
        if bricks >= height_diff:
            brick_path = dfs(i + 1, bricks - height_diff, ladders)

        result = max(brick_path, ladder_path)
        return result

    return dfs(0, bricks, ladders)


# HEAP

import heapq


def sol(heights, bricks, ladders):
    heap = []
    heapq.heapify(heap)

    for i in range(len(heights) - 1):
        if heights[i] >= heights[i + 1]:
            continue

        diff = heights[i + 1] - heights[i]
        if diff <= bricks:
            heapq.heappush(heap, -diff)
            bricks -= diff
            continue

        if ladders <= 0:
            return i

        bricks -= heapq.heappop(heap)
        ladders -= 1

    return len(heights) - 1
