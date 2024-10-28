/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
  /**
   * @param {ListNode} head
   * @return {ListNode}
   */
  reverseList(head) {
      const stack = [];
      if (!head) {
          return null
      }
      while (head) {
          stack.push(head);
          head = head.next
      }


      const listStart = stack.pop();
      let curr = listStart;
      while (stack.length > 0) {
          const next = stack.pop();
          curr.next = next;
          curr = next;
          if (stack.length === 0) {
              curr.next = null
          }

      }

      return listStart
  }
}