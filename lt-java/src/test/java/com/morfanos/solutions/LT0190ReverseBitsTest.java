package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0190ReverseBits.reverseBits;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0190ReverseBitsTest {

    @Test
    void reverseBits1() {
        var actual = reverseBits(43261596);
        assertEquals(964176192, actual);
    }

    @Test
    void reverseBits2() {
        var actual = reverseBits(-3);
        assertEquals(-1073741825, actual);
    }

    @Test
    void reverseBits3() {
        var actual = reverseBits(-1763388427);
        assertEquals(-1345640599, actual);
    }

    @Test
    void reverseBits4() {
        var actual = reverseBits(1);
        assertEquals(-2147483648, actual);
    }

    @Test
    void reverseBits5() {
        var actual = reverseBits(-2147483648);
        assertEquals(1, actual);
    }

    @Test
    void reverseBits6() {
        var actual = reverseBits(-1431655766);
        assertEquals(1431655765, actual);
    }

}
