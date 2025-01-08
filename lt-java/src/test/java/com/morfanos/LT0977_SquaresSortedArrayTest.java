package com.morfanos;

import static com.morfanos.LT0977_SquaresSortedArray.sortedSquares;
import static com.morfanos.shared.Helper.toArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0977_SquaresSortedArrayTest {

    @Test
    void sortedSquares1() {
        var actual = sortedSquares(toArray(-4, -1, 0, 3, 10));
        assertArrayEquals(toArray(0, 1, 9, 16, 100), actual);
    }

    @Test
    void sortedSquares2() {
        var actual = sortedSquares(toArray(-7, -3, 2, 3, 11));
        assertArrayEquals(toArray(4, 9, 9, 49, 121), actual);
    }

}
