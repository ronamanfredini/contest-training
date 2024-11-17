// URL - https://neetcode.io/problems/search-for-word

class Solution {
  /**
   * @param {character[][]} board
   * @param {string} word
   * @return {boolean}
   */
  exist(board, word) {
    const alreadyVisited = new Map();
    const recurse = (letterIndex, i, j) => {
      if (!board[i] || !board[i][j]) {
        return false;
      }
      const visitedKey = `${i}${j}`;
      const letter = word[letterIndex];
      const currentBoardLetter = board[i][j];

      if (alreadyVisited.has(visitedKey) || currentBoardLetter !== letter) {
        return false;
      }
      alreadyVisited.set(visitedKey, true);

      if (letterIndex === word.length - 1) {
        return true;
      }

      const result = recurse(letterIndex + 1, i - 1, j) ||
        recurse(letterIndex + 1, i + 1, j) ||
        recurse(letterIndex + 1, i, j + 1) ||
        recurse(letterIndex + 1, i, j - 1)

      alreadyVisited.delete(visitedKey);
      return result;


    }

    for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[i].length; j++) {
        if (recurse(0, i, j)) {
          return true;
        }
      }
    }

    return false;
  }
}

const board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
const word = "AAAAAAAAAAAAAAB"

const s = new Solution();
console.log(s.exist(board, word))
