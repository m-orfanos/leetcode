package com.morfanos;

import static com.morfanos.LT0268_MissingNumber.missingNumber;
import static com.morfanos.shared.Helper.toArray;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0268_MissingNumberTest {

    @Test
    void missingNumber1() {
        var actual = missingNumber(toArray(3, 0, 1));
        assertEquals(2, actual);
    }

    @Test
    void missingNumber2() {
        var actual = missingNumber(toArray(0, 1));
        assertEquals(2, actual);
    }

}
