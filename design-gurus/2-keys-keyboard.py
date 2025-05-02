def solution(n):
    memo = {}
    def dfs(clipboard, current_str):
        if len(current_str) == n:
            return 0
        if len(current_str) > n or n < len(clipboard) + len(current_str):
            return 1e9
        
        memo_key = (current_str)
        if memo_key in memo:
            return memo.get(memo_key)

        paste_path = dfs(clipboard, current_str + clipboard) + 1
        update_clip_path = dfs(clipboard + current_str, current_str) + 1

        result = min(paste_path, update_clip_path)
        memo[memo_key] = result

        return result
    

    return dfs("A", "A") + 1


# print(solution(9))
print(solution(5))
# print(solution(4))
# print(solution(2))