package com.morfanos;

import org.junit.jupiter.api.Test;

import static com.morfanos.LT0977SquaresSortedArray.sortedSquares;
import static com.morfanos.shared.Helper.to1DArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0977SquaresSortedArrayTest {

    @Test
    void sortedSquares1() {
        var actual = sortedSquares(to1DArray(-4, -1, 0, 3, 10));
        assertArrayEquals(to1DArray(0, 1, 9, 16, 100), actual);
    }

    @Test
    void sortedSquares2() {
        var actual = sortedSquares(to1DArray(-7, -3, 2, 3, 11));
        assertArrayEquals(to1DArray(4, 9, 9, 49, 121), actual);
    }

}
