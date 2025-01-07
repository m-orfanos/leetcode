package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0226_InvertBinaryTree.invertTree;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import java.util.List;

import org.junit.jupiter.api.Test;

class LT0226_InvertBinaryTreeTest {

    @Test
    void invertTree1() {
        var t1 = toTreeNode(List.of(4, 2, 7, 1, 3, 6, 9));
        var t2 = invertTree(t1);
        assertArrayEquals(
                toArray(4, 7, 2, 9, 6, 3, 1),
                toArray(t2));
    }

}
