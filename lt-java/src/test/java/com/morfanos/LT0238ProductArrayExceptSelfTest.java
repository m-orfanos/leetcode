package com.morfanos;

import static com.morfanos.LT0238ProductArrayExceptSelf.productExceptSelf;
import static com.morfanos.shared.Helper.to1DArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0238ProductArrayExceptSelfTest {

    @Test
    void productExceptSelf1() {
        var actual = productExceptSelf(to1DArray(1, 2, 3, 4));
        assertArrayEquals(to1DArray(24, 12, 8, 6), actual);
    }

}
