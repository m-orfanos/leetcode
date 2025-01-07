package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.solutions.LT0338_CountingBits.countBits;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0338_CountingBitsTest {

    @Test
    void countBits1() {
        var actual = countBits(2);
        assertArrayEquals(toArray(0, 1, 1), actual);
    }

    @Test
    void countBits2() {
        var actual = countBits(5);
        assertArrayEquals(toArray(0, 1, 1, 2, 1, 2), actual);
    }

    @Test
    void countBits3() {
        var actual = countBits(8);
        assertArrayEquals(toArray(0, 1, 1, 2, 1, 2, 2, 3, 1), actual);
    }

}
