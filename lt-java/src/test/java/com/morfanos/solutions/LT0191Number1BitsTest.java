package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0191Number1Bits.hammingWeight;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0191Number1BitsTest {

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
