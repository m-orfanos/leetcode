package com.morfanos.solutions;

import java.util.List;
import java.util.Stack;

class LT0150ReversePolishNotation {

    static int evalRPN(String[] tokens) {
        var ops = List.of("+", "-", "*", "/");
        var s = new Stack<Integer>();
        for (var token : tokens) {
            if (!ops.contains(token)) {
                s.add(Integer.parseInt(token, 10));
            } else {
                var n2 = s.pop();
                var n1 = s.pop();
                if ("+".equals(token)) {
                    s.push(n1 + n2);
                } else if ("-".equals(token)) {
                    s.push(n1 - n2);
                } else if ("*".equals(token)) {
                    s.push(n1 * n2);
                } else {
                    s.push(n1 / n2);
                }
            }
        }

        return s.pop();
    }

}
