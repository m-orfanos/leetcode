package com.morfanos.shared;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Helper {

    public static int[] toArray(int... a) {
        return a;
    }

    // *** ListNode *** //
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

    // *** TreeNode *** //
    public static TreeNode toTreeNode(List<Integer> a) {
        if (a.isEmpty()) {
            return null;
        }

        record Tuple(int i, TreeNode t) {
        }

        var head = new TreeNode(a.get(0));

        Queue<Tuple> q = new LinkedList<>();
        q.add(new Tuple(0, head));
        while (!q.isEmpty()) {
            var tup = q.poll();
            var i = tup.i;
            var t = tup.t;

            var left = 2 * i + 1;
            var right = 2 * i + 2;

            if (left < a.size() && a.get(left) != null) {
                t.left = new TreeNode(a.get(left));
                q.add(new Tuple(left, t.left));
            }

            if (right < a.size() && a.get(right) != null) {
                t.right = new TreeNode(a.get(right));
                q.add(new Tuple(right, t.right));
            }
        }

        return head;
    }

    public static int[] toArray(TreeNode t) {
        List<Integer> l = new ArrayList<>();

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(t);
        while (!q.isEmpty()) {
            var n = q.poll();
            if (n == null) {
                continue;
            }
            l.add(n.val);
            q.add(n.left);
            q.add(n.right);
        }

        return l.stream().mapToInt(i -> i).toArray();
    }

}
