// URL - https://neetcode.io/problems/minimum-window-with-characters

class Solution {
  /**
   * @param {string} s
   * @param {string} t
   * @return {string}
   */
  minWindow(s, t) {
    const tMap = new Map();
    let minSubstring = '';
    let currSubstring

    if (s.length < t.length) {
      return '';
    }

    for (const char of t) {
      const tChar = (tMap.get(char) || 0) + 1;
      tMap.set(char, tChar);
    }

    for (let r = 0, l = -1; r < s.length; r++) {
      let tCharCount = tMap.get(s[r]);

      while (l !== -1 && !tCharCount) {

      }

    }


    return minSubstring;
  }
}


const sol = new Solution()
const s = "OUZODYXAZV", t = "XYZ"

console.log(sol.minWindow(s, t))