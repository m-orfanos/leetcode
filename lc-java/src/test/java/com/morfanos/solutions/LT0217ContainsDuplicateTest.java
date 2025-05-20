package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0217ContainsDuplicate.containsDuplicate;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0217ContainsDuplicateTest {

    @Test
    void containsDuplicate1() {
        var actual = containsDuplicate(to1DArray(1, 2, 3, 1));
        assertTrue(actual);
    }

}
