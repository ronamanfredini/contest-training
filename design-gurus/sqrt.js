class Solution {
  mySqrt(x) {
    let left = 1;
    let right = x - 1;
    if (x == 1) {
      return 1
    }
    while (left <= right) {
      const middle = left + Math.floor((right - left) / 2);
      const middleSquared = middle * middle;
      if (middleSquared === x || (middleSquared < x && (middleSquared + 1) * (middleSquared + 1) > x)) {
        return middle;
      }

      if (middleSquared > x) {
        right = middle - 1;
        continue;
      }

      if (middleSquared < x) {
        left = middle + 1;
      }
    }
  
    return 0; 
  };
}

const s = new Solution();
console.log(s.mySqrt(8));
