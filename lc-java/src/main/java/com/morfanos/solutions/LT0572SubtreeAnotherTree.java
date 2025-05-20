package com.morfanos.solutions;

import com.morfanos.shared.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class LT0572SubtreeAnotherTree {

    // Helper methods
    private static List<Integer> toList(TreeNode t) {
        List<Integer> l = new ArrayList<>();
        var s = new Stack<TreeNode>();
        s.push(t);
        while (!s.isEmpty()) {
            var n = s.pop();
            if (n == null) {
                l.add(null);
            } else {
                l.add(n.val);
                s.add(n.left);
                s.add(n.right);
            }
        }
        return l;
    }

    private static boolean isEqual(Integer a, Integer b) {
        return (a == null && b == null) || (a != null && a.equals(b));
    }

    // **** Approach 1 **** //
    private static boolean go(TreeNode n, TreeNode t) {
        if (n == null && t == null) {
            return true;
        }

        if (n == null || t == null) {
            return false;
        }

        return n.val == t.val && go(n.left, t.left) && go(n.right, t.right);

    }

    static boolean isSubtree1(TreeNode root, TreeNode subRoot) {
        var stk = new Stack<TreeNode>();
        stk.add(root);

        while (!stk.isEmpty()) {
            var r = stk.pop();

            if (go(r, subRoot)) {
                return true;
            }

            if (r.left != null) {
                stk.add(r.left);
            }

            if (r.right != null) {
                stk.add(r.right);
            }
        }

        return false;
    }

    // **** Approach 2 **** //
    static boolean isSubtree2(TreeNode root, TreeNode subRoot) {
        var r = toList(root);
        var s = toList(subRoot);

        for (int i = 0; i < r.size(); i++) {
            if (isEqual(r.get(i), s.get(0))) {
                var isSub = true;
                for (int j = 0; j < s.size(); j++) {
                    if (i + j >= r.size() || !isEqual(r.get(i + j), s.get(j))) {
                        isSub = false;
                        break;
                    }
                }
                if (isSub) {
                    return true;
                }
            }
        }

        return false;
    }

    // **** Approach 3 **** //
    private static int[] constructLps(List<Integer> pat) {
        var lps = new int[pat.size()];
        var len = 0;

        // lps[0] = 0;

        var i = 1;
        while (i < pat.size()) {
            if (isEqual(pat.get(i), pat.get(len))) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }

        return lps;
    }

    // List<Integer>
    private static boolean kmpSearch(List<Integer> pat, List<Integer> txt) {
        var n = txt.size();
        var m = pat.size();

        // var res = new ArrayList<Integer>();
        var lps = constructLps(pat);

        var i = 0;
        var j = 0;

        while (i < n) {
            if (isEqual(txt.get(i), pat.get(j))) {
                i++;
                j++;
                if (j == m) {
                    // res.add(i - j);
                    // j = lps[j - 1];
                    return true;
                }
            } else {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }

        // return res;
        return false;
    }

    static boolean isSubtree3(TreeNode root, TreeNode subRoot) {
        var ar = toList(root);
        var as = toList(subRoot);
        return kmpSearch(as, ar);
    }

}
