package com.morfanos;

import static com.morfanos.LT0102BinaryTreeLevelOrderTraversal.levelOrder;
import static com.morfanos.shared.Helper.toTreeNode;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

class LT0102BinaryTreeLevelOrderTraversalTest {

    @Test
    void levelOrder11() {
        var l = Arrays.asList(3, 9, 20, null, null, 15, 7);
        var t = toTreeNode(l);
        var actual = levelOrder(t);
        var expected = List.of(
                List.of(3),
                List.of(9, 20),
                List.of(15, 7));
        assertEquals(expected, actual);
    }

}
