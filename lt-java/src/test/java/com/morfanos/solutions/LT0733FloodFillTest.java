package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0733FloodFill.floodFill;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0733FloodFillTest {

    @Test
    void floodFill1() {
        var image = new int[][] { { 1, 1, 1 }, { 1, 1, 0 }, { 1, 0, 1 } };
        var actual = floodFill(image, 1, 1, 2);
        var expected = new int[][] { { 2, 2, 2 }, { 2, 2, 0 }, { 2, 0, 1 } };
        assertArrayEquals(expected, actual);
    }

}
