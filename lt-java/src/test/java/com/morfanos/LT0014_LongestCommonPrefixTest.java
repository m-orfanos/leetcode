package com.morfanos;

import static com.morfanos.LT0014_LongestCommonPrefix.longestCommonPrefix;
import static com.morfanos.shared.Helper.toArray;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0014_LongestCommonPrefixTest {

    @Test
    void longestCommonPrefix1() {
        var actual = longestCommonPrefix(toArray("flower", "flow", "flight"));
        assertEquals("fl", actual);
    }

}
