package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0169MajorityElement.majorityElement;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0169MajorityElementTest {

    @Test
    void majorityElement1() {
        var actual = majorityElement(to1DArray(3, 2, 3));
        assertEquals(3, actual);
    }

    @Test
    void majorityElement2() {
        var actual = majorityElement(to1DArray(2, 2, 1, 1, 1, 2, 2));
        assertEquals(2, actual);
    }

}
