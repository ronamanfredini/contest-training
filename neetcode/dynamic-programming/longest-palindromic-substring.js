// URL - https://neetcode.io/problems/longest-palindromic-substring

class Solution {
  /**
   * @param {string} s
   * @return {string}
   */
  longestPalindrome(s) {
    let maxPalindrome = s[0];
    const dfs = (currentPalindrome = '', i = 0) => {
      if (currentPalindrome.length > maxPalindrome.length) {
        const reversed = [...currentPalindrome].reverse().join('');
        if (currentPalindrome === reversed) {
          maxPalindrome = reversed;
        }
      }

      if (i >= s.length) {
        return;
      }

      currentPalindrome += s[i];
      dfs(currentPalindrome, i + 1);
      currentPalindrome = currentPalindrome.slice(currentPalindrome.length - 1);
      dfs(currentPalindrome, i + 1);
    }
    dfs();
    return maxPalindrome
  }
}

const s = new Solution();
const str = 'abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba';

console.log(s.longestPalindrome(str));
