package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.solutions.LT0014_LongestCommonPrefix.longestCommonPrefix;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0014_LongestCommonPrefixTest {

    @Test
    void longestCommonPrefix1() {
        var actual = longestCommonPrefix(toArray("flower", "flow", "flight"));
        assertEquals("fl", actual);
    }

}
