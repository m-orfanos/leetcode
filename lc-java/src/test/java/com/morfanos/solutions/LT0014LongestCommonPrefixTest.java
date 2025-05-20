package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArrayObj;
import static com.morfanos.solutions.LT0014LongestCommonPrefix.longestCommonPrefix;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0014LongestCommonPrefixTest {

    @Test
    void longestCommonPrefix1() {
        var actual = longestCommonPrefix(to1DArrayObj("flower", "flow", "flight"));
        assertEquals("fl", actual);
    }

}
