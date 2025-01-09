package com.morfanos;

import org.junit.jupiter.api.Test;

import static com.morfanos.LT0108ConvertSortedArrayToBinarySearchTree.sortedArrayToBST;
import static com.morfanos.shared.Helper.to1DArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0108ConvertSortedArrayToBinarySearchTreeTest {

    @Test
    void sortedArrayToBST1() {
        var t = sortedArrayToBST(to1DArray(-10, -3, 0, 5, 9));
        var actual = to1DArray(t);
        assertArrayEquals(to1DArray(0, -3, 9, -10, 5), actual);
    }

}
