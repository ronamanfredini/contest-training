// URL - https://neetcode.io/problems/search-2d-matrix
class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let top = matrix.length - 1
        let down = 0;

        while (down <= top) {
            const middle = Math.floor((top + down) / 2);
            const row = matrix[middle];
            const first = row[0];
            const last = row[row.length - 1];

            if (target >= first && target <= last) {
                return this.binarySearch(row, target) === -1? false : true;
            }

            if (target > last) {
                down = middle + 1;
            }

            if (target < first) {
                top = middle - 1;
            }
        }

        return false;
    }

    /**
     * @param {number[]} list
     * @param {number} target
     * @return {number}
     */ 
    binarySearch(list, target) {
        let left = 0;
        let right = list.length - 1;

        while (left <= right) {
            const middle = Math.floor((left + right) / 2);
            if (list[middle] === target) {
                return middle;
            }

            if (target < list[middle]) {
                right = middle - 1;
            }

            if (list[middle] < target) {
                left = middle + 1;
            }
        }

        return -1
    }
}

const s  = new Solution()

const matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

console.log(s.searchMatrix(matrix, target))
