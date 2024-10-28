// URL - https://neetcode.io/problems/permutation-string

class Solution {
  /**
   * @param {string} s1
   * @param {string} s2
   * @return {boolean}
   */
  checkInclusion(s1, s2) {
    const s1Map = new Map();
    let l = -1
    let currPermutationLen = 0;

    if (s1.length > s2.length) {
      return false;
    }

    for (const char of s1) {
      const charCount = (s1Map.get(char) || 0) + 1;
      s1Map.set(char, charCount);
    }

    for (let r = 0; r < s2.length; r++) {
      const char = s2[r];
      let s1Char = s1Map.get(char);

      while (!s1Char && l !== -1) {
        const lChar = s2[l];
        s1Map.set(lChar, s1Map.get(lChar) + 1)
        l++;
        currPermutationLen--;
        if (currPermutationLen === 0) {
          l = -1;
        }
        s1Char = s1Map.get(char);
      }

      if (s1Char) {
        if (l === -1) {
          l = r;
        }

        s1Map.set(char, s1Char - 1);

        currPermutationLen++;
        if (currPermutationLen === s1.length) {
          return true;
        }
      }
    }

    return false;
  }
}


const sol = new Solution();

const  s1 = "adc", s2 = "dcda"

console.log(sol.checkInclusion(s1, s2));