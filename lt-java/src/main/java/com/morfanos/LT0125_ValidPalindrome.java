package com.morfanos;

class LT0125_ValidPalindrome {

    static boolean isPalindrome(String s) {
        int a = 'a'; // 97
        int z = 'z'; // 122
        int A = 'A'; // 65
        int Z = 'Z'; // 90

        var lhs = 0;
        var rhs = s.length() - 1;
        while (lhs < rhs) {
            // ignore non-alphanumeric
            var clhs = s.charAt(lhs);
            if (!((a <= clhs && clhs <= z)
                    || (A <= clhs && clhs <= Z)
                    || ('0' <= clhs && clhs <= '9'))) {
                lhs += 1;
                continue;
            }
            var crhs = s.charAt(rhs);
            if (!((a <= crhs && crhs <= z)
                    || (A <= crhs && crhs <= Z)
                    || ('0' <= crhs && crhs <= '9'))) {
                rhs -= 1;
                continue;
            }

            // to lowercase
            if (A <= clhs && clhs <= Z) {
                clhs += (a - A);
            }
            if (A <= crhs && crhs <= Z) {
                crhs += (a - A);
            }

            // finally check
            if (clhs != crhs) {
                return false;
            }

            lhs += 1;
            rhs -= 1;
        }

        return true;
    }

}
