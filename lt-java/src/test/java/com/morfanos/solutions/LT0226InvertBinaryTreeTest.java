package com.morfanos.solutions;

import com.morfanos.shared.Helper;
import org.junit.jupiter.api.Test;

import java.util.List;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0226InvertBinaryTree.invertTree;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0226InvertBinaryTreeTest {

    @Test
    void invertTree1() {
        var t1 = toTreeNode(List.of(4, 2, 7, 1, 3, 6, 9));
        var t2 = invertTree(t1);
        assertArrayEquals(
                Helper.to1DArray(4, 7, 2, 9, 6, 3, 1),
                to1DArray(t2));
    }

}
