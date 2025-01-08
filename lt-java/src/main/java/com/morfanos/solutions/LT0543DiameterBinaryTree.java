package com.morfanos.solutions;

import com.morfanos.shared.TreeNode;

class LT0543DiameterBinaryTree {

    private static int[] go(TreeNode n) {
        if (n == null) {
            return new int[] { 0, 0 };
        }

        var l = go(n.left);
        var lh = l[0];
        var ld = l[1];

        var r = go(n.right);
        var rh = r[0];
        var rd = r[1];

        var h = 1 + Math.max(lh, rh);
        var d = Math.max(ld, Math.max(rd, lh + rh));

        return new int[] { h, d };
    }

    static int diameterOfBinaryTree(TreeNode root) {
        return go(root)[1];
    }

}
