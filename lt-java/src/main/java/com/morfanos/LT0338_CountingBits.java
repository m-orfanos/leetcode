package com.morfanos;

class LT0338_CountingBits {

    // 00 0000 0 0
    // 01 0001 1 1
    //
    // 02 0010 1 0+1
    // 03 0011 2 1+1
    //
    // 04 0100 1 0+1
    // 05 0101 2 1+1
    // 06 0110 2 1+1
    // 07 0111 3 2+1
    //
    // 08 1000 1
    // 09 1001 1
    // 10 1010 2
    // 11 1011 3
    // 12 1100 2
    // 13 1101 3
    // 14 1110 3
    // 15 1111 4
    static int[] countBits(int n) {
        if (n == 0) {
            return new int[] { 0 };
        }

        var ans = new int[n + 1];
        // ans[0] = 0;
        ans[1] = 1;
        var offset = 1;
        for (int i = 2; i <= n; i++) {
            if (i == 2 * offset) {
                offset *= 2;
            }
            ans[i] = ans[i - offset] + 1;
        }

        return ans;
    }

}
