package com.morfanos.solutions;

import static com.morfanos.shared.Helper.to1DArrayObj;
import static com.morfanos.solutions.LT0150ReversePolishNotation.evalRPN;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0150ReversePolishNotationTest {

    @Test
    void evalRPN1() {
        String[] tokens = to1DArrayObj("2", "1", "+", "3", "*");
        var actual = evalRPN(tokens);
        assertEquals(9, actual);
    }

}
