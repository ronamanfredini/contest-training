# Unnoptimized, DP solution

# def sol(cards, k):
#     memo = {}
#     def dfs(i, j, curr_k):
#         if curr_k == k:
#             return 0
        
#         key = (i, j)
#         if key in memo:
#             return memo.get(key)

#         l_card = cards[i]
#         r_card = cards[j]

#         l = dfs(i + 1, j, curr_k + 1) + l_card
#         r = dfs(i, j - 1, curr_k + 1) + r_card

#         result = max(l, r)
#         memo[key] = result

#         return result

#     return dfs(0, len(cards) - 1, 0)


# Sliding window
def sol(cards, k):
    window = sum(cards[:k])
    max_points = window
    for i in range(k):
        left = cards[k - 1 - i]
        right = cards[len(cards) - 1 - i]
        window = (window - left) + right
        max_points = max(max_points, window)

    return window




print(sol([1,2,3,4,5,6,1], 3))
    