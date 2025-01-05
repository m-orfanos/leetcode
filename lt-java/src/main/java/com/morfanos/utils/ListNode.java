package com.morfanos.utils;

import java.util.ArrayList;

public class ListNode {
    public int val;
    public ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public static ListNode toListNode(int[] a) {
        if (a.length == 0) {
            return new ListNode();
        }
        var h = new ListNode(a[0]);
        var t = h;
        for (var i = 1; i < a.length; i++) {
            t.next = new ListNode(a[i]);
            t = t.next;
        }
        return h;
    }

    public static int[] toArray(ListNode l) {
        var a = new ArrayList<Integer>();
        while (l != null) {
            a.add(l.val);
            l = l.next;
        }
        return a.stream().mapToInt(i -> i).toArray();
    }
}
