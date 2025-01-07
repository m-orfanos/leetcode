package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0235_LowestCommonAncestor.lowestCommonAncestor;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

import com.morfanos.shared.TreeNode;

class LT0235_LowestCommonAncestorTest {

    @Test
    void lowestCommonAncestor1() {
        var l = Arrays.asList(6, 2, 8, 0, 4, 7, 9, null, null, 3, 5);
        var t = toTreeNode(l);
        var actual = lowestCommonAncestor(t, new TreeNode(2), new TreeNode(8));
        assertEquals(6, actual.val);
    }

}
