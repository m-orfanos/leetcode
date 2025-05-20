package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0136SingleNumber.singleNumber;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0136SingleNumberTest {

    @Test
    void singleNumber1() {
        var actual = singleNumber(to1DArray(2, 2, 1));
        assertEquals(1, actual);
    }

}
