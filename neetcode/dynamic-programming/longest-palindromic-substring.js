// URL - https://neetcode.io/problems/longest-palindromic-substring

class Solution {

  /**
   * @param {string} s
   * @return {boolean}
   */
  isPalindrome(s) {
    let left = 0;
    let right = s.length - 1;

    while (left <= right) {
      if (s[left] !== s[right]) {
        return false;
      }
      left++;
      right--;
    }

    return true;
  }

  /**
   * @param {string} s
   * @return {string}
   */
  longestPalindrome(s) {
    let maxPalindrome = '';

    /**
     * @param {string} s
     * @return {string}
    */
    const findLongest = (str) => {
      if (maxPalindrome.length >= str.length) {
        return;
      }

      if (this.isPalindrome(str)) {
        maxPalindrome = str;
        return;
      }

      findLongest(str.substring(0, str.length - 1));
    };

    for (let i = 0; i < s.length; i++) {
      findLongest(s.substring(i));
    }

    return maxPalindrome
  }
}

const s = new Solution();
const str = 'abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba';

console.log(s.longestPalindrome(str));
