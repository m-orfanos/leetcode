package com.morfanos;

import static com.morfanos.LT0003LongestSubstringWithoutRepeat.lengthOfLongestSubstring1;
import static com.morfanos.LT0003LongestSubstringWithoutRepeat.lengthOfLongestSubstring2;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0003LongestSubstringWithoutRepeatTest {

    @Test
    void lengthOfLongestSubstring11() {
        var actual = lengthOfLongestSubstring1("abcabcbb");
        assertEquals(3, actual);
    }

    @Test
    void lengthOfLongestSubstring12() {
        var actual = lengthOfLongestSubstring1("pwwkew");
        assertEquals(3, actual);
    }

    @Test
    void lengthOfLongestSubstring13() {
        var actual = lengthOfLongestSubstring1(" ");
        assertEquals(1, actual);
    }

    @Test
    void lengthOfLongestSubstring14() {
        var actual = lengthOfLongestSubstring1("dvdf");
        assertEquals(3, actual);
    }

    @Test
    void lengthOfLongestSubstring15() {
        var actual = lengthOfLongestSubstring1("abba");
        assertEquals(2, actual);
    }

    @Test
    void lengthOfLongestSubstring21() {
        var actual = lengthOfLongestSubstring2("abcabcbb");
        assertEquals(3, actual);
    }

    @Test
    void lengthOfLongestSubstring22() {
        var actual = lengthOfLongestSubstring2("pwwkew");
        assertEquals(3, actual);
    }

}
