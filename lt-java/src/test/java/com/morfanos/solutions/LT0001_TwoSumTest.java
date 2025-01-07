package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.solutions.LT0001_TwoSum.twoSum1;
import static com.morfanos.solutions.LT0001_TwoSum.twoSum2;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0001_TwoSumTest {

    @Test
    void twoSumTest1() {
        assertArrayEquals(
                twoSum1(toArray(2, 7, 11, 15), 9),
                toArray(0, 1));
    }

    @Test
    void twoSumTest2() {
        assertArrayEquals(
                twoSum2(toArray(2, 7, 11, 15), 9),
                toArray(0, 1));
    }

}
