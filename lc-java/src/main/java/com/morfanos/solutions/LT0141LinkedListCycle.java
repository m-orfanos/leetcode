package com.morfanos.solutions;

import com.morfanos.shared.ListNode;

class LT0141LinkedListCycle {

    static boolean hasCycle(ListNode head) {
        var slow = head;
        var fast = head == null ? null : head.next;
        while (slow != null && fast != null) {
            if (slow == fast) {
                return true;
            }
            slow = slow.next;
            fast = fast.next == null ? null : fast.next.next;
        }
        return false;
    }

}
