package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0125ValidPalindrome.isPalindrome;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0125ValidPalindromeTest {

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
