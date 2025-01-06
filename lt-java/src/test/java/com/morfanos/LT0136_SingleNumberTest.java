package com.morfanos;

import static com.morfanos.LT0136_SingleNumber.singleNumber;
import static com.morfanos.shared.Helper.toArray;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0136_SingleNumberTest {

    @Test
    void singleNumber1() {
        var actual = singleNumber(toArray(2, 2, 1));
        assertEquals(1, actual);
    }

}
