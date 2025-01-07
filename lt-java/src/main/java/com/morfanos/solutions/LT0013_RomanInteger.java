package com.morfanos.solutions;

import java.util.Map;

class LT0013_RomanInteger {

    static int romanToInt(String s) {
        var m = Map.of(
                'I', 1,
                'V', 5,
                'X', 10,
                'L', 50,
                'C', 100,
                'D', 500,
                'M', 1000);

        var ans = m.get(s.charAt(0));
        for (var i = 1; i < s.length(); i++) {
            ans += m.get(s.charAt(i));
            if (m.get(s.charAt(i - 1)) < m.get(s.charAt(i))) {
                ans -= 2 * m.get(s.charAt(i - 1));
            }
        }

        return ans;
    }

}
