package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0020ValidParentheses.isValid;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0020ValidParenthesesTest {

    @Test
    void isValidTest() {
        assertTrue(isValid("()"));
    }

}
