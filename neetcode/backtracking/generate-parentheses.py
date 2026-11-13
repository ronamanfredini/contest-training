from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        OPEN = '('
        CLOSE = ')'
        freq = {OPEN: n, CLOSE: n}
        res = []

        def dfs(curr, open_count = 0):
            if freq[OPEN] == 0 and freq[CLOSE] == 0:
                res.append(''.join(curr))
                return
            elif freq[CLOSE] == 0 and freq[OPEN] > 0:
                return

            if freq[OPEN] > 0:
                freq[OPEN] -= 1
                curr.append(OPEN)
                open_count += 1
                dfs(curr, open_count)
                popped = curr.pop()
                if popped == OPEN:
                    open_count -= 1
                freq[popped] += 1

            if len(curr) > 0 and open_count > 0:
                curr.append(CLOSE)
                freq[CLOSE] -= 1
                open_count -= 1
                dfs(curr, open_count)
                popped = curr.pop()
                if popped == OPEN:
                    open_count -= 1
                freq[popped] += 1


        dfs([], 0)
        return res

def run_case(n: int) -> None:
    """Run generateParenthesis on n and print the result."""
    print(f"n={n}")
    print(f"  got={Solution().generateParenthesis(n)}")


run_case(3)
