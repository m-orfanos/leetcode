package com.morfanos.solutions;

class LT0844BackspaceStringCompare {

    static boolean backspaceCompare(String s, String t) {
        var si = s.length() - 1;
        var sc = 0;

        var ti = t.length() - 1;
        var tc = 0;
        while (si >= 0 && ti >= 0) {
            if (s.charAt(si) == '#') {
                sc += 1;
                si -= 1;
                continue;
            } else if (sc > 0) {
                sc -= 1;
                si -= 1;
                continue;
            }

            if (t.charAt(ti) == '#') {
                tc += 1;
                ti -= 1;
                continue;
            } else if (tc > 0) {
                tc -= 1;
                ti -= 1;
                continue;
            }

            if (s.charAt(si) != t.charAt(ti)) {
                return false;
            }

            si -= 1;
            ti -= 1;
        }

        while (si >= 0) {
            if (s.charAt(si) == '#') {
                sc += 1;
            } else if (sc > 0) {
                sc -= 1;
            } else {
                return false;
            }
            si -= 1;
        }

        while (ti >= 0) {
            if (t.charAt(ti) == '#') {
                tc += 1;
            } else if (tc > 0) {
                tc -= 1;
            } else {
                return false;
            }
            ti -= 1;
        }

        return true;
    }

}
