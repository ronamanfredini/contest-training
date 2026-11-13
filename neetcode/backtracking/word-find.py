from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(i, j, word_idx, used):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
                return False
            coordinate = (i, j)
            if coordinate in used:
                return False

            char = word[word_idx]
            if char == board[i][j]:
                if word_idx == len(word) - 1:
                    return True

                used.add(coordinate)
                next_idx = word_idx + 1
                return find(i + 1, j, next_idx, used.copy()) or find(i - 1, j, next_idx, used.copy()) or find(i, j - 1, next_idx, used.copy()) or find(i, j + 1, next_idx, used.copy())

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                char = board[i][j]
                if char == word[0]:
                    used_coordinates = set()
                    res = find(i, j, 0, used_coordinates)
                    if res:
                        return res

        return False
        


def run_case(board: List[List[str]], word: str) -> None:
    """Run Solution.exist on one case and print the result."""
    print(f"board={board} word={word!r}")
    print(f"  got={Solution().exist(board, word)}")


run_case([
    ["A", "B", "C", "E"], 
    ["S", "F", "E", "S"], 
    ["A", "D", "E", "E"]], "ABCESEEEFS")
