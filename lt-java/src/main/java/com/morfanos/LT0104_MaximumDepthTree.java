package com.morfanos;

import com.morfanos.shared.TreeNode;

class LT0104_MaximumDepthTree {

    static int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        var ld = maxDepth(root.left);
        var rd = maxDepth(root.right);
        return 1 + Math.max(ld, rd);
    }

}
