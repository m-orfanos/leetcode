package com.morfanos;

import static com.morfanos.LT0053_MaximumSubarray.maxSubArray1;
import static com.morfanos.LT0053_MaximumSubarray.maxSubArray2;
import static com.morfanos.shared.Helper.toArray;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0053_MaximumSubarrayTest {

    @Test
    void maxSubArray11() {
        var actual = maxSubArray1(toArray(-2, 1, -3, 4, -1, 2, 1, -5, 4));
        assertEquals(6, actual);
    }

    @Test
    void maxSubArray21() {
        var actual = maxSubArray2(toArray(-2, 1, -3, 4, -1, 2, 1, -5, 4));
        assertEquals(6, actual);
    }

}
