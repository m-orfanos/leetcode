package com.morfanos;

import com.morfanos.utils.ListNode;

class LT0021_MergeTwoSortedLists {

    static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        var ans = new ListNode();

        var t = ans;
        while (list1 != null && list2 != null) {
            var val1 = list1.val;
            var val2 = list2.val;
            if (val1 < val2) {
                t.next = new ListNode(val1);
                list1 = list1.next;
            } else {
                t.next = new ListNode(val2);
                list2 = list2.next;
            }
            t = t.next;
        }

        var rem = list1 != null ? list1 : list2;
        while (rem != null) {
            t.next = new ListNode(rem.val);
            rem = rem.next;
            t = t.next;
        }

        return ans.next;
    }

}
