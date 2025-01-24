class Solution {
  removeDuplicateLetters(s) {
    let newStr = '';
    const existingChars = new Map();
    for (const char of s) {
      if (!existingChars.has(char)) {
        newStr += char;
        existingChars.set(char, newStr.length - 1);
        continue;
      }

      const charIdxOnMap = existingChars.get(char);
      for (let right = newStr.length - 1; right > charIdxOnMap; right--) {
        const currChar = s[right];
        if (char.charCodeAt(0) < currChar.charCodeAt(0)) {
          newStr = newStr.substring(0, charIdxOnMap) + newStr.substring(charIdxOnMap + 1) + char;
          break;
        }
      }
      existingChars.set(char, newStr.length - 1);
    }
    return newStr;
  }
}

const s = new Solution();
console.log(s.removeDuplicateLetters('bcabc'));