package com.morfanos;

class LT0190_ReverseBits {

    static int reverseBits(int n) {
        var isNeg = n < 0;
        if (isNeg) {
            n = ~n;
        }

        var rev = 0;
        var i = 0;
        while (i < 32) {
            rev = (rev << 1) + (n & 0b1);
            n >>= 1;
            i++;
        }

        if (isNeg) {
            rev = ~rev;
        }

        return rev;
    }

}