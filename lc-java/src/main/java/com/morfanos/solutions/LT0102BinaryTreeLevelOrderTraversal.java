package com.morfanos.solutions;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import com.morfanos.shared.TreeNode;

class LT0102BinaryTreeLevelOrderTraversal {

    static List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return List.of();
        }

        record Tuple(TreeNode node, int level) {
        }

        var ans = new ArrayList<List<Integer>>();

        var q = new LinkedList<Tuple>();
        q.add(new Tuple(root, 0));

        while (!q.isEmpty()) {
            var t = q.poll();

            if (ans.size() < t.level + 1) {
                ans.add(new ArrayList<>());
            }
            ans.get(t.level).add(t.node.val);

            if (t.node.left != null) {
                q.add(new Tuple(t.node.left, t.level + 1));
            }
            if (t.node.right != null) {
                q.add(new Tuple(t.node.right, t.level + 1));
            }

        }

        return ans;
    }

}
