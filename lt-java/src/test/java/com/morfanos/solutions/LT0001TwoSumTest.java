package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0001TwoSum.twoSum1;
import static com.morfanos.solutions.LT0001TwoSum.twoSum2;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0001TwoSumTest {

    @Test
    void twoSumTest1() {
        assertArrayEquals(
                twoSum1(to1DArray(2, 7, 11, 15), 9),
                to1DArray(0, 1));
    }

    @Test
    void twoSumTest2() {
        assertArrayEquals(
                twoSum2(to1DArray(2, 7, 11, 15), 9),
                to1DArray(0, 1));
    }

}
