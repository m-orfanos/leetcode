package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0268MissingNumber.missingNumber;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0268MissingNumberTest {

    @Test
    void missingNumber1() {
        var actual = missingNumber(to1DArray(3, 0, 1));
        assertEquals(2, actual);
    }

    @Test
    void missingNumber2() {
        var actual = missingNumber(to1DArray(0, 1));
        assertEquals(2, actual);
    }

}
