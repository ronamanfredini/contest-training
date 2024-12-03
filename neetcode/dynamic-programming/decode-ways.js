//URL - https://neetcode.io/problems/decode-ways
class Solution {
  fromCharCode(num) {
    return String.fromCharCode(num + 65 - 1);    
  }

  getCharCode(c) {
    return c.toUpperCase().charCodeAt() - 65 + 1;
  }

  /**
   * @param {string} s
   * @return {number}
   */
  numDecodings(s) {
    if ((s.length === 1 || s.length === 2) && s[0] === '0') {
      return 0;
    }

    const decode = (str) => {
      if (!str || str.length <= 1) {
        return 1;
      }

      if (str.length === 2) {
        const intElements = parseInt(str);
        if (intElements >= 26 ||  intElements > 10) {
          return 2;
        }

        return 1;
      }

      return decode(str.substring(0, str.length - 2)) * 1;
    }

    return decode(s);
  }
}


const s = new Solution();
const str = '226';

console.log(s.numDecodings(str));
