class Solution {
  /**
   * 
   * @param {string} str 
   * @returns {boolean}
   */
  isPalindrome(str) {
    let l = 0;
    let r = str.length - 1;

    while (l <= r) {
      if (str[l] !== str[r]) {
        return false;
      }

      l++;
      r--;
    }

    return true;
  }

  /**
   * 
   * @param {string} str 
   * @returns {number}
   */
  getPalindromeCount(str) {
    if (str.length === 0) {
      return 0;
    }

    const increment = this.isPalindrome(str) ? 1 : 0;
    return this.getPalindromeCount(str.substring(0, str.length - 1)) + increment;
  }

  /**
   * @param {string} s
   * @return {number}
   */
  countSubstrings(s) {
    let palindromeCount = 0;
    for (let i = 0; i < s.length; i++) {
      palindromeCount += this.getPalindromeCount(s.substring(i));
    }
    
    return palindromeCount
  }
}

const s = new Solution();
const str = "aaa";

console.log(s.countSubstrings(str))
