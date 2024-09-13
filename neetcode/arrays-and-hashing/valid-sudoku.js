// URL - https://neetcode.io/problems/valid-sudoku

class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const rowCheckedMap = new Map();
        const columnCheckedMap = new Map();

        for (let i = 0; i < board.length; i++) {
            for (let j = 0; j < board[i].length; j++) {
                if (rowCheckedMap.has(i)) {
                    continue;
                }
            }
        }
    }
}


const solution = new Solution();

const board = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]
console.log(solution.isValidSudoku(board));