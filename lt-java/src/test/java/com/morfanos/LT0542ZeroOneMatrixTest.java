package com.morfanos;

import static com.morfanos.LT0542ZeroOneMatrix.updateMatrix;
import static com.morfanos.shared.Helper.to2DArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0542ZeroOneMatrixTest {

    @Test
    void updateMatrix1() {
        var mat = to2DArray(
                0, 0, 0,
                0, 1, 0,
                0, 0, 0);
        var actual = updateMatrix(mat);
        var expected = to2DArray(0, 0, 0, 0, 1, 0, 0, 0, 0);
        assertArrayEquals(expected, actual);
    }

    @Test
    void updateMatrix2() {
        var mat = to2DArray(
                0, 0, 0,
                0, 1, 0,
                1, 1, 1);
        var actual = updateMatrix(mat);
        var expected = to2DArray(0, 0, 0, 0, 1, 0, 1, 2, 1);
        assertArrayEquals(expected, actual);
    }

}
