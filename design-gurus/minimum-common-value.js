class Solution {
  binarySearch(array, value) {
      let start = 0;
      let end = array.length - 1;

      while (start <= end) {
          const middle = start + Math.floor((end - start) / 2);
          const middleElement = array[middle];
          if (middleElement === value) {
              return middle;
          }

          if (value < middleElement) {
              end = middle - 1;
          } else {
              start = middle + 1;
          }
      }

      return -1;
  }

  findMinimumCommonValue(nums1, nums2) {
      const smallerArray = nums1.length <= nums1 ? nums1 : nums2;
      const biggerArray = nums1.length <= nums1 ? nums2 : nums1;

      for (const num of smallerArray) {
        const result = this.binarySearch(biggerArray, num);
        if (result !== -1) {
          return biggerArray[result];
        }
      }

      return -1;
  }
}


const s = new Solution()
const nums1 = [1, 3, 5, 7], nums2 = [3, 4, 5, 6, 8, 10]
console.log(s.findMinimumCommonValue(nums1, nums2))
console.log(s.binarySearch(nums1, 7))