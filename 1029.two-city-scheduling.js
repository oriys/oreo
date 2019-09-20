
/**
 * @param {ListNode} head
 * @return {number[]}
 */
let nextLargerNodes = function (head) {
    let slow = head;
    let fast = slow.next;
    let arr = [];
    while (fast != null) {
        while (slow.val >= fast.val && fast.next != null) {
            fast = fast.next;
        }
        if (slow.val >= fast.val) {
            arr.push(0);
        }
        else {
            arr.push(fast.val);
        }
        slow = slow.next;
        fast = slow.next;
    }
    if (slow != null) {
        arr.push(0);
    }
    return arr;
};