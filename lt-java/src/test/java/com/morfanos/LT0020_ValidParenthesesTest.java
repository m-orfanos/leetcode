package com.morfanos;

import static com.morfanos.LT0020_ValidParentheses.isValid;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0020_ValidParenthesesTest {

    @Test
    void isValidTest() {
        assertTrue(isValid("()"));
    }

}
