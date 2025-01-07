package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0543_DiameterBinaryTree.diameterOfBinaryTree;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;

import org.junit.jupiter.api.Test;

class LT0543_DiameterBinaryTreeTest {

    @Test
    void diameterOfBinaryTree1() {
        var a = List.of(1, 2, 3, 4, 5);
        var t = toTreeNode(a);
        var actual = diameterOfBinaryTree(t);
        assertEquals(3, actual);
    }

}
