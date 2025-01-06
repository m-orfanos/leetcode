package com.morfanos;

class LT0014_LongestCommonPrefix {

    static String longestCommonPrefix(String[] strs) {
        var len = Integer.MAX_VALUE;
        for (var i = 0; i < strs.length; i++) {
            len = Math.min(len, strs[i].length());
        }

        var i = 0;
        while (i < len) {
            var curr = strs[0].charAt(i);
            for (var j = 1; j < strs.length; j++) {
                if (curr != strs[j].charAt(i)) {
                    return strs[0].substring(0, i);
                }
            }
            i += 1;
        }

        return strs[0].substring(0, len);
    }

}
