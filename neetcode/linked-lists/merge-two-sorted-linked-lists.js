// URL - https://neetcode.io/problems/merge-two-sorted-linked-lists

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
  /**
   * @param {ListNode} list1
   * @param {ListNode} list2
   * @return {ListNode}
   */
  mergeTwoLists(list1, list2) {
    const listHead = new ListNode();
    let current = listHead;

    while (list1 && list2) {
      if (list1.val <= list2.val) {
        current.next = list1;
        list1 = list1.next
      } else {
        current.next = list2;
        list2 = list2.next
      }
      current = current.next
    }

    while (list1) {
      current.next = list1;
      current = list1;
      list1 = list1.next
    }

    while (list2) {
      current.next = list2;
      current = list2;
      list2 = list2.next
    }

    return listHead.next
  }
}

let list1 = [1,2,4], list2 = [1,3,5]

list1 = list1.reverse().reduce((acc, curr) => new ListNode(curr, acc), null);
list2 = list2.reverse().reduce((acc, curr) => new ListNode(curr, acc), null);

const sol = new Solution()

console.log(sol.mergeTwoLists(list1, list2));