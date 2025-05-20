package com.morfanos.solutions;

import com.morfanos.shared.TreeNode;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0235LowestCommonAncestor.lowestCommonAncestor;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0235LowestCommonAncestorTest {

    @Test
    void lowestCommonAncestor1() {
        var l = Arrays.asList(6, 2, 8, 0, 4, 7, 9, null, null, 3, 5);
        var t = toTreeNode(l);
        var actual = lowestCommonAncestor(t, new TreeNode(2), new TreeNode(8));
        assertEquals(6, actual.val);
    }

}
