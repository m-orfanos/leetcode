package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0009PalindromeNumber.isPalindrome;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0009PalindromeNumberTest {

    @Test
    void isPalindrome1() {
        var actual = isPalindrome(121);
        assertTrue(actual);
    }

    @Test
    void isPalindrome2() {
        var actual = isPalindrome(-121);
        assertFalse(actual);
    }

    @Test
    void isPalindrome3() {
        var actual = isPalindrome(10);
        assertFalse(actual);
    }

}
