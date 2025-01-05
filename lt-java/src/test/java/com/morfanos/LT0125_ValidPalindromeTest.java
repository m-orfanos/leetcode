package com.morfanos;

import static com.morfanos.LT0125_ValidPalindrome.isPalindrome;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0125_ValidPalindromeTest {

    @Test
    void isPalindrome1() {
        var ans = isPalindrome("A man, a plan, a canal: Panama");
        assertTrue(ans);
    }

    @Test
    void isPalindrome2() {
        var ans = isPalindrome("0P");
        assertFalse(ans);
    }

}
