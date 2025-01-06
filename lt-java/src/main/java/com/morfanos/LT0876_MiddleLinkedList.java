package com.morfanos;

import com.morfanos.shared.ListNode;

class LT0876_MiddleLinkedList {

    static ListNode middleNode(ListNode head) {
        var slow = head;
        var fast = head.next;
        while (slow != null && fast != null) {
            slow = slow.next;
            fast = fast.next == null ? null : fast.next.next;
        }
        return slow;
    }

}
