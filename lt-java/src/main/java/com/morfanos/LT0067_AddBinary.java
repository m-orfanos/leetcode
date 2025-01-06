package com.morfanos;

class LT0067_AddBinary {

    private static String reverse(String s, int n, char ch) {
        // reverse and pad right
        StringBuilder sb = new StringBuilder(s);
        sb.reverse();
        while (sb.length() < n) {
            sb.append(ch);
        }
        return sb.toString();
    }

    static String addBinary(String a, String b) {
        var n = a.length() < b.length() ? b.length() : a.length();

        a = reverse(a, n, '0');
        b = reverse(b, n, '0');

        var ans = new StringBuilder();
        var nc = '0';
        for (int i = 0; i < n; i++) {
            var na = a.charAt(i);
            var nb = b.charAt(i);

            if (nc == '0' && na == '0' && nb == '0') {
                // nc = '0';
                ans.append('0');
            } else if (nc == '0' && na == '0' && nb == '1') {
                // nc = '0';
                ans.append('1');
            } else if (nc == '0' && na == '1' && nb == '0') {
                // nc = '0';
                ans.append('1');
            } else if (nc == '0' && na == '1' && nb == '1') {
                nc = '1';
                ans.append('0');
            } else if (nc == '1' && na == '0' && nb == '0') {
                nc = '0';
                ans.append('1');
            } else if (nc == '1' && na == '0' && nb == '1') {
                // nc = '1';
                ans.append('0');
            } else if (nc == '1' && na == '1' && nb == '0') {
                // nc = '1';
                ans.append('0');
            } else if (nc == '1' && na == '1' && nb == '1') {
                // nc = '1';
                ans.append('1');
            }
        }

        if (nc == '1') {
            ans.append('1');
        }

        return ans.reverse().toString();
    }

}
