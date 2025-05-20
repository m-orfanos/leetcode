package com.morfanos.solutions;

import com.morfanos.shared.ListNode;

class LT0206ReverseLinkedList {

    static ListNode reverseList(ListNode head) {
        ListNode p = null;
        var curr = head;
        while (curr != null) {
            var h = curr;
            curr = curr.next;
            h.next = p;
            p = h;
        }
        return p;
    }

}
