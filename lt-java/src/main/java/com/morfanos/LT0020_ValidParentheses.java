package com.morfanos;

import java.util.Stack;

class LT0020_ValidParentheses {

    static boolean isValid(String s) {
        var stk = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == ')') {
                if (stk.isEmpty() || stk.pop() != '(') {
                    return false;
                }
            } else if (ch == ']') {
                if (stk.isEmpty() || stk.pop() != '[') {
                    return false;
                }
            } else if (ch == '}') {
                if (stk.isEmpty() || stk.pop() != '{') {
                    return false;
                }
            } else {
                stk.push(ch);
            }
        }
        return stk.empty();
    }

}