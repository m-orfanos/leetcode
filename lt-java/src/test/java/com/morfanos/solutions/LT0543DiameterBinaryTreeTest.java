package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import java.util.List;

import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0543DiameterBinaryTree.diameterOfBinaryTree;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0543DiameterBinaryTreeTest {

    @Test
    void diameterOfBinaryTree1() {
        var a = List.of(1, 2, 3, 4, 5);
        var t = toTreeNode(a);
        var actual = diameterOfBinaryTree(t);
        assertEquals(3, actual);
    }

}
