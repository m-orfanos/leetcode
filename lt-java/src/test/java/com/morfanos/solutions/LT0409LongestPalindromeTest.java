package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0409LongestPalindrome.longestPalindrome;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0409LongestPalindromeTest {

    @Test
    void longestPalindrome1() {
        var actual = longestPalindrome("abccccdd");
        assertEquals(7, actual);
    }

}
