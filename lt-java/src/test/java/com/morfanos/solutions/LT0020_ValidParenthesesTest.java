package com.morfanos.solutions;

import static com.morfanos.solutions.LT0020_ValidParentheses.isValid;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0020_ValidParenthesesTest {

    @Test
    void isValidTest() {
        assertTrue(isValid("()"));
    }

}
