package com.morfanos.solutions;

import static com.morfanos.solutions.LT0191_Number1Bits.hammingWeight;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0191_Number1BitsTest {

    @Test
    void hammingWeight1() {
        var actual = hammingWeight(11);
        assertEquals(3, actual);
    }

    @Test
    void hammingWeight2() {
        var actual = hammingWeight(2147483645);
        assertEquals(30, actual);
    }

}
