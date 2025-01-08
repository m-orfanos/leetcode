package com.morfanos.solutions;

import com.morfanos.shared.ListNode;

class LT0234PalindromeLinkedList {

    static boolean isPalindrome(ListNode head) {
        // find midpoint
        var slow = head;
        var fast = head.next;
        while (fast != null) {
            slow = slow.next;
            fast = fast.next == null ? null : fast.next.next;
        }

        // reverse midpoint -> end
        ListNode p = null;
        var curr = slow;
        while (curr != null) {
            var h = curr;
            curr = curr.next;
            h.next = p;
            p = h;
        }

        // compare
        while (head != null && p != null) {
            if (head.val != p.val) {
                return false;
            }
            head = head.next;
            p = p.next;
        }

        return true;
    }

}
