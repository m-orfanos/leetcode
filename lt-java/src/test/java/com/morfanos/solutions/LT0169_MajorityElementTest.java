package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.solutions.LT0169_MajorityElement.majorityElement;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0169_MajorityElementTest {

    @Test
    void majorityElement1() {
        var actual = majorityElement(toArray(3, 2, 3));
        assertEquals(3, actual);
    }

    @Test
    void majorityElement2() {
        var actual = majorityElement(toArray(2, 2, 1, 1, 1, 2, 2));
        assertEquals(2, actual);
    }

}
