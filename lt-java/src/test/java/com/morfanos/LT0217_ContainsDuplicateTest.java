package com.morfanos;

import static com.morfanos.LT0217_ContainsDuplicate.containsDuplicate;
import static com.morfanos.shared.Helper.toArray;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0217_ContainsDuplicateTest {

    @Test
    void containsDuplicate1() {
        var actual = containsDuplicate(toArray(1, 2, 3, 1));
        assertTrue(actual);
    }

}
