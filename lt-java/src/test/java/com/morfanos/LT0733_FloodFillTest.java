package com.morfanos;

import static com.morfanos.LT0733_FloodFill.floodFill;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0733_FloodFillTest {

    @Test
    void floodFill1() {
        var image = new int[][] { { 1, 1, 1 }, { 1, 1, 0 }, { 1, 0, 1 } };
        var actual = floodFill(image, 1, 1, 2);
        var expected = new int[][] { { 2, 2, 2 }, { 2, 2, 0 }, { 2, 0, 1 } };
        assertArrayEquals(expected, actual);
    }

}
