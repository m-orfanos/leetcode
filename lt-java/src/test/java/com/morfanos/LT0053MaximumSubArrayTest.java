package com.morfanos;

import com.morfanos.shared.Helper;
import org.junit.jupiter.api.Test;

import static com.morfanos.LT0053MaximumSubArray.maxSubArray1;
import static com.morfanos.LT0053MaximumSubArray.maxSubArray2;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0053MaximumSubArrayTest {

    @Test
    void maxSubArray11() {
        var actual = maxSubArray1(Helper.to1DArray(-2, 1, -3, 4, -1, 2, 1, -5, 4));
        assertEquals(6, actual);
    }

    @Test
    void maxSubArray21() {
        var actual = maxSubArray2(Helper.to1DArray(-2, 1, -3, 4, -1, 2, 1, -5, 4));
        assertEquals(6, actual);
    }

}
