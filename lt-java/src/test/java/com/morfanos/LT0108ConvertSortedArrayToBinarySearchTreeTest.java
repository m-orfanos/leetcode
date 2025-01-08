package com.morfanos;

import com.morfanos.shared.Helper;
import org.junit.jupiter.api.Test;

import static com.morfanos.LT0108ConvertSortedArrayToBinarySearchTree.sortedArrayToBST;
import static com.morfanos.shared.Helper.to1DArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0108ConvertSortedArrayToBinarySearchTreeTest {

    @Test
    void sortedArrayToBST1() {
        var t = sortedArrayToBST(Helper.to1DArray(-10, -3, 0, 5, 9));
        var actual = to1DArray(t);
        assertArrayEquals(Helper.to1DArray(0, -3, 9, -10, 5), actual);
    }

}
