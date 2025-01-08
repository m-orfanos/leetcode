package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0338CountingBits.countBits;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0338CountingBitsTest {

    @Test
    void countBits1() {
        var actual = countBits(2);
        assertArrayEquals(to1DArray(0, 1, 1), actual);
    }

    @Test
    void countBits2() {
        var actual = countBits(5);
        assertArrayEquals(to1DArray(0, 1, 1, 2, 1, 2), actual);
    }

    @Test
    void countBits3() {
        var actual = countBits(8);
        assertArrayEquals(to1DArray(0, 1, 1, 2, 1, 2, 2, 3, 1), actual);
    }

}
