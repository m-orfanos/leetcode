package com.morfanos.solutions;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0409_LongestPalindromeTest {

    @Test
    void longestPalindrome1() {
        var actual = LT0409_LongestPalindrome.longestPalindrome("abccccdd");
        assertEquals(7, actual);
    }

}
